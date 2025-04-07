from . import element as element

class DataType(element.Element):
    __resource_type__: str
    @classmethod
    def elements_sequence(cls): ...
