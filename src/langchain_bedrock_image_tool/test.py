import re

from IPython.display import Image
from langchain.agents import AgentType, initialize_agent
from langchain.llms import OpenAI
from langchain.tools import SteamshipImageGenerationTool
from steamship import Block, Steamship

llm = OpenAI(temperature=0)
tools = [SteamshipImageGenerationTool(model_name="stable-diffusion")]

mrkl = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

output = mrkl.run("How would you visualize a parot playing soccer?")

