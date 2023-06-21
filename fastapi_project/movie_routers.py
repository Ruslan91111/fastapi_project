"""CRUD Routes for operations with movies in Database"""
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from .database import (add_movie_to_db, retrieve_movie_by_id,
                                                      retrieve_all_movies_from_db, update_movie_in_db,
                                                      delete_movie_in_db)
from .models.movie_model import (successful_response, error_response,
                                                                MovieSchema, UpdateMovieModel)

router = APIRouter()


@router.post("/", response_description="Movie data added into database")
async def add_movie_data(movie: MovieSchema = Body(...)):
    """Create a new movie"""
    movie = jsonable_encoder(movie)
    new_movie = await add_movie_to_db(movie)
    return successful_response(new_movie, "Movie added successfully.")
