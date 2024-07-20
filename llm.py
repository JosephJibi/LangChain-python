from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key="sk-proj-lRiarById1qINSPJOT9cT3BlbkFJCMgsTpTidoispK0xuhaq",
    model="gpt-3.5-turbo"
)

response = llm.invoke("Hello, How are you?")

print(response)