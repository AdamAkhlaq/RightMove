from typing import Optional
from httpx import AsyncClient
from models.property import Property
from scrapers.extractor import extract_property
from parsers.property_parser import parse_property


async def scrape_property(url: str, client: AsyncClient) -> Optional[Property]:
    """Scrape a single Rightmove property listing"""
    response = await client.get(url)
    extracted = extract_property(response)
    if extracted:
        return parse_property(extracted)
    return None
