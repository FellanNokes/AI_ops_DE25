from pydantic_ai import Agent
from model import nividia_model
from data_models import Movie

movie_agent = Agent(
    model=nividia_model(),
    instructions="you are an expert in finding a movie based on a text",
    output_type=Movie
)


# only runs when the script is runned directly
if __name__ == "__main__":
    # To test an agent in python script use run_sync
    movie = movie_agent.run_sync("Ill be back")
    print(movie)
