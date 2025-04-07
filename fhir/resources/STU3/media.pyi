from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Media(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    bodySite: fhirtypes.CodeableConceptType | None
    content: fhirtypes.AttachmentType
    context: fhirtypes.ReferenceType | None
    device: fhirtypes.ReferenceType | None
    duration: fhirtypes.UnsignedIntType | None
    duration__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    frames: fhirtypes.PositiveIntType | None
    frames__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    height: fhirtypes.PositiveIntType | None
    height__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    operator: fhirtypes.ReferenceType | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    subject: fhirtypes.ReferenceType | None
    subtype: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    view: fhirtypes.CodeableConceptType | None
    width: fhirtypes.PositiveIntType | None
    width__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
