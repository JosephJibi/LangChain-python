### Using ChatPromptTemplate.from_template

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)

# Using Prompt Template we can en-force a behavior.

# Prompt Template
prompt = ChatPromptTemplate.from_template("Tell me a joke about {subject}, {subject2}")

# Chain Creation
chain = prompt | llm

response = chain.invoke({"subject": "rain","subject2":  "wind"}) # If there is only one value then we can do like this: chain.invoke("rain")
print(response.content)