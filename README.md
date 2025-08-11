# 🍕 Local AI Restaurant Review Chatbot 🤖

A local AI-powered chatbot that answers questions about a pizza restaurant using customer reviews and vector similarity search. The system uses Ollama for language models and embeddings, LangChain for orchestration, and ChromaDB for vector storage.

## ✨ Features

- **🤔 Question Answering**: Ask natural language questions about the restaurant
- **🔍 Vector Search**: Uses semantic similarity to find relevant reviews
- **🏠 Local AI**: Runs entirely locally using Ollama models
- **💾 Persistent Storage**: Vector database persists between sessions
- **💻 Interactive CLI**: Simple command-line interface for queries

## 🏗️ Architecture

The project consists of two main components:

### 1. 🗃️ Vector Database Setup (`vector.py`)
- 📊 Loads restaurant reviews from CSV file
- 🧠 Creates vector embeddings using Ollama's `mxbai-embed-large` model
- 💾 Stores embeddings in ChromaDB for fast similarity search
- 🔄 Provides a retriever interface for finding relevant reviews

### 2. 💬 Chat Interface (`main.py`)
- 🦙 Uses Ollama's `llama3.2:1b` model for question answering
- 🔍 Retrieves relevant reviews based on user questions
- 📝 Combines reviews with questions using a prompt template
- 🖥️ Provides interactive CLI for continuous questioning

## 📋 Prerequisites

1. **🦙 Ollama Installation**: Install Ollama from [ollama.ai](https://ollama.ai)
2. **🤖 Required Models**: Pull the necessary models:
   ```bash
   ollama pull llama3.2:1b
   ollama pull mxbai-embed-large
   ```

## ⚙️ Installation

1. **📥 Clone or download this repository**

2. **🐍 Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **📄 Ensure you have the restaurant reviews data**:
   - The project includes `realistic_restaurant_reviews.csv` with sample restaurant reviews
   - Each review contains: Title, Date, Rating (1-5), and Review text

## 🚀 Usage

### 🆕 First Run
On the first run, the system will:
- 📖 Read all reviews from the CSV file
- 🧠 Generate vector embeddings for each review
- 💾 Store them in the ChromaDB database (`chroma_langchain_db/`)

### 🏃‍♂️ Running the Chatbot
```bash
python main.py
```

### 💡 Example Interactions
```
Ask your question (q to quit): What do customers say about the pizza crust? 🍕

Ask your question (q to quit): Are there any complaints about delivery? 🚚

Ask your question (q to quit): What's the most expensive item mentioned? 💰

Ask your question (q to quit): q
```

## 📁 Project Structure

```
Local AI Agent/
├── 🐍 main.py                          # Main chat interface
├── 🔍 vector.py                        # Vector database setup and retriever
├── 📋 requirements.txt                 # Python dependencies
├── 📄 realistic_restaurant_reviews.csv # Restaurant review data
├── 📖 README.md                        # This file
└── 🗃️ chroma_langchain_db/            # ChromaDB vector database (auto-generated)
    ├── 💾 chroma.sqlite3
    └── 📂 b686ea07-51e6-47e4-aba5-25fadda50e30/
        ├── 📊 data_level0.bin
        ├── 📋 header.bin
        ├── 📏 length.bin
        └── 🔗 link_lists.bin
```

## ⚡ How It Works

1. **📊 Data Loading**: Reviews are loaded from the CSV file with metadata (rating, date)
2. **🧠 Embedding Generation**: Each review is converted to a vector using Ollama embeddings
3. **💾 Vector Storage**: Embeddings are stored in ChromaDB for fast retrieval
4. **🔍 Query Processing**: User questions are embedded and matched against stored reviews
5. **🎯 Context Retrieval**: Top 5 most relevant reviews are retrieved
6. **💬 Answer Generation**: The language model generates answers using the relevant reviews as context

## 📦 Dependencies

- **🔗 langchain**: Framework for building LLM applications
- **🦙 langchain-ollama**: Ollama integration for LangChain
- **🗃️ langchain-chroma**: ChromaDB integration for LangChain
- **🐼 pandas**: Data manipulation for CSV processing

## ⚙️ Configuration

### 🔄 Changing Models
To use different Ollama models, modify the model names in:
- `main.py`: Change `llama3.2:1b` to your preferred language model
- `vector.py`: Change `mxbai-embed-large` to your preferred embedding model

### 🎛️ Adjusting Retrieval
To change the number of reviews retrieved per query, modify the `k` parameter in `vector.py`:
```python
retriever = vector_store.as_retriever(search_kwargs={"k": 5})  # Change 5 to desired number
```

### 📊 Custom Data
Replace `realistic_restaurant_reviews.csv` with your own data. Ensure the CSV has columns:
- `Title`: Review title
- `Date`: Review date  
- `Rating`: Numerical rating
- `Review`: Review text content

## ⚡ Performance Notes

- ⏱️ First run will be slower due to embedding generation
- 🚀 Subsequent runs use the persisted vector database
- 🏃‍♂️ Query response time depends on the Ollama model speed
- 💨 The `llama3.2:1b` model is chosen for fast local inference

## 🔧 Troubleshooting

1. **🔌 Ollama Connection Issues**: Ensure Ollama is running (`ollama serve`)
2. **🤖 Model Not Found**: Pull required models using `ollama pull <model-name>`
3. **💾 Memory Issues**: Consider using smaller models if you have limited RAM
4. **🗃️ Database Issues**: Delete `chroma_langchain_db/` folder to rebuild the vector database
