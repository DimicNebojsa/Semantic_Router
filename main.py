
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# Set up the LLM Chain to return a single word based on the query,
# and based on a list of words we provide to it in the prompt template
llm_completion_select_route_chain = (
        PromptTemplate.from_template("""
Given the user question below, classify it as either
being about `LangChain`, `Anthropic`, or `Other`.

Do not respond with more than one word.

<question>
{question}
</question>

Classification:"""
                                     )
        | ChatAnthropic(model_name="claude-3-haiku")
        | StrOutputParser()
)

# We setup an IF/Else condition to route the query to the correct chain
# based on the LLM completion call above
def route_to_chain(route_name):
    if "anthropic" == route_name.lower():
        return anthropic_chain
    elif "langchain" == route_name.lower():
        return langchain_chain
    else:
        return general_chain

...

# Later on in the application, we can use the response from the LLM
# completion chain to control (i.e route) the flow of the application
# to the correct chain via the route_to_chain method we created
route_name = llm_completion_select_route_chain.invoke(user_query)
chain = route_to_chain(route_name)
chain.invoke(user_query)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')


