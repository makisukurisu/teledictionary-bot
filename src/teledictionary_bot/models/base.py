import pydantic


class BaseModel(pydantic.BaseModel):
    id: int = 0
