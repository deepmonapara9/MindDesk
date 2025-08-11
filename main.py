from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# This will import the model from Ollama
# and create a chat prompt template for answering questions about a pizza restaurant
# using the reviews provided.
model = OllamaLLM(model="llama3.2:1b")

template = """
You are an expert in answering questions about a pizza restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

# Create a chat prompt template with the given template
prompt = ChatPromptTemplate.from_template(template)

# This will create a chain that takes in reviews and a question, and outputs an answer
chain = prompt | model

while True:
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question == "q":
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)
