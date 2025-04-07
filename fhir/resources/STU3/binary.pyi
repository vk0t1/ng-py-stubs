from . import fhirtypes as fhirtypes
from . import resource as resource

class Binary(resource.Resource):
    __resource_type__: str
    content: fhirtypes.Base64BinaryType | None
    content__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contentType: fhirtypes.CodeType | None
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    securityContext: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
