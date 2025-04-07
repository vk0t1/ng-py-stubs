from . import datatype as datatype
from . import fhirtypes as fhirtypes

class Annotation(datatype.DataType):
    __resource_type__: str
    authorReference: fhirtypes.ReferenceType | None
    authorString: fhirtypes.StringType | None
    authorString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    text: fhirtypes.MarkdownType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    time: fhirtypes.DateTimeType | None
    time__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
