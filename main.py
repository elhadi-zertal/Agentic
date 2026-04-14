import os
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
#from agno.tools.yfinance import YFinanceTools
#from agno.tools.reasoning import ReasoningTools


load_dotenv()

db = SqliteDb(db_file="tmp/agents.db")

agent = Agent(
    session_id=1,
    user_id="admin",
    model=Groq(
        id="llama-3.1-8b-instant",
        api_key=os.environ['GROQ_API_KEY']
    ),

    db=db,
    add_history_to_context=True,
    update_memory_on_run=True,
    
    #instructions=[
    #    "Include sources in your response",
    #],

    #tools=[
    #    ReasoningTools(),
    #    YFinanceTools()
    #],
)

#agent.print_response(
#    "Write a report on AMD?",
    #show_full_reasoning=True,
    #stream_intermediate_steps=True,
#)

agent.print_response("My name is el hadi")
agent.print_response("What is my name?")
