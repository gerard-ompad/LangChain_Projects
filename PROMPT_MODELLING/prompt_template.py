#author:gdompad#
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import pandas as pd

api_key = pd.read_csv('/Users/gerardompad/Desktop/API_KEY/openai.csv')
api_key = api_key[api_key.name == 'openai']['code'][0]

information = """Angela Dorothea Merkel (German: [ aŋ'ɡela doʁoˈteːa ˈmɛʁkl̩] (listen);[a] née Kasner; born 17 July 1954) is a German former politician and scientist who served as Chancellor of Germany from November 2005 to December 2021. A member of the Christian Democratic Union (CDU), she previously served as Leader of the Opposition from 2002 to 2005 and as Leader of the Christian Democratic Union from 2000 to 2018.[9] Merkel was the first female chancellor of Germany.[10] During her tenure as Chancellor, Merkel was frequently referred to as the de facto leader of the European Union (EU), the most powerful woman in the world, and, beginning in 2016, was contended as the leader of the free world.[11][12][13][14][15]

Merkel was born in Hamburg in then-West Germany, moving to East Germany as an infant when her father, a Lutheran clergyman, received a pastorate in Perleberg. She obtained a doctorate in quantum chemistry in 1986 and worked as a research scientist until 1989.[16] Merkel entered politics in the wake of the Revolutions of 1989, briefly serving as deputy spokeswoman for the first democratically elected Government of East Germany led by Lothar de Maizière. Following German reunification in 1990, Merkel was elected to the Bundestag for the state of Mecklenburg-Vorpommern. As the protégée of Chancellor Helmut Kohl, Merkel was appointed as Minister for Women and Youth in 1991, later becoming Minister for the Environment, Nature Conservation and Nuclear Safety in 1994. After the CDU lost the 1998 federal election, Merkel was elected CDU General Secretary, before becoming the party's first female leader and the first female Leader of the Opposition two years later, in the aftermath of a donations scandal that toppled Wolfgang Schäuble.

Following the 2005 federal election, Merkel was appointed to succeed Gerhard Schröder as Chancellor of Germany, leading a grand coalition consisting of the CDU, its Bavarian sister party the Christian Social Union (CSU) and the Social Democratic Party of Germany (SPD). Merkel was the first woman to be elected as Chancellor, and the first Chancellor since reunification to have been raised in the former East Germany. At the 2009 federal election, the CDU obtained the largest share of the vote, and Merkel was able to form a coalition government with the Free Democratic Party (FDP).[17] At the 2013 federal election, Merkel's CDU won a landslide victory with 41.5% of the vote and formed a second grand coalition with the SPD, after the FDP lost all of its representation in the Bundestag.[18] At the 2017 federal election, Merkel led the CDU to become the largest party for the fourth time; Merkel formed a third grand coalition with the SPD and was sworn in for a joint-record fourth term as Chancellor on 14 March 2018.[19]

In foreign policy, Merkel has emphasised international cooperation, both in the context of the EU and NATO, and strengthening transatlantic economic relations. In 2008, Merkel served as President of the European Council and played a central role in the negotiation of the Treaty of Lisbon and the Berlin Declaration. Merkel played a crucial role in managing the global financial crisis of 2007–2008 and the European debt crisis. She negotiated the 2008 European Union stimulus plan focusing on infrastructure spending and public investment to counteract the Great Recession. In domestic policy, Merkel's Energiewende program has focused on future energy development, seeking to phase out nuclear power in Germany, reduce greenhouse gas emissions, and increase renewable energy sources. Reforms to the Bundeswehr which abolished conscription, health care reform, and her government's response to the 2010s European migrant crisis and the COVID-19 pandemic in Germany were major issues during her chancellorship.[20] She served as the senior G7 leader from 2011 to 2012 and again from 2014 to 2021. In 2014, she became the longest-serving incumbent head of government in the EU. In October 2018, Merkel announced that she would stand down as Leader of the CDU at the party convention, and would not seek a fifth term as chancellor in the 2021 federal election.[21] In 2022, Merkel condemned the Russian invasion of Ukraine..."""
print('information')
print(information)
if __name__ == '__main__':
    summary_template = """Given the information {information} about a person, create:
                        1. A short summary.
                        1. Two interesting Facts about them."""


    summary_prompt_template = PromptTemplate(input_variables = ["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name = "gpt-3.5-turbo", openai_api_key=api_key)

    chain = LLMChain(llm=llm, prompt = summary_prompt_template)

    print(chain.run(information = information))