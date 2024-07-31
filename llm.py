from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7, verbose=True)
# response = llm.invoke("Hello, how are you?") # Simple way to ask questions.
# response = llm.batch(["Hello, how are  you?", "Example use of linear algebra in ML"]) # We can give array of messages, all of this messages is processed concurrently.

# print(response)

# To Get Streaming response.
responseChunks = llm.stream("write a poem about AI")
for chunk in responseChunks:
        print(chunk.content, end="", flush=True)