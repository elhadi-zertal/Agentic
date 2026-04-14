import os
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.yfinance import YFinanceTools
from agno.tools.reasoning import ReasoningTools

load_dotenv()

agent = Agent(
    model=Groq(
        id="llama-3.1-8b-instant",
        api_key=os.environ['GROQ_API_KEY']
    ),
    
    instructions=[
        "Include sources in your response",
    ],

    tools=[
        ReasoningTools(),
        YFinanceTools()
    ],
)

agent.print_response(
    "Write a report on AMD?",
    show_full_reasoning=True,
    stream_intermediate_steps=True,
)

