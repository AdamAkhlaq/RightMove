from typing import Dict
from models.property import Property


def get_nested(data: Dict, path: str, default=None):
    """Access nested dictionary keys using dot notation"""
    keys = path.split('.')
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return default
    return data


def parse_property(data: Dict) -> Property:
    """Parse raw property data"""

    return Property(
        id=get_nested(data, "id"),
        price=get_nested(data, "prices.primaryPrice"),
        price_value=get_nested(data, "prices.amount"),
        bedrooms=get_nested(data, "bedrooms"),
        bathrooms=get_nested(data, "bathrooms"),
        property_type=get_nested(data, "propertyType"),
        property_sub_type=get_nested(data, "propertySubType"),
        transaction_type=get_nested(data, "transactionType"),
        address=get_nested(data, "address", {}),
        description=get_nested(data, "text.description"),
        features=get_nested(data, "keyFeatures", []),
        photos=[{"url": p["url"], "caption": p.get("caption")}
                for p in get_nested(data, "images", [])],
        floorplans=[{"url": p["url"], "caption": p.get("caption")}
                    for p in get_nested(data, "floorplans", [])],
        agency={
            "id": get_nested(data, "customer.branchId"),
            "branch": get_nested(data, "customer.branchName"),
            "company": get_nested(data, "customer.companyName"),
            "address": get_nested(data, "customer.displayAddress"),
        },
        location={
            "latitude": get_nested(data, "location.latitude"),
            "longitude": get_nested(data, "location.longitude")
        },
        listing_history=get_nested(data, "listingHistory", []),
        tags=get_nested(data, "tags", []),
        council_tax_band=get_nested(data, "livingCosts.councilTaxBand")
    )
