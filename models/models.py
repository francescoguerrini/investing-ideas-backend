# models.py (nuovo file per definire i modelli)

from pydantic import BaseModel # type: ignore
from typing import List, Optional

class Idea(BaseModel):
    name: str
    stock_name: str
    price: float
    one_year_variation: str
    chart_url: str
    last_year: float
    dividends: Optional[float]
    dividend_yield: str

class IdeaResponse(BaseModel):
    category: str
    ideas: List[Idea]
