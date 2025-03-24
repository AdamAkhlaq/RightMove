from httpx import Response
from parsel import Selector
import json
from typing import Optional, Dict


def find_json_objects(text: str, decoder=json.JSONDecoder()):
    """Find JSON objects in text"""
    pos = 0
    while True:
        match = text.find("{", pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            yield result
            pos = match + index
        except ValueError:
            pos = match + 1


def extract_property(response: Response) -> Optional[Dict]:
    """Extract property data from both PAGE_MODEL and adInfo"""
    selector = Selector(response.text)
    property_data = {}

    scripts = selector.xpath(
        "//script[contains(.,'PAGE_MODEL = ')]/text()").get()
    if scripts:
        for json_data in find_json_objects(scripts):
            if "propertyData" in json_data:
                property_data.update(json_data["propertyData"])

    return property_data if property_data else None
