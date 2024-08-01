from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser, JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.7)


def call_string_output_parser():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Tell me a joke about following subject"),
            ("human", "{input}")
        ]
    )

    parser = StrOutputParser()
    chain = prompt | llm | parser
    return chain.invoke({"input": "rain"})

def call_list_output_parser():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Generate list of 10 synonyms for the following word. Return results as a comma separated"),
            ("human", "{input}")
        ]
    )

    parser = CommaSeparatedListOutputParser()
    chain = prompt | llm | parser
    return chain.invoke("Rain")



### IMPORTANT
def call_json_output_parser_one():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Extract information from the following phrase. \n Formatting Instructions: {format_instructions}"),
            ("human", "{phrase}")
        ]
    )

    # Class Person is inheriting BaseModal - look at the syntax.
    class Person(BaseModel):
        # we can add any type like this
        # TODO: Need to explore this using different types
        name: str = Field(description="the name of the person")
        age:  int = Field(description="the age of the person")


    parser = JsonOutputParser(pydantic_object=Person) # Take a look at this
    chain = prompt | llm | parser

    return chain.invoke({
        "phrase": "Athul is 22 years old",
        "format_instructions": parser.get_format_instructions()  # Take a look at this
    })

# example 2 of json output parser
def call_json_output_parser_two():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Extract information from the following phrase. \n Formatting Instructions: {format_instructions}"),
            ("human", "{phrase}")
        ]
    )

    class Person(BaseModel):
        recipe: str = Field(description="the name of the recipe")
        ingredients:  list = Field(description="ingredients")


    parser = JsonOutputParser(pydantic_object=Person)
    chain = prompt | llm | parser
    return chain.invoke({
        "phrase": "The ingredients for a  Margherita pizza are tomatoes, onion, cheese, basil",
        "format_instructions": parser.get_format_instructions()
    })





# print(call_string_output_parser())
# print(call_list_output_parser())
# print(call_json_output_parser_one())
print(call_json_output_parser_two())