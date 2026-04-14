import os
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.yfinance import YFinanceTools

load_dotenv()

agent = Agent(
    model=Groq(
        id="llama-3.1-8b-instant",
        api_key=os.environ['GROQ_API_KEY']
    ),
    tools=[YFinanceTools()],
)

agent.print_response("What is the stock price of Apple?", stream=True)

