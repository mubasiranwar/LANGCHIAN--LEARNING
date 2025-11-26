from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()



# Step 1: Make a prompt template
prompt = ChatPromptTemplate.from_template("Explain {topic} like I am 10 years old.")

# Step 2: Connect an AI model from OpenRouter
model = ChatOpenAI(
    model="deepseek/deepseek-r1-distill-llama-70b:free",
    base_url="https://openrouter.ai/api/v1",
    temperature=0.7
)

# Step 3: Chain prompt and model
chain = prompt | model

# Step 4: Run it
result = chain.invoke({"topic": "Who is the president of pakistan"})
print(result.content)
