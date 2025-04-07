from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class BodyStructure(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    excludedStructure: list[fhirtypes.BodyStructureIncludedStructureType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    image: list[fhirtypes.AttachmentType] | None
    includedStructure: list[fhirtypes.BodyStructureIncludedStructureType]
    morphology: fhirtypes.CodeableConceptType | None
    patient: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...

class BodyStructureIncludedStructure(backboneelement.BackboneElement):
    __resource_type__: str
    bodyLandmarkOrientation: list[fhirtypes.BodyStructureIncludedStructureBodyLandmarkOrientationType] | None
    laterality: fhirtypes.CodeableConceptType | None
    qualifier: list[fhirtypes.CodeableConceptType] | None
    spatialReference: list[fhirtypes.ReferenceType] | None
    structure: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class BodyStructureIncludedStructureBodyLandmarkOrientation(backboneelement.BackboneElement):
    __resource_type__: str
    clockFacePosition: list[fhirtypes.CodeableConceptType] | None
    distanceFromLandmark: (
        list[fhirtypes.BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmarkType] | None
    )
    landmarkDescription: list[fhirtypes.CodeableConceptType] | None
    surfaceOrientation: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class BodyStructureIncludedStructureBodyLandmarkOrientationDistanceFromLandmark(backboneelement.BackboneElement):
    __resource_type__: str
    device: list[fhirtypes.CodeableReferenceType] | None
    value: list[fhirtypes.QuantityType] | None
    @classmethod
    def elements_sequence(cls): ...
