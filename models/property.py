from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any, List


@dataclass
class Property:
    """Model for property data with comprehensive fields"""
    id: int
    price: Optional[str]
    price_value: Optional[float]
    bedrooms: Optional[int]
    bathrooms: Optional[int]
    property_type: Optional[str]
    property_sub_type: Optional[str]
    transaction_type: Optional[str]
    address: Optional[Dict[str, Any]]
    description: Optional[str]
    features: Optional[List[str]]
    photos: Optional[List[Dict[str, str]]]
    floorplans: Optional[List[Dict[str, str]]]
    location: Optional[Dict[str, float]]
    listing_history: Optional[List[Dict[str, Any]]]
    tags: Optional[List[str]]
    council_tax_band: Optional[str]
    epc_graphs: Optional[List[Dict[str, str]]]

    def to_dict(self):
        """Convert to dictionary with all fields"""
        return asdict(self)

    def is_within_budget(self, max_budget: float) -> bool:
        """Check if property is within budget"""
        return self.price_value <= max_budget if self.price_value else False
