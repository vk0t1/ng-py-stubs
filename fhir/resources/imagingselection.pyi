from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ImagingSelection(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    bodySite: fhirtypes.CodeableReferenceType | None
    category: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType
    derivedFrom: list[fhirtypes.ReferenceType] | None
    endpoint: list[fhirtypes.ReferenceType] | None
    focus: list[fhirtypes.ReferenceType] | None
    frameOfReferenceUid: fhirtypes.IdType | None
    frameOfReferenceUid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    instance: list[fhirtypes.ImagingSelectionInstanceType] | None
    issued: fhirtypes.InstantType | None
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    performer: list[fhirtypes.ImagingSelectionPerformerType] | None
    seriesNumber: fhirtypes.UnsignedIntType | None
    seriesNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    seriesUid: fhirtypes.IdType | None
    seriesUid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    studyUid: fhirtypes.IdType | None
    studyUid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImagingSelectionInstance(backboneelement.BackboneElement):
    __resource_type__: str
    imageRegion2D: list[fhirtypes.ImagingSelectionInstanceImageRegion2DType] | None
    imageRegion3D: list[fhirtypes.ImagingSelectionInstanceImageRegion3DType] | None
    number: fhirtypes.UnsignedIntType | None
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sopClass: fhirtypes.CodingType | None
    subset: list[fhirtypes.StringType | None] | None
    subset__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    uid: fhirtypes.IdType | None
    uid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImagingSelectionInstanceImageRegion2D(backboneelement.BackboneElement):
    __resource_type__: str
    coordinate: list[fhirtypes.DecimalType | None] | None
    coordinate__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    regionType: fhirtypes.CodeType | None
    regionType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImagingSelectionInstanceImageRegion3D(backboneelement.BackboneElement):
    __resource_type__: str
    coordinate: list[fhirtypes.DecimalType | None] | None
    coordinate__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    regionType: fhirtypes.CodeType | None
    regionType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImagingSelectionPerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType | None
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
