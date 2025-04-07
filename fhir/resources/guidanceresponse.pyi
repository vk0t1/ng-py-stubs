from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class GuidanceResponse(domainresource.DomainResource):
    __resource_type__: str
    dataRequirement: list[fhirtypes.DataRequirementType] | None
    encounter: fhirtypes.ReferenceType | None
    evaluationMessage: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    moduleCanonical: fhirtypes.CanonicalType | None
    moduleCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    moduleCodeableConcept: fhirtypes.CodeableConceptType | None
    moduleUri: fhirtypes.UriType | None
    moduleUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    outputParameters: fhirtypes.ReferenceType | None
    performer: fhirtypes.ReferenceType | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    requestIdentifier: fhirtypes.IdentifierType | None
    result: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
