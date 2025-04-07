from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ImagingStudy(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    endpoint: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: fhirtypes.ReferenceType | None
    modality: list[fhirtypes.CodeableConceptType] | None
    note: list[fhirtypes.AnnotationType] | None
    numberOfInstances: fhirtypes.UnsignedIntType | None
    numberOfInstances__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    numberOfSeries: fhirtypes.UnsignedIntType | None
    numberOfSeries__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    partOf: list[fhirtypes.ReferenceType] | None
    procedure: list[fhirtypes.CodeableReferenceType] | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    referrer: fhirtypes.ReferenceType | None
    series: list[fhirtypes.ImagingStudySeriesType] | None
    started: fhirtypes.DateTimeType | None
    started__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImagingStudySeries(backboneelement.BackboneElement):
    __resource_type__: str
    bodySite: fhirtypes.CodeableReferenceType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    endpoint: list[fhirtypes.ReferenceType] | None
    instance: list[fhirtypes.ImagingStudySeriesInstanceType] | None
    laterality: fhirtypes.CodeableConceptType | None
    modality: fhirtypes.CodeableConceptType
    number: fhirtypes.UnsignedIntType | None
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    numberOfInstances: fhirtypes.UnsignedIntType | None
    numberOfInstances__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    performer: list[fhirtypes.ImagingStudySeriesPerformerType] | None
    specimen: list[fhirtypes.ReferenceType] | None
    started: fhirtypes.DateTimeType | None
    started__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uid: fhirtypes.IdType | None
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    __resource_type__: str
    number: fhirtypes.UnsignedIntType | None
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sopClass: fhirtypes.CodingType
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uid: fhirtypes.IdType | None
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImagingStudySeriesPerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
