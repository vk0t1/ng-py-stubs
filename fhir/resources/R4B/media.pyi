from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Media(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    bodySite: fhirtypes.CodeableConceptType | None
    content: fhirtypes.AttachmentType
    createdDateTime: fhirtypes.DateTimeType | None
    createdDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    createdPeriod: fhirtypes.PeriodType | None
    device: fhirtypes.ReferenceType | None
    deviceName: fhirtypes.StringType | None
    deviceName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    duration: fhirtypes.DecimalType | None
    duration__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    frames: fhirtypes.PositiveIntType | None
    frames__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    height: fhirtypes.PositiveIntType | None
    height__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    issued: fhirtypes.InstantType | None
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modality: fhirtypes.CodeableConceptType | None
    note: list[fhirtypes.AnnotationType] | None
    operator: fhirtypes.ReferenceType | None
    partOf: list[fhirtypes.ReferenceType] | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    view: fhirtypes.CodeableConceptType | None
    width: fhirtypes.PositiveIntType | None
    width__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
