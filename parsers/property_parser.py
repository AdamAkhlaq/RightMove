from typing import Dict, Any, List, Optional, Tuple
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


def get_property_size(sizings_data: List[Dict[str, Any]]) -> Tuple[Optional[int], Optional[int]]:
    """
    Extract square meters and square feet sizes from sizings data
    Returns: Tuple of (size_sqm, size_sqft)
    """
    size_sqm = None
    size_sqft = None

    for sizing in sizings_data:
        unit = sizing.get("unit")
        min_size = sizing.get("minimumSize")

        if not unit or min_size is None:
            continue

        if unit == "sqm":
            size_sqm = int(min_size)
        elif unit == "sqft":
            size_sqft = int(min_size)

        # Early exit if we've found both sizes
        if size_sqm is not None and size_sqft is not None:
            break

    return size_sqm, size_sqft


def parse_property(data: Dict) -> Property:
    """Parse raw property data"""
    size_sqm, size_sqft = get_property_size(get_nested(data, "sizings", []))

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
        location={
            "latitude": get_nested(data, "location.latitude"),
            "longitude": get_nested(data, "location.longitude")
        },
        listing_history=get_nested(data, "listingHistory", []),
        tags=get_nested(data, "tags", []),
        council_tax_band=get_nested(data, "livingCosts.councilTaxBand"),
        epc_graphs=[{"url": p["url"], "caption": p.get("caption")}
                    for p in get_nested(data, "epcGraphs", [])],
        tenure=get_nested(data, "tenure.tenureType"),
        size_sqm=size_sqm,
        size_sqft=size_sqft
    )
