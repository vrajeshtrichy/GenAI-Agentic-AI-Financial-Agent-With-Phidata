from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import streamlit as st

# DuckDuckGo web search agent
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for the information",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tools_calls = True,
    markdown = True,
)

# Financial Agent
finance_agent = Agent(
name = "Finance AI Agent",
model = Groq(id = "llama-3.3-70b-versatile"),
tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
instructions = ["Use tables to display the data"],
show_tools_calls = True,
markdown = True,
)

#Multi Model Agent
multi_ai_agent = Agent(
team = [web_search_agent, finance_agent],
model=Groq(id="llama-3.3-70b-versatile"),
instructions = ["Always include sources", "Use tables to display the data"],
show_tools_calls = True,
markdown = True,
)

# multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Apple", stream = True)


with st.sidebar:
    phi_api_key = st.text_input("Phi API Key", key="phi_api_key", type="password")

st.title("💬 Stock Analyst")
st.caption("🚀 A Multi-Agentic AI chatbot powered by Llama")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    # if not phi_api_key:
    #     st.info("Please add your Phi API key to continue.")
    #     st.stop()

    # client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = multi_ai_agent.run(prompt, stream = False)
    print(response.content)
    msg = response.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)