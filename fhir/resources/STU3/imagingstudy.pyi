from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ImagingStudy(domainresource.DomainResource):
    __resource_type__: str
    accession: fhirtypes.IdentifierType | None
    availability: fhirtypes.CodeType | None
    availability__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    context: fhirtypes.ReferenceType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    endpoint: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    interpreter: list[fhirtypes.ReferenceType] | None
    modalityList: list[fhirtypes.CodingType] | None
    numberOfInstances: fhirtypes.UnsignedIntType | None
    numberOfInstances__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    numberOfSeries: fhirtypes.UnsignedIntType | None
    numberOfSeries__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patient: fhirtypes.ReferenceType
    procedureCode: list[fhirtypes.CodeableConceptType] | None
    procedureReference: list[fhirtypes.ReferenceType] | None
    reason: fhirtypes.CodeableConceptType | None
    referrer: fhirtypes.ReferenceType | None
    series: list[fhirtypes.ImagingStudySeriesType] | None
    started: fhirtypes.DateTimeType | None
    started__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uid: fhirtypes.OidType | None
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImagingStudySeries(backboneelement.BackboneElement):
    __resource_type__: str
    availability: fhirtypes.CodeType | None
    availability__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    bodySite: fhirtypes.CodingType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    endpoint: list[fhirtypes.ReferenceType] | None
    instance: list[fhirtypes.ImagingStudySeriesInstanceType] | None
    laterality: fhirtypes.CodingType | None
    modality: fhirtypes.CodingType
    number: fhirtypes.UnsignedIntType | None
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    numberOfInstances: fhirtypes.UnsignedIntType | None
    numberOfInstances__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    performer: list[fhirtypes.ReferenceType] | None
    started: fhirtypes.DateTimeType | None
    started__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uid: fhirtypes.OidType | None
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    __resource_type__: str
    number: fhirtypes.UnsignedIntType | None
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sopClass: fhirtypes.OidType | None
    sopClass__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uid: fhirtypes.OidType | None
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
