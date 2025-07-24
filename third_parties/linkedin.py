import os
import requests
from dotenv import load_dotenv
import pprint

from urllib3 import response

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    '''
    Scrape LinkedIn profile using linkedin_profile_url,
    Manually scrape the information from the LinkedIn profile
    :param linkedin_profile_url: string that describes the LinkedIn profile
    :param mock: boolean that describes whether if we need to mock it (true for mock testing)
    :return:scrai
    '''
    rahul_gist_json = 'https://gist.githubusercontent.com/aceveggie/3a28e3f9f973d62ae75baecf775fec30/raw/be14d53a565fc31d47a6fa0f8b67a94133fbfbfe/rahul-kavi-scrapin.json'
    marco_gist_json = 'https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json'
    if mock:
        linkedin_profile_url = marco_gist_json
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = 'https://api.scrapin.io/v1/enrichment/profile'
        apikey = os.getenv('SCRAPIN_API_KEY')
        linkedInUrl = linkedin_profile_url
        params = {'apikey': apikey, 'linkedInUrl': linkedInUrl}
        response = requests.get(api_endpoint, params=params, timeout=10)
    data = response.json().get('person')
    # remove information that is empty
    data = {
        k: v
        for k, v in data.items()
        if (v not in ([], "", "") and k != 'photoUrl') or k == 'photoUrl'  # Always keep photoUrl
        and k not in ['certifications', 'languages', 'skills', 'work', 'education']
    }
    return data

if __name__ == '__main__':
    linkedin_profile_url = 'https://www.linkedin.com/in/eden-marco/'
    pprint.pprint(scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url, mock=False))
