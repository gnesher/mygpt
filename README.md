# mygpt
A small LangChain/OpenAI chat based on your own context

The example book - "The Four Corners in California" by Amy Ella Blanchard, is provided by the Gutenberg project.  

## Getting started
* Set up a local Python enviroment with virutalenv
* Run pip install -r requirements.txt to get dependencies
* Add your OPEN-AI API key to all the python files (or just set an enviroment variable)
* Set up a Redis database locally or using [Redis Cloud](https://redis.com/redis-enterprise-cloud/overview/)
* run python data_praser.py - which will generate the vector embeddings
* run python chat.py - To start the CLI chat
