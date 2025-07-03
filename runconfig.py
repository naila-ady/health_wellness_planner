from agents import AsyncOpenAI, OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv, find_dotenv
from agents.run import RunConfig

load_dotenv(find_dotenv())


gemini_api_key =os.getenv("GEMINI_API_KEY")

provider=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model=OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client= provider
)

config=RunConfig(
    model= model,
    model_provider=provider,
    tracing_disabled= True,
)

