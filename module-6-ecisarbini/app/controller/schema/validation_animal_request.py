from pydantic import BaseModel, Field
from typing import Optional

# untuk validasi
class Update_animal_request(BaseModel):
    name: str = Field(..., description='Animal name',min_length=3, max_length=50)
    birthdate: Optional[int] = Field(None, description='Animal birthdate')