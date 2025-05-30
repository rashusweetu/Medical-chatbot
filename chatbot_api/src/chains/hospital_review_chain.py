import os
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)

# Use OpenAIEmbeddings without manually passing client (fixes proxy issue in 0.0.8+)
embedding = OpenAIEmbeddings(
    model="text-embedding-3-small"  # or whatever embedding model you're using
)

neo4j_vector_index = Neo4jVector.from_existing_graph(
    embedding=embedding,
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
    index_name="reviews",
    node_label="Review",
    text_node_properties=[
        "physician_name",
        "patient_name",
        "text",
        "hospital_name",
    ],
    embedding_node_property="embedding",
)

review_template = """Your job is to use patient
reviews to answer questions about their experience at a hospital. Use
the following context to answer questions. Be as detailed as possible, but
don't make up any information that's not from the context. If you don't know
an answer, say you don't know.
{context}
"""

review_system_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(input_variables=["context"], template=review_template)
)

review_human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(input_variables=["question"], template="{question}")
)

messages = [review_system_prompt, review_human_prompt]

review_prompt = ChatPromptTemplate(
    input_variables=["context", "question"], messages=messages
)

reviews_vector_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model=os.getenv("HOSPITAL_QA_MODEL"), temperature=0),
    chain_type="stuff",
    retriever=neo4j_vector_index.as_retriever(k=12),
)

reviews_vector_chain.combine_documents_chain.llm_chain.prompt = review_prompt
