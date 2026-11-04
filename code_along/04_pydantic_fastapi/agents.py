from pydantic_ai import Agent
from model import nividia_model

movie_agent = Agent(
    model=nividia_model(),
    instructions="you are an expert in finding a movie based on a text"
)


# To test an agent in python script use run_sync
movie = movie_agent.run_sync("Ill be back")
print(movie)
