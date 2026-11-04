from agents import movie_agent
from fastapi import FastAPI
from pydantic import BaseModel
from setup_db import query_duckdb

app = FastAPI()


class Question(BaseModel):
    question: str


@app.get("/movies")
async def read_movies():
    movies = query_duckdb("FROM movies;")
    return movies.to_dict(orient="records")


@app.post("/movies")
async def create_movie(body: Question):
    result = await movie_agent.run(body.question)
    movie = result.output

    query_duckdb(
        "INSERT INTO movies VALUES(?, ?, ?, ?, ?)",
        parameters=[movie.title, movie.year, movie.genre, movie.rating, movie.summary],
    )
    return movie