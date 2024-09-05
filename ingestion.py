from dotenv import load_dotenv
load_dotenv()
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import  PineconeVectorStore

def read_dcos():
    print("Running Processing")
    loader = ReadTheDocsLoader('langchain-docs/api.python.langchain.com/en/latest')
    documents = loader.load()
    print(len(documents))
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=750, chunk_overlap=60)
    documents = text_splitter.split_documents(documents)
    for doc in documents:
        # print(doc)
        # print(doc.metadata)
        # break
        new_url = doc.metadata["source"]
        new_url = new_url.replace("langchain-docs", "https:/")
        doc.metadata.update({"source": new_url})

    print(f"Adding {len(documents)} to Pinecone")

    PineconeVectorStore.from_documents(
        documents, embeddings, index_name = "documentation-index"
    )

if __name__ == '__main__':
    embeddings = OpenAIEmbeddings()
    read_dcos()


