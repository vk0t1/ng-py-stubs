from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class SubstanceProtein(domainresource.DomainResource):
    __resource_type__: str
    disulfideLinkage: list[fhirtypes.StringType | None] | None
    disulfideLinkage__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    numberOfSubunits: fhirtypes.IntegerType | None
    numberOfSubunits__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sequenceType: fhirtypes.CodeableConceptType | None
    subunit: list[fhirtypes.SubstanceProteinSubunitType] | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceProteinSubunit(backboneelement.BackboneElement):
    __resource_type__: str
    cTerminalModification: fhirtypes.StringType | None
    cTerminalModification__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    cTerminalModificationId: fhirtypes.IdentifierType | None
    length: fhirtypes.IntegerType | None
    length__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    nTerminalModification: fhirtypes.StringType | None
    nTerminalModification__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    nTerminalModificationId: fhirtypes.IdentifierType | None
    sequence: fhirtypes.StringType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sequenceAttachment: fhirtypes.AttachmentType | None
    subunit: fhirtypes.IntegerType | None
    subunit__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
