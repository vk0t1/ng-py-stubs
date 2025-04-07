from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ImmunizationEvaluation(domainresource.DomainResource):
    __resource_type__: str
    authority: fhirtypes.ReferenceType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    doseNumber: fhirtypes.StringType | None
    doseNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    doseStatus: fhirtypes.CodeableConceptType
    doseStatusReason: list[fhirtypes.CodeableConceptType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    immunizationEvent: fhirtypes.ReferenceType
    patient: fhirtypes.ReferenceType
    series: fhirtypes.StringType | None
    series__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    seriesDoses: fhirtypes.StringType | None
    seriesDoses__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetDisease: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
