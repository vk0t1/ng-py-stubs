from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class SubstanceSourceMaterial(domainresource.DomainResource):
    __resource_type__: str
    countryOfOrigin: list[fhirtypes.CodeableConceptType] | None
    developmentStage: fhirtypes.CodeableConceptType | None
    fractionDescription: list[fhirtypes.SubstanceSourceMaterialFractionDescriptionType] | None
    geographicalLocation: list[fhirtypes.StringType | None] | None
    geographicalLocation__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    organism: fhirtypes.SubstanceSourceMaterialOrganismType | None
    organismId: fhirtypes.IdentifierType | None
    organismName: fhirtypes.StringType | None
    organismName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    parentSubstanceId: list[fhirtypes.IdentifierType] | None
    parentSubstanceName: list[fhirtypes.StringType | None] | None
    parentSubstanceName__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    partDescription: list[fhirtypes.SubstanceSourceMaterialPartDescriptionType] | None
    sourceMaterialClass: fhirtypes.CodeableConceptType | None
    sourceMaterialState: fhirtypes.CodeableConceptType | None
    sourceMaterialType: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceSourceMaterialFractionDescription(backboneelement.BackboneElement):
    __resource_type__: str
    fraction: fhirtypes.StringType | None
    fraction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    materialType: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceSourceMaterialOrganism(backboneelement.BackboneElement):
    __resource_type__: str
    author: list[fhirtypes.SubstanceSourceMaterialOrganismAuthorType] | None
    family: fhirtypes.CodeableConceptType | None
    genus: fhirtypes.CodeableConceptType | None
    hybrid: fhirtypes.SubstanceSourceMaterialOrganismHybridType | None
    intraspecificDescription: fhirtypes.StringType | None
    intraspecificDescription__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    intraspecificType: fhirtypes.CodeableConceptType | None
    organismGeneral: fhirtypes.SubstanceSourceMaterialOrganismOrganismGeneralType | None
    species: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceSourceMaterialOrganismAuthor(backboneelement.BackboneElement):
    __resource_type__: str
    authorDescription: fhirtypes.StringType | None
    authorDescription__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    authorType: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceSourceMaterialOrganismHybrid(backboneelement.BackboneElement):
    __resource_type__: str
    hybridType: fhirtypes.CodeableConceptType | None
    maternalOrganismId: fhirtypes.StringType | None
    maternalOrganismId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maternalOrganismName: fhirtypes.StringType | None
    maternalOrganismName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    paternalOrganismId: fhirtypes.StringType | None
    paternalOrganismId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    paternalOrganismName: fhirtypes.StringType | None
    paternalOrganismName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceSourceMaterialOrganismOrganismGeneral(backboneelement.BackboneElement):
    __resource_type__: str
    class_fhir: fhirtypes.CodeableConceptType | None
    kingdom: fhirtypes.CodeableConceptType | None
    order: fhirtypes.CodeableConceptType | None
    phylum: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceSourceMaterialPartDescription(backboneelement.BackboneElement):
    __resource_type__: str
    part: fhirtypes.CodeableConceptType | None
    partLocation: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
