import os
from langchain.vectorstores.redis import Redis
from langchain.embeddings import OpenAIEmbeddings

os.environ['OPENAI_API_KEY'] = "YOUR_API_KEY"
embeddings = OpenAIEmbeddings()

rds = Redis.from_existing_index(
    embeddings, redis_url="redis://localhost:6379", index_name="link"
)

results = rds.similarity_search("where does mrs ruan live")

print(results[0].page_content)