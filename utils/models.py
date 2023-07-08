from enum import IntEnum

class ProductSizes(IntEnum):
  Small = 1
  medium = 2
  Large = 3
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]