#author:gdompad#
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import pandas as pd
import os
import requests

api = pd.read_csv('/Users/gerardompad/Desktop/API_KEY/openai.csv')
api_key = api[api.name == 'openai']['code'][0]
proxy_url_api = api[api.name == 'proxyrul']['code']
proxy_url_api_index = api[api.name == 'proxyurl']['code'].index
proxy_url_api = api[api.name == 'proxyurl']['code'][int(proxy_url_api_index[0])]

if __name__ == '__main__':
    def scrape_linkedin_data(linkedin_profile_url):
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        header_dic = {"Authorization":f"Bearer.{os.environ.get(proxy_url_api)}"}
        response = requests.get(api_endpoint, params = {"url":linkedin_profile_url},headers = header_dic)
        
    linkedin_data = scrape_linkedin_data('https://www.linkedin.com/in/gerard-ompad/')
    print(linkedin_data)
'''
    summary_template = """Given the information {information} about a person, create:
                        1. A short summary.
                        1. Two interesting Facts about them."""


    summary_prompt_template = PromptTemplate(input_variables = ["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name = "gpt-3.5-turbo", openai_api_key=api_key)

    chain = LLMChain(llm=llm, prompt = summary_prompt_template)

    print(chain.run(information = information))'''