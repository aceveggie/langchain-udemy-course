'''
gets the LinkedIn profile URL
Uses tavily package
'''
from langchain_community.tools import TavilySearchResults


def get_profile_url_tavily(name: str):
    '''searches for LinkedIn profile URL or Twitter Page'''
    search = TavilySearchResults()
    res = search.run(f'{name}')
    return res
