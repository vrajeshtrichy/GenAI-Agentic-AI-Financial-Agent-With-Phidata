from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

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

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Apple", stream = True)
