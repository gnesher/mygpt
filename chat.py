import os
from langchain.vectorstores.redis import Redis
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# set your openAI api key as an environment variable
os.environ['OPENAI_API_KEY'] = "YOUR_API_KEY"

embeddings = OpenAIEmbeddings()

rds = Redis.from_existing_index(
    embeddings, redis_url="redis://localhost:6379", index_name="chunk"
)

retriever = rds.as_retriever()

model = ChatOpenAI(
    temperature= 0,
    model_name= 'gpt-3.5-turbo',
  )

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
qa = ConversationalRetrievalChain.from_llm(llm=model, retriever=retriever, memory=memory)

print("Ask any question regarding The Four Corners in California book:")

# keep the bot running in a loop to simulate a conversation
while True:
    question = input()
    result = qa({"question": question})
    print(result["answer"])
