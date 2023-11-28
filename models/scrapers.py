from typing import Optional
from pydantic import BaseModel, field_validator, Field, field_serializer

from enum import Enum, auto

from commons.openai import Calification


class Opinion(BaseModel):
    author: str
    text: str
    date: str
    calification: Optional[Calification] | None = Field(None)

    @field_serializer("calification", return_type=str, when_used="unless-none")
    def serialize_calification(self, v: Calification, _info) -> str:
        if v:
            return v.name.capitalize()


class Order(Enum):
    ASC = auto()
    DESC = auto()


class SendScraping(BaseModel):
    order: str

    @field_validator("order")
    def validate_order(cls, v):
        if v.upper() not in ["ASC", "DESC"]:
            raise ValueError("order must be asc or desc")
        return v.upper()
