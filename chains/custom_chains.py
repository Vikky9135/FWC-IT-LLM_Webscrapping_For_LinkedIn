from langchain_core.runnables import RunnableSequence
from langchain.prompts.prompt import PromptTemplate
from output_parsers import summary_parser
from langchain_openai import ChatOpenAI
from output_parsers import topics_of_interest_parser
from output_parsers import ice_breaker_parser



llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
llm_creative = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")




def get_summary_chain() -> RunnableSequence:
    summary_template = """
         given the information about a person from LinkedIn {information}, I want you to create:
         1. a short summary
         2. two interesting facts about them
         \n{format_instructions}
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    return summary_prompt_template | llm | summary_parser


def get_interests_chain() -> RunnableSequence:
    interesting_facts_template = """
         given the information about a person from LinkedIn {information}, I want you to create:
         3 topics that might interest them
        \n{format_instructions}
     """

    interesting_facts_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=interesting_facts_template,
        partial_variables={
            "format_instructions": topics_of_interest_parser.get_format_instructions()
        },
    )

    return interesting_facts_prompt_template | llm | topics_of_interest_parser


def get_ice_breaker_chain() -> RunnableSequence:
    ice_breaker_template = """
         given the information about a person from LinkedIn {information}, I want you to create:
         2 creative Ice breakers with them that are derived from their LinkedIn activity
        \n{format_instructions}
     """

    ice_breaker_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=ice_breaker_template,
        partial_variables={
            "format_instructions": ice_breaker_parser.get_format_instructions()
        },
    )

    return ice_breaker_prompt_template | llm | ice_breaker_parser