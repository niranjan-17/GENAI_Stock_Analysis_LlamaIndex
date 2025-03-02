# 📊 Financial Stock Analysis using LlamaIndex

## 📌 Overview
This project leverages **LlamaIndex** to build a **GPT-powered vector store index** for analyzing stock-related articles. It integrates **OpenAI's GPT API** to create an index from documents stored in the `articles` directory, enabling efficient retrieval and analysis.

## 🚀 Features
- **Automated Document Parsing:** Reads and indexes stock analysis articles.
- **OpenAI GPT Integration:** Uses OpenAI's API for intelligent stock insights.
- **Vector Store Indexing:** Stores data for fast and efficient querying.
- **Persistent Storage:** Saves indexed data for future use.
- **Streamlit Dashboard:** Interactive UI for financial analysis.

## 🛠️ Technology Used
- **LlamaIndex**
- **OpenAI GPT-4**
- **Streamlit**

📌 **Note:** Use Python version **3.8 or later**.

## 📂 Project Structure
```
GENAI_Stock_Analysis_LlamaIndex/
│-- .env                        # Environment variables (API keys, etc.)
│-- articles/                    # Directory for input documents
│-- storage/                     # Indexed data storage
│-- src/
│   │-- fetch_data.py           # Script to fetch and extract articles
│   │-- generate_index.py       # Script to create the vector store index
│-- requirements.txt             # Required Python packages
│-- README.md                    # Documentation
│-- app.py                       # Streamlit application
│-- Dockerfile                   # Docker container configuration
```

## 🚀 How to Run?
### 1️⃣ Clone the Repository
```bash
git clone "repository"
cd GENAI_Stock_Analysis_LlamaIndex
```

### 2️⃣ Create a Conda Environment
```bash
conda create -n finance python=3.8 -y
conda activate finance
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Download and Extract Articles
```python
import os
import urllib.request as request
import zipfile

data_url = "https://github.com/entbappy/Branching-tutorial/raw/master/articles.zip"

def download_and_extract():
    zip_path = "articles.zip"
    request.urlretrieve(url=data_url, filename=zip_path)
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall("articles")
    os.remove(zip_path)

download_and_extract()
```

### 5️⃣ Run the Streamlit Application
```bash
streamlit run app.py
```
Now, open **http://localhost:8501** in your browser.

## 📦 Running with Docker
### 1️⃣ Build the Docker Image
```bash
docker build -t llamaindex-stock-analysis .
```

### 2️⃣ Run the Docker Container
```bash
docker run -p 8501:8501 --env-file .env llamaindex-stock-analysis
```
Now, access the app at **http://localhost:8501**.

## 📈 Stock Symbols Used
```python
symbols = ['MSFT', 'NVDA', 'GOOG', 'META', 'AAPL', 'TSM']
```

## 🔍 Troubleshooting
### ⚠️ "unzip is not recognized as an internal or external command"
✅ Fix: Use `zipfile` for extraction instead of `unzip` (already handled in the script).

### ⚠️ "OPENAI_API_KEY is None"
✅ Fix: Ensure your `.env` file exists and contains the correct API key. Restart your terminal if needed.

## 🏆 Acknowledgments
- [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/) for efficient document indexing.
- [OpenAI](https://openai.com) for GPT-powered insights.



