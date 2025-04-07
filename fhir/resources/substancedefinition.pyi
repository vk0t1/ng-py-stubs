from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class SubstanceDefinition(domainresource.DomainResource):
    __resource_type__: str
    characterization: list[fhirtypes.SubstanceDefinitionCharacterizationType] | None
    classification: list[fhirtypes.CodeableConceptType] | None
    code: list[fhirtypes.SubstanceDefinitionCodeType] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    domain: fhirtypes.CodeableConceptType | None
    grade: list[fhirtypes.CodeableConceptType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    informationSource: list[fhirtypes.ReferenceType] | None
    manufacturer: list[fhirtypes.ReferenceType] | None
    moiety: list[fhirtypes.SubstanceDefinitionMoietyType] | None
    molecularWeight: list[fhirtypes.SubstanceDefinitionMolecularWeightType] | None
    name: list[fhirtypes.SubstanceDefinitionNameType] | None
    note: list[fhirtypes.AnnotationType] | None
    nucleicAcid: fhirtypes.ReferenceType | None
    polymer: fhirtypes.ReferenceType | None
    property: list[fhirtypes.SubstanceDefinitionPropertyType] | None
    protein: fhirtypes.ReferenceType | None
    referenceInformation: fhirtypes.ReferenceType | None
    relationship: list[fhirtypes.SubstanceDefinitionRelationshipType] | None
    sourceMaterial: fhirtypes.SubstanceDefinitionSourceMaterialType | None
    status: fhirtypes.CodeableConceptType | None
    structure: fhirtypes.SubstanceDefinitionStructureType | None
    supplier: list[fhirtypes.ReferenceType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceDefinitionCharacterization(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    file: list[fhirtypes.AttachmentType] | None
    form: fhirtypes.CodeableConceptType | None
    technique: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceDefinitionCode(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    note: list[fhirtypes.AnnotationType] | None
    source: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeableConceptType | None
    statusDate: fhirtypes.DateTimeType | None
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceDefinitionMoiety(backboneelement.BackboneElement):
    __resource_type__: str
    amountQuantity: fhirtypes.QuantityType | None
    amountString: fhirtypes.StringType | None
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    measurementType: fhirtypes.CodeableConceptType | None
    molecularFormula: fhirtypes.StringType | None
    molecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    opticalActivity: fhirtypes.CodeableConceptType | None
    role: fhirtypes.CodeableConceptType | None
    stereochemistry: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SubstanceDefinitionMolecularWeight(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.QuantityType
    method: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceDefinitionName(backboneelement.BackboneElement):
    __resource_type__: str
    domain: list[fhirtypes.CodeableConceptType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    language: list[fhirtypes.CodeableConceptType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    official: list[fhirtypes.SubstanceDefinitionNameOfficialType] | None
    preferred: bool | None
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    source: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeableConceptType | None
    synonym: list[fhirtypes.SubstanceDefinitionNameType] | None
    translation: list[fhirtypes.SubstanceDefinitionNameType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SubstanceDefinitionNameOfficial(backboneelement.BackboneElement):
    __resource_type__: str
    authority: fhirtypes.CodeableConceptType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceDefinitionProperty(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SubstanceDefinitionRelationship(backboneelement.BackboneElement):
    __resource_type__: str
    amountQuantity: fhirtypes.QuantityType | None
    amountRatio: fhirtypes.RatioType | None
    amountString: fhirtypes.StringType | None
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    comparator: fhirtypes.CodeableConceptType | None
    isDefining: bool | None
    isDefining__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    ratioHighLimitAmount: fhirtypes.RatioType | None
    source: list[fhirtypes.ReferenceType] | None
    substanceDefinitionCodeableConcept: fhirtypes.CodeableConceptType | None
    substanceDefinitionReference: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SubstanceDefinitionSourceMaterial(backboneelement.BackboneElement):
    __resource_type__: str
    countryOfOrigin: list[fhirtypes.CodeableConceptType] | None
    genus: fhirtypes.CodeableConceptType | None
    part: fhirtypes.CodeableConceptType | None
    species: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceDefinitionStructure(backboneelement.BackboneElement):
    __resource_type__: str
    molecularFormula: fhirtypes.StringType | None
    molecularFormula__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    molecularFormulaByMoiety: fhirtypes.StringType | None
    molecularFormulaByMoiety__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    molecularWeight: fhirtypes.SubstanceDefinitionMolecularWeightType | None
    opticalActivity: fhirtypes.CodeableConceptType | None
    representation: list[fhirtypes.SubstanceDefinitionStructureRepresentationType] | None
    sourceDocument: list[fhirtypes.ReferenceType] | None
    stereochemistry: fhirtypes.CodeableConceptType | None
    technique: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceDefinitionStructureRepresentation(backboneelement.BackboneElement):
    __resource_type__: str
    document: fhirtypes.ReferenceType | None
    format: fhirtypes.CodeableConceptType | None
    representation: fhirtypes.StringType | None
    representation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
