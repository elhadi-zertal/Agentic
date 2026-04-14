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
    
    instructions=[
        "Display data using markdown tables",
        "Only include the markdown table in your response, do not include any other text",
    ],

    tools=[YFinanceTools()],
)

agent.print_response("What are the stock prices of NVIDIA and AMD?", stream=True)

