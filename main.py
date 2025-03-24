import asyncio
import json
from pathlib import Path
from scrapers.client import create_client
from scrapers.scraper import scrape_property
from config import PROPERTY_URL

OUTPUT_DIR = Path("property_data")
OUTPUT_DIR.mkdir(exist_ok=True)


async def run():
    client = create_client()
    try:
        property = await scrape_property(PROPERTY_URL, client)
        if property:
            filename = OUTPUT_DIR / f"property_{property.id}.json"

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(property.to_dict(), f, indent=2, ensure_ascii=False)

            print(f"✅ Successfully saved property data to {filename}")
        else:
            print("❌ Failed to scrape property")
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
    finally:
        await client.aclose()

if __name__ == "__main__":
    asyncio.run(run())
