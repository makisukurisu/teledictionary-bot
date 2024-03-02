import pydantic

from teledictionary_bot.enums import ProviderNames
from teledictionary_bot.models.base import BaseModel


class Dictionary(BaseModel):
    name: str
    description: str = pydantic.Field(default="")
    provider_name: ProviderNames

    def as_string(self: "Dictionary") -> str:
        return f"{self.name}\n\n{self.description}"
