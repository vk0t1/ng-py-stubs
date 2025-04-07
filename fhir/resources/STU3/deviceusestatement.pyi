from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DeviceUseStatement(domainresource.DomainResource):
    __resource_type__: str
    bodySite: fhirtypes.CodeableConceptType | None
    device: fhirtypes.ReferenceType
    identifier: list[fhirtypes.IdentifierType] | None
    indication: list[fhirtypes.CodeableConceptType] | None
    note: list[fhirtypes.AnnotationType] | None
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
    whenUsed: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
