import pydantic

from teledictionary_bot.models.base import BaseModel


class Dictionary(BaseModel):
    name: str
    description: str = pydantic.Field(default="")

    def as_string(self: "Dictionary") -> str:
        return f"{self.name}\n\n{self.description}"
