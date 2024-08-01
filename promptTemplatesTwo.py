###  Using ChatPromptTemplate.from_messages

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, convert_system_message_to_human=True)

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
    ("system", "Generate list of 10 synonyms for the following word. Return results as a comma separated"),
    ("human", "{input}")
    ]
)

# LLM chain
chain = prompt | llm

response = chain.invoke({"input": "happy"})

print(response.content)




# Note:
# GenAI model like: "gemini-pro", "gemini-flash" - don't  support SystemMessage directly(from_messages in this case).
# So, we can use 'convert_system_message_to_human=True'
# This will add the system message to the first human message in the sequence.
# Reference: Link -  https://github.com/langchain-ai/langchain/discussions/24817
# Update on this issue(on Aug 1, 2024) -  we can use modal 'gemini-1.5-pro-latest' to fix this issue. it the current mdoal.