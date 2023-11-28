from typing import Optional
from pydantic import BaseModel, Field

class SendOpinion(BaseModel):
    id: Optional[int] | None = Field(None, gt=0)
