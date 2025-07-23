import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import time
from langchain_ollama import ChatOllama

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parser import summary_parser


def ice_break_with(name: str) -> str:
    linkedin_username_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username_url, mock=True)
    summary_template = '''
    given the linkedin information {information} about a person, I want you to create:
    1. A short summary
    2. two interesting facts about their career (not linkedin profile).
    \n{format_instructions}
    '''
    summary_prompt_template = PromptTemplate(
        input_variables=['information'],
        template=summary_template,
        partial_variables={'format_instructions': summary_parser.get_format_instructions()},
    )
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    chain = summary_prompt_template | llm | summary_parser
    res = chain.invoke(input={'information': linkedin_data})
    print(res)


# TASK: Given a text about a person, return the following: 1. Summary about the person 2. Two interesting facts.
if __name__ == "__main__":
    load_dotenv()
    print('Ice Breaker enter')
    ice_break_with(name='Rahul Kavi ServiceNow')
