from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class SubstanceNucleicAcid(domainresource.DomainResource):
    __resource_type__: str
    areaOfHybridisation: fhirtypes.StringType | None
    areaOfHybridisation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    numberOfSubunits: fhirtypes.IntegerType | None
    numberOfSubunits__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    oligoNucleotideType: fhirtypes.CodeableConceptType | None
    sequenceType: fhirtypes.CodeableConceptType | None
    subunit: list[fhirtypes.SubstanceNucleicAcidSubunitType] | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceNucleicAcidSubunit(backboneelement.BackboneElement):
    __resource_type__: str
    fivePrime: fhirtypes.CodeableConceptType | None
    length: fhirtypes.IntegerType | None
    length__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    linkage: list[fhirtypes.SubstanceNucleicAcidSubunitLinkageType] | None
    sequence: fhirtypes.StringType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sequenceAttachment: fhirtypes.AttachmentType | None
    subunit: fhirtypes.IntegerType | None
    subunit__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sugar: list[fhirtypes.SubstanceNucleicAcidSubunitSugarType] | None
    threePrime: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceNucleicAcidSubunitLinkage(backboneelement.BackboneElement):
    __resource_type__: str
    connectivity: fhirtypes.StringType | None
    connectivity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    residueSite: fhirtypes.StringType | None
    residueSite__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceNucleicAcidSubunitSugar(backboneelement.BackboneElement):
    __resource_type__: str
    identifier: fhirtypes.IdentifierType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    residueSite: fhirtypes.StringType | None
    residueSite__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
