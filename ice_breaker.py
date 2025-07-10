import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import time
from langchain_ollama import ChatOllama

# TASK: Given a text about a person, return the following: 1. Summary about the person 2. Two interesting facts.
if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain!")
    # given information about a person
    information = '''Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman known for his leadership of Tesla, SpaceX, and X (formerly Twitter). Since 2025, he has been a senior advisor to United States president Donald Trump and the de facto head of the Department of Government Efficiency (DOGE). Musk has been considered the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion. He was named Time magazine's Person of the Year in 2021. Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada. He graduated from the University of Pennsylvania in the U.S. before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became a U.S. citizen.'''

    # describe summary_template
    summary_template = '''Given this text about a person: {information}, I want you to return the following in less than 500 words: 1. One paragraph summary about the person (max 5 sentences) 2. Two interesting facts.'''

    summary_prompt_template = PromptTemplate(input_variables=['information'], template=summary_template)
    # llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo') # takes forever to run locally
    llm = ChatOllama(model='llama2:latest') # reasonably fast 20 sec call for 1000 words
    chain = summary_prompt_template | llm
    # chain = summary_prompt_template | llm | StrOutputParser # this is taking really long and 
    start_time = time.time()
    print('started calling')
    res = chain.invoke(input={'information': information})
    print('finished calling')
    print('time taken', time.time()-start_time)
    # print(res)
    print(res.content)
