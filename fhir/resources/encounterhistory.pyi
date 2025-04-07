from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class EncounterHistory(domainresource.DomainResource):
    __resource_type__: str
    actualPeriod: fhirtypes.PeriodType | None
    class_fhir: fhirtypes.CodeableConceptType
    encounter: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    length: fhirtypes.DurationType | None
    location: list[fhirtypes.EncounterHistoryLocationType] | None
    plannedEndDate: fhirtypes.DateTimeType | None
    plannedEndDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    plannedStartDate: fhirtypes.DateTimeType | None
    plannedStartDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    serviceType: list[fhirtypes.CodeableReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    subjectStatus: fhirtypes.CodeableConceptType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class EncounterHistoryLocation(backboneelement.BackboneElement):
    __resource_type__: str
    form: fhirtypes.CodeableConceptType | None
    location: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
