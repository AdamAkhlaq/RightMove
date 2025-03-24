from config import PROPERTY_URL
from scrapers.rightmove_scraper import get_rightmove_data

if __name__ == "__main__":
    print(get_rightmove_data(PROPERTY_URL))
