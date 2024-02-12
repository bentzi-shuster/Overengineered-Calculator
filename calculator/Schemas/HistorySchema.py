from typing import List, Optional
from pydantic import BaseModel
from decimal import Decimal  

class OperationResult(BaseModel):
    operation: str
    args: List[Decimal]
    start: float
    end: Optional[float]
    result: Optional[Decimal]
    error: Optional[str]

class CalculationHistory(BaseModel):
    calculations: List[OperationResult]

    