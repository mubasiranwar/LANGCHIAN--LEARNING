from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
# 1. Load webpage
url = 'https://adeenaperfume.com/'
loader = WebBaseLoader(url)
#Converting into streamlit ui

# 2. Load documents
docs = loader.load()  # Fixed: removed hyphen, added space

parser=StrOutputParser()
model=ChatOpenAI(
        model="deepseek/deepseek-r1-distill-llama-70b:free",
        base_url="https://openrouter.ai/api/v1",
        temperature=0.7
    ) 

prompt = PromptTemplate(
    template='Give a brief summary of the following webpage content - \n {webpage_content}',
    input_variables=['webpage_content']
)

print(len(docs))

chain=prompt | model | parser

print(chain.invoke({'webpage_content':docs[0].page_content}))
