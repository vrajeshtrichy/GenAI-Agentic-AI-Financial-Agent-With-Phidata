# Stock Analyst Assistant AI

An **Agentic AI-powered** chatbot designed to assist stock analysts by providing real-time stock market insights, financial data, and news. This application is built using `FastAPI` for backend processing and deployed as a `Streamlit` chatbot.

## Features
- Fetches real-time stock market data using `yfinance`
- Provides financial news via `duckduckgo-search`
- Supports AI-powered analysis with `groq` using llama-3.3-70b-versatile
- Interactive chatbot interface using `Streamlit`
- Scalable and fast backend with `FastAPI` & `uvicorn`
- Built using Phidata for agent development

## Tech Stack
- **Backend**: FastAPI, Uvicorn
- **Frontend**: Streamlit
- **AI Engine**: Groq (using llama-3.3-70b-versatile)
- **Data Sources**: yFinance, DuckDuckGo Search
- **Agent Framework**: Phidata
- **Environment Management**: python-dotenv

## Installation

### Clone the Repository
```bash
git clone https://github.com/vrajeshtrichy/GenAI-Agentic-AI-Financial-Agent-With-Phidata.git
cd GenAI-Agentic-AI-Financial-Agent-With-Phidata
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a `.env` file in the project root and add:
```env
PHI_API_KEY = your_api_key
```
```env
GROQ_API_KEY = your_api_key
```

### Start the Streamlit Frontend
```bash
streamlit run llm_bot.py
```

## Usage
- Enter a stock ticker (e.g., `AAPL`) in the chatbot.
- Get real-time stock prices, financial data, and news.
- Use AI-generated insights for investment decisions.

