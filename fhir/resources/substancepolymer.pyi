from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class SubstancePolymer(domainresource.DomainResource):
    __resource_type__: str
    class_fhir: fhirtypes.CodeableConceptType | None
    copolymerConnectivity: list[fhirtypes.CodeableConceptType] | None
    geometry: fhirtypes.CodeableConceptType | None
    identifier: fhirtypes.IdentifierType | None
    modification: fhirtypes.StringType | None
    modification__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    monomerSet: list[fhirtypes.SubstancePolymerMonomerSetType] | None
    repeat: list[fhirtypes.SubstancePolymerRepeatType] | None
    @classmethod
    def elements_sequence(cls): ...

class SubstancePolymerMonomerSet(backboneelement.BackboneElement):
    __resource_type__: str
    ratioType: fhirtypes.CodeableConceptType | None
    startingMaterial: list[fhirtypes.SubstancePolymerMonomerSetStartingMaterialType] | None
    @classmethod
    def elements_sequence(cls): ...

class SubstancePolymerMonomerSetStartingMaterial(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.QuantityType | None
    category: fhirtypes.CodeableConceptType | None
    code: fhirtypes.CodeableConceptType | None
    isDefining: bool | None
    isDefining__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstancePolymerRepeat(backboneelement.BackboneElement):
    __resource_type__: str
    averageMolecularFormula: fhirtypes.StringType | None
    averageMolecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    repeatUnit: list[fhirtypes.SubstancePolymerRepeatRepeatUnitType] | None
    repeatUnitAmountType: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstancePolymerRepeatRepeatUnit(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.IntegerType | None
    amount__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    degreeOfPolymerisation: list[fhirtypes.SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisationType] | None
    orientation: fhirtypes.CodeableConceptType | None
    structuralRepresentation: list[fhirtypes.SubstancePolymerRepeatRepeatUnitStructuralRepresentationType] | None
    unit: fhirtypes.StringType | None
    unit__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation(backboneelement.BackboneElement):
    __resource_type__: str
    average: fhirtypes.IntegerType | None
    average__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    high: fhirtypes.IntegerType | None
    high__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    low: fhirtypes.IntegerType | None
    low__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstancePolymerRepeatRepeatUnitStructuralRepresentation(backboneelement.BackboneElement):
    __resource_type__: str
    attachment: fhirtypes.AttachmentType | None
    format: fhirtypes.CodeableConceptType | None
    representation: fhirtypes.StringType | None
    representation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
