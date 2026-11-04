from pydantic import BaseModel, Field
from typing import Literal

class Movie(BaseModel):
    title: str = Field(description="Title of the movie")
    year: int = Field(description="Year when the movie came out")
    genre: Literal["Action", "Comedy", "Romance", "War", "Cartoon", "Adventure", "Horror"] = Field(
        description="main genre, if there is more than one, choose the one thats is most characeristic"
    )
    rating: int = Field(description=("give a rating between 1 and 10,"
                         "the higher the more popular the movie is"),
                         ge=1, le=10)
    summary: str = Field(description="short exciting summary of the movie, max 3 sentences")