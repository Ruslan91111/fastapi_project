"""Model of movie  """

from typing import Optional
from pydantic import BaseModel, Field


class MovieSchema(BaseModel):
    title: str = Field(...)
    synopsis: str = Field(...)
    year: int = Field(..., gt=1895, le=2030)

    class Config:
        schema_extra = {
            "example": {
                "title": "Fight Club",
                "synopsis": "An insomniac office worker and a devil-may-care soap maker form an underground fight club "
                            "that evolves into much more. ",
                "year": 1999,
            }
        }


class UpdateMovieModel(BaseModel):
    title: Optional[str]
    synopsis: Optional[str]
    year: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "title": "Fight Club",
                "synopsis": "An insomniac office worker and a devil-may-care soap maker form an underground fight club "
                            "that evolves into much more. ",
                "year": 1999,
            }
        }


def successful_response(data, message):
    """Response for successful action"""
    return {
        "data": [data],
        "code": 200,
        "message": message
    }


def error_response(error, code, message):
    """Response for unsuccessful action"""
    return {"error": error, "code": code, "message": message}
