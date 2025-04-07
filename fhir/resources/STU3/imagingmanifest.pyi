from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ImagingManifest(domainresource.DomainResource):
    __resource_type__: str
    author: fhirtypes.ReferenceType | None
    authoringTime: fhirtypes.DateTimeType | None
    authoringTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    patient: fhirtypes.ReferenceType
    study: list[fhirtypes.ImagingManifestStudyType]
    @classmethod
    def elements_sequence(cls): ...

class ImagingManifestStudy(backboneelement.BackboneElement):
    __resource_type__: str
    endpoint: list[fhirtypes.ReferenceType] | None
    imagingStudy: fhirtypes.ReferenceType | None
    series: list[fhirtypes.ImagingManifestStudySeriesType]
    uid: fhirtypes.OidType | None
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImagingManifestStudySeries(backboneelement.BackboneElement):
    __resource_type__: str
    endpoint: list[fhirtypes.ReferenceType] | None
    instance: list[fhirtypes.ImagingManifestStudySeriesInstanceType]
    uid: fhirtypes.OidType | None
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImagingManifestStudySeriesInstance(backboneelement.BackboneElement):
    __resource_type__: str
    sopClass: fhirtypes.OidType | None
    sopClass__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uid: fhirtypes.OidType | None
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
