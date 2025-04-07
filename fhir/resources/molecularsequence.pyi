from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MolecularSequence(domainresource.DomainResource):
    __resource_type__: str
    device: fhirtypes.ReferenceType | None
    focus: list[fhirtypes.ReferenceType] | None
    formatted: list[fhirtypes.AttachmentType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    literal: fhirtypes.StringType | None
    literal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    performer: fhirtypes.ReferenceType | None
    relative: list[fhirtypes.MolecularSequenceRelativeType] | None
    specimen: fhirtypes.ReferenceType | None
    subject: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MolecularSequenceRelative(backboneelement.BackboneElement):
    __resource_type__: str
    coordinateSystem: fhirtypes.CodeableConceptType
    edit: list[fhirtypes.MolecularSequenceRelativeEditType] | None
    ordinalPosition: fhirtypes.IntegerType | None
    ordinalPosition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sequenceRange: fhirtypes.RangeType | None
    startingSequence: fhirtypes.MolecularSequenceRelativeStartingSequenceType | None
    @classmethod
    def elements_sequence(cls): ...

class MolecularSequenceRelativeEdit(backboneelement.BackboneElement):
    __resource_type__: str
    end: fhirtypes.IntegerType | None
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    replacedSequence: fhirtypes.StringType | None
    replacedSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    replacementSequence: fhirtypes.StringType | None
    replacementSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    start: fhirtypes.IntegerType | None
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MolecularSequenceRelativeStartingSequence(backboneelement.BackboneElement):
    __resource_type__: str
    chromosome: fhirtypes.CodeableConceptType | None
    genomeAssembly: fhirtypes.CodeableConceptType | None
    orientation: fhirtypes.CodeType | None
    orientation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sequenceCodeableConcept: fhirtypes.CodeableConceptType | None
    sequenceReference: fhirtypes.ReferenceType | None
    sequenceString: fhirtypes.StringType | None
    sequenceString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    strand: fhirtypes.CodeType | None
    strand__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    windowEnd: fhirtypes.IntegerType | None
    windowEnd__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    windowStart: fhirtypes.IntegerType | None
    windowStart__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
