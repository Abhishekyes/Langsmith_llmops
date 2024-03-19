from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant.Please response to the user request only based on the given context"),  # Added comma here
        ("user","Question:{question}\nContext:{context}")
    ]
)


model=ChatOpenAI(model="gpt-3.5-turbo")
output_parser= StrOutputParser()
chain=prompt|model|output_parser
question="Can you summarize the speech?"
context="""APJ Abdul Kalam was appointed to the Indian Ministry of Defense as a Technical Advisor in 1992, after which he served with DRDO and ISRO, the country's largest organization. Considered a national hero for successful nuclear tests in 1998, a second successful nuclear test was conducted in Pokhran the same year under his supervision, after which India was included in the list of nuclear-powered nations. Abdul Kalam has been active in all space programs and development programs in India as a scientist. For developing India's Agni missile, Kalam was called 'Missile Man.'Abdul Kalam made a special technological and scientific contribution, for which, along with Bharat Ratna, India's highest honour, he was awarded the Padma Bhushan, Padam Vibhushan, etc. He was also awarded an honorary doctorate by more than 30 universities in the world for the same. 

 """

print(chain.invoke({"question":question,"context":context}))
