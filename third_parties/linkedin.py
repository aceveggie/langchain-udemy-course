import os
import requests
from dotenv import load_dotenv
import pprint

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    '''
    Scrape LinkedIn profile using linkedin_profile_url,
    Manually scrape the information from the LinkedIn profile
    :param linkedin_profile_url: string that describes the LinkedIn profile
    :param mock: boolean that describes whether if we need to mock it (true for mock testing)
    :return:scrai
    '''
    pprint.pprint(requests.get(
        'https://gist.githubusercontent.com/aceveggie/3a28e3f9f973d62ae75baecf775fec30/raw/be14d53a565fc31d47a6fa0f8b67a94133fbfbfe/rahul-kavi-scrapin.json').json())
    return ''

if __name__ == '__main__':
    print(scrape_linkedin_profile())