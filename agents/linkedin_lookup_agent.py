import os
from dotenv import load_dotenv
from langchain import hub

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (create_react_agent, AgentExecutor)
from tools.tools import get_profile_url_tavily

def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0.0,
        model_name= 'gpt-3.5-turbo',
    )
    template = '''given the full name {name_of_person}, I want you to get me a link to their LinkedIn profile page. 
    Your answer should only contain a URL, nothing else'''
    prompt_template = PromptTemplate(template=template, input_variables=['name_of_person'])
    tools_for_agent = [
        Tool(
            name = 'Crawl Google for LinkedIn profile page',
            func=get_profile_url_tavily,
            description='useful for when you need to get  LinkedIn profile page URL',
        )
    ]
    react_prompt = hub.pull('hwchase17/react')
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt,
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=False)
    result = agent_executor.invoke(
        input = {'input':prompt_template.format_prompt(name_of_person = name)}
    )
    linkedin_profile_url = result['output']
    return linkedin_profile_url

if __name__ == '__main__':
    linked_in_url = lookup(name='Rahul Kavi ServiceNow LinkedIn')
    # print(linked_in_url)
