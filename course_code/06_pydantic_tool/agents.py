from pydantic_ai import Agent
from model import nividia_model

weather_agent = Agent(
    model=nividia_model(),
    instructions=(
        "You are a helpful weather assistant, and always answer "
        "short and concise. Never add more text than neccessary."
        " use the available tools whenever possible. When there "
        " are questions that are not about weather, decline them"
    ),
    
)