from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class GuidanceResponse(domainresource.DomainResource):
    __resource_type__: str
    context: fhirtypes.ReferenceType | None
    dataRequirement: list[fhirtypes.DataRequirementType] | None
    evaluationMessage: list[fhirtypes.ReferenceType] | None
    identifier: fhirtypes.IdentifierType | None
    module: fhirtypes.ReferenceType
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    outputParameters: fhirtypes.ReferenceType | None
    performer: fhirtypes.ReferenceType | None
    reasonCodeableConcept: fhirtypes.CodeableConceptType | None
    reasonReference: fhirtypes.ReferenceType | None
    requestId: fhirtypes.IdType | None
    requestId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    result: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
