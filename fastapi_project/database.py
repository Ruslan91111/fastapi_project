"""Configuration of connection to database - MongoDB and
operations CRUD with movies in Database."""

import motor.motor_asyncio
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.movies

movie_collection = database.get_collection("movies_collections")


def movie_helper(movie) -> dict:
    """Put data from db into the desired form, for the convenience of work."""
    return {
        "id": str(movie['_id']),
        "title": movie["title"],
        "synopsis": movie["synopsis"],
        "year": movie["year"],
    }


async def retrieve_all_movies_from_db():
    """Retrieve all movies present in th database."""
    movies = []
    async for movie in movie_collection.find():
        movies.append(movie_helper(movie))
    return movies


async def add_movie_to_db(movie_data: dict) -> dict:
    """Add new movie into the database"""
    movie = await movie_collection.insert_one(movie_data)
    new_movie = await movie_collection.find_one({"_id": movie.inserted_id})
    return movie_helper(new_movie)


async def retrieve_movie_by_id(movie_id: str) -> dict:
    """Retrieve a movie by matching id"""
    movie = await movie_collection.find_one({"_id": ObjectId(movie_id)})
    if movie:
        return movie_helper(movie)


async def update_movie_in_db(movie_id: str, movie_data: dict) -> bool:
    """Update a movie with matching id."""
    if len(movie_data) < 1:
        return False
    movie = movie_collection.find({"_id": ObjectId(movie_id)})
    if movie:
        updated_movie = movie_collection.update_one(
            {"_id": ObjectId(movie_id)}, {"$set": movie_data}
        )
        if updated_movie:
            return True
        return False


async def delete_movie_in_db(movie_id: str) -> bool:
    """Delete the movie from database by id."""
    movie = movie_collection.find_one({"_id": ObjectId(movie_id)})
    if movie:
        await movie_collection.delete_one({"_id": ObjectId(movie_id)})
        return True
