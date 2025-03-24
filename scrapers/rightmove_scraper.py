import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept-Language": "en-GB,en;q=0.9",
    "Referer": "https://www.rightmove.co.uk/",
}


def get_rightmove_data(PROPERTY_URL):
    """Scrape a Rightmove property page"""
    page = requests.get(PROPERTY_URL, headers=HEADERS)
    return page.text
