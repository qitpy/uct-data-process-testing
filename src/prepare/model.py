from pydantic import BaseModel


# TODO: define job fields
class Job(BaseModel):
    requirement: str
    responsibilities: str