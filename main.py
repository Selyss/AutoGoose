from src.tiny_agent.tiny_agent import TinyAgent
from src.tiny_agent.config import get_tiny_agent_config
from dotenv import load_dotenv
import os

load_dotenv()

config_path = os.getenv("CONFIG")
tiny_agent_config = get_tiny_agent_config(config_path=config_path)
tiny_agent = TinyAgent(tiny_agent_config)


TinyAgent.arun(
    query="Create a meeting with Sid and Lutfi for tomorrow 2pm to discuss the meeting notes."
)
