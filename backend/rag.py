import os

from dotenv import load_dotenv
from langchain.chains.history_aware_retriever import create_history_aware_retriever

load_dotenv()
from langchain.chains.retrieval import create_retrieval_chain
from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

def get_response(query: str, chat_history):
    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI(verbose = True, temperature = 0)
    vector_database = PineconeVectorStore(
        index_name=os.getenv('PINECONE_INDEX_NAME'),
        embedding=embeddings
    )
    prompt = hub.pull('langchain-ai/retrieval-qa-chat')
    rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")
    print(rephrase_prompt)
    history_aware_retriever = create_history_aware_retriever(
        llm=llm, retriever=vector_database.as_retriever(), prompt=rephrase_prompt
    )
    document_stuff = create_stuff_documents_chain(
        llm, prompt
    )

    chain = create_retrieval_chain(
        retriever=history_aware_retriever, combine_docs_chain=document_stuff
    )

    result = chain.invoke(input={'input':query, 'chat_history':chat_history})
    final_res = {
        "query" : result["input"],
        "result" : result["answer"],
        "source_documents" : result["context"]
    }
    return final_res


if __name__ == '__main__':
    answer = get_response(query='What is the langchain chain')
    print(answer)

