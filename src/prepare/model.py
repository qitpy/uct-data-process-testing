from pydantic import BaseModel


# TODO: define job fields
class Job(BaseModel):
    about: str | None = None
    minimum_requirement: str | None = None
    preferred_requirement: str | None = None
    responsibilities: str | None = None
    compensation: str | None = None