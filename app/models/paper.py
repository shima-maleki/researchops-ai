from pydantic import BaseModel


class Paper(BaseModel):
    title: str
    summary: str
    link: str
    category: str