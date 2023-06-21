"""Main module, contains instance of application."""
import uvicorn
from fastapi import FastAPI

from .movie_routers import router as MovieRouter

app = FastAPI(
    title='MyApp'
)

app.include_router(MovieRouter, tags=["Movie"], prefix="/movie")


@app.get("/", tags=["Root"])
async def read_root():
    """Welcome page"""
    return {"message": "Welcome to my app"}


if __name__ == "__main__":
    uvicorn.run("fastapi_project.fastapi_project.app:app",
                host="0.0.0.0", port=8000, reload=True)
