

import asyncio
from fastapi import APIRouter, HTTPException
from typing import List
from .models import Idea, IdeaResponse
from services.fetcher import CATEGORY_MAP, fetch_top_ideas

router = APIRouter()

async def fetch_all_categories_sequentially():
    all_ideas = {}
    for category, tickers in CATEGORY_MAP.items():
        try:
            print(f"Fetching data for category: {category}")
            # Fetch ideas for the category
            ideas_data = await fetch_top_ideas(tickers)
            all_ideas[category] = ideas_data
        except Exception as e:
            print(f"Error fetching data for {category}: {str(e)}")
            all_ideas[category] = []
    return all_ideas

@router.get("/all-ideas")
async def get_all_ideas():
    """
    Fetch all ideas in categories sequentially and return.
    """
    # Fetch all categories one by one
    all_ideas = await fetch_all_categories_sequentially()
    
    return {"all_ideas": all_ideas}
