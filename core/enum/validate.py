from enum import Enum

class Validate(Enum):
    NameAutoPark = (
        r'^[A-Z][a-z]{2,30}$',
        'Name Auto Park must be only litters and min 3 char max 30 char '
    )
    BrandCar = (
        r'^[a-zA-Z0-9]{3,20}$',
        'Brand Car must be min 3 char max 30 char '
    )
    NameUser = (
        r'^[A-Z][a-z]{2,20}$',
        'Name User must be only litters and min 3 char max 30 char '
    )
    def __init__(self, pattern, message):
        self.pattern = pattern
        self.message = message