import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.redis import Redis

loader = TextLoader("thefourcorners.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
docs = text_splitter.split_documents(documents)

# set your openAI api key as an environment variable
os.environ['OPENAI_API_KEY'] = "YOUR_API_KEY"

# we will use OpenAI as our embeddings provider
embeddings = OpenAIEmbeddings()

rds = Redis.from_documents(
    docs, embeddings, redis_url="redis://localhost:6379", index_name="chunk"
)
