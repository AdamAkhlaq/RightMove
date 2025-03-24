import json
from typing import Generator, Dict, Any


def find_json_objects(text: str, decoder=json.JSONDecoder()) -> Generator[Dict[str, Any], None, None]:
    """Find JSON objects in text, and generate decoded JSON data"""
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
