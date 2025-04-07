from . import datatype as datatype

class PrimitiveType(datatype.DataType):
    __resource_type__: str
    @classmethod
    def elements_sequence(cls): ...
