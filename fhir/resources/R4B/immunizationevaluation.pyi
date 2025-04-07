from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ImmunizationEvaluation(domainresource.DomainResource):
    __resource_type__: str
    authority: fhirtypes.ReferenceType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    doseNumberPositiveInt: fhirtypes.PositiveIntType | None
    doseNumberPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    doseNumberString: fhirtypes.StringType | None
    doseNumberString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    doseStatus: fhirtypes.CodeableConceptType
    doseStatusReason: list[fhirtypes.CodeableConceptType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    immunizationEvent: fhirtypes.ReferenceType
    patient: fhirtypes.ReferenceType
    series: fhirtypes.StringType | None
    series__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    seriesDosesPositiveInt: fhirtypes.PositiveIntType | None
    seriesDosesPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    seriesDosesString: fhirtypes.StringType | None
    seriesDosesString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetDisease: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
