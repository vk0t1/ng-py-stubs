from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DeviceUseStatement(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    bodySite: fhirtypes.CodeableConceptType | None
    derivedFrom: list[fhirtypes.ReferenceType] | None
    device: fhirtypes.ReferenceType
    identifier: list[fhirtypes.IdentifierType] | None
    note: list[fhirtypes.AnnotationType] | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    recordedOn: fhirtypes.DateTimeType | None
    recordedOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    source: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    timingDateTime: fhirtypes.DateTimeType | None
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingPeriod: fhirtypes.PeriodType | None
    timingTiming: fhirtypes.TimingType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
