from . import quantity as quantity

class Duration(quantity.Quantity):
    __resource_type__: str
    @classmethod
    def elements_sequence(cls): ...
