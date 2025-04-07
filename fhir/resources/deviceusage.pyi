from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DeviceUsage(domainresource.DomainResource):
    __resource_type__: str
    adherence: fhirtypes.DeviceUsageAdherenceType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    bodySite: fhirtypes.CodeableReferenceType | None
    category: list[fhirtypes.CodeableConceptType] | None
    context: fhirtypes.ReferenceType | None
    dateAsserted: fhirtypes.DateTimeType | None
    dateAsserted__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    derivedFrom: list[fhirtypes.ReferenceType] | None
    device: fhirtypes.CodeableReferenceType
    identifier: list[fhirtypes.IdentifierType] | None
    informationSource: fhirtypes.ReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    patient: fhirtypes.ReferenceType
    reason: list[fhirtypes.CodeableReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingDateTime: fhirtypes.DateTimeType | None
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingPeriod: fhirtypes.PeriodType | None
    timingTiming: fhirtypes.TimingType | None
    usageReason: list[fhirtypes.CodeableConceptType] | None
    usageStatus: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DeviceUsageAdherence(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    reason: list[fhirtypes.CodeableConceptType]
    @classmethod
    def elements_sequence(cls): ...
