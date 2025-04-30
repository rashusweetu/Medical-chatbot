# Healthcare RAG Agent 🤖

I decided to build this chatbot, with the help of Real Python's LLM RAG Chatbot [tutorial](https://realpython.com/build-llm-rag-chatbot-with-langchain), to have an LLM project to build upon as I learn new topics and experiment with new ideas.

Along the way, I learned about LangChain, how and when to use graph databases, and how to quickly deploy LLM RAG apps with FastAPI and Streamlit.


## Why don't you check it out? 

Start by cloning this repo and adding a .env file with the following environment variables:

```
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>

NEO4J_URI=<YOUR_NEO4J_URI>
NEO4J_USERNAME=<YOUR_NEO4J_USERNAME>
NEO4J_PASSWORD=<YOUR_NEO4J_PASSWORD>

HOSPITALS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/hospitals.csv
PAYERS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/payers.csv
PHYSICIANS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/physicians.csv
PATIENTS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/patients.csv
VISITS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/visits.csv
REVIEWS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/reviews.csv

HOSPITAL_AGENT_MODEL=gpt-4 0125 preview
HOSPITAL_CYPHER_MODEL=gpt-4 0125 preview
HOSPITAL_QA_MODEL=gpt-4 0125 preview

CHATBOT_URL=http://host.docker.internal:8000/hospital-rag-agent
```

Next, navigate to the project root, start Docker, and run:

```
make build
```

The build will start the servers, however, you can also do so with:

```
make start
```

and stop all containers by running:

```
make stop
```

You can interact with the chatbot on `localhost:8501`:

<img width="1614" alt="Screenshot 2024-03-27 at 19 44 54" src="https://github.com/asanmateu/healthcare-rag-chatbot/assets/62403518/ef6de300-5dbd-41a0-b89f-34fbe94473bf">
