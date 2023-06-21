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


@router.get("/", response_description="All movies retrieved.")
async def get_all_movies():
    """Get all movies from DB"""
    movies = await retrieve_all_movies_from_db()
    if movies:
        successful_response(movies, "Movies data retrieved successfully")
    return successful_response(movies, "Empty list returned")


@router.get("/{id}", response_description="The movie retrieved.")
async def get_the_movie(movie_id: str):
    """Get a sertain movie from database"""
    movie = await retrieve_movie_by_id(movie_id)
    if movie:
        return successful_response(movie, "The movie retrieved successfully")
    return error_response("An error occurred.", 404, "Movie doesn't exist.")


@router.put("/{id}")
async def update_movie_data(movie_id: str, requisites: UpdateMovieModel = Body(...)):
    """Update data about the movie in database."""
    requisites = {k: v for k, v in requisites.dict().items() if v is not None}
    updated_movie = await update_movie_in_db(movie_id, requisites)
    if updated_movie:
        return successful_response(
            f"Movie with ID: {movie_id} updated successfully",
            "Movie updated successfully",
        )
    return error_response(
        'An error occurred',
        404,
        "There was error updating the movie data."
    )


@router.delete("/{id}")
async def delete_movie_from_database(movie_id: str):
    """Delete movie from database."""
    deleted_movie = delete_movie_in_db(movie_id)
    if deleted_movie:
        return successful_response(
            f"Movie with ID: {movie_id} removed", "Movie deleted successfully"
        )
    return error_response(
        "An error occurred", 404, f"Movie with id {movie_id} doesn't exist"
    )
