from . import quantity as quantity

class Age(quantity.Quantity):
    __resource_type__: str
    @classmethod
    def elements_sequence(cls): ...
