from pydantic import BaseModel, Field
from typing import Optional

# untuk validasi
class Update_employee_request(BaseModel):
    name: str = Field(..., description='Employee name',min_length=3, max_length=50)
    age: Optional[int] = Field(None, description='Employee age')