from typing import List

from pydantic import BaseModel


class CalculationRequest(BaseModel):
    expression: List[str]


class CalculationResponse(BaseModel):
    expression: List[str]
    result: float
