from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import (
    RunnableLambda,
    RunnablePassthrough,
    RunnableParallel,
)

class DocAnswerChain:
    def __init__(self):
        self.init_prompt = '''You are a legal contract answering specialist. Given the context of a legal contract and a related query, provide a brief and precise response. If the answer is not available in the given context, respond with "I don't know."'''

        # Setting up the language model with specific parameters
        self.qa_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    def generate_response_chain(self, retriever_base):
        contract_template = """{self.init_prompt}
        
        ### CONTRACT CONTEXT
        {context}

        ### User Query
        Query: {query_prompt}
        """

        # Create a prompt template with the above instructions
        question_prompt = ChatPromptTemplate.from_template(contract_template)

        # Combining the retriever and user input
        parallel_retriever = RunnableParallel(
            {
                "contract_context": itemgetter("query_prompt") | retriever_base,
                "query_prompt": itemgetter("query_prompt"),
            }
        )

        # Setting up the retrieval-augmented QA chain
        qa_chain = parallel_retriever | {
            "response": question_prompt | self.qa_model,
            "context": itemgetter("contract_context"),
        }
        return qa_chain