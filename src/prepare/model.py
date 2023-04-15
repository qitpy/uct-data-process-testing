from pydantic import BaseModel


# TODO: define job fields
class Job(BaseModel):
    about: str | None = None
    requirement: str | None = None
    responsibilities: str | None = None
    benefit: str | None = None
    compensation: str | None = None