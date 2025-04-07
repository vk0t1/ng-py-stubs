from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MedicinalProductDefinition(domainresource.DomainResource):
    __resource_type__: str
    additionalMonitoringIndicator: fhirtypes.CodeableConceptType | None
    attachedDocument: list[fhirtypes.ReferenceType] | None
    characteristic: list[fhirtypes.MedicinalProductDefinitionCharacteristicType] | None
    classification: list[fhirtypes.CodeableConceptType] | None
    clinicalTrial: list[fhirtypes.ReferenceType] | None
    code: list[fhirtypes.CodingType] | None
    combinedPharmaceuticalDoseForm: fhirtypes.CodeableConceptType | None
    comprisedOf: list[fhirtypes.ReferenceType] | None
    contact: list[fhirtypes.MedicinalProductDefinitionContactType] | None
    crossReference: list[fhirtypes.MedicinalProductDefinitionCrossReferenceType] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    domain: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    impurity: list[fhirtypes.CodeableReferenceType] | None
    indication: fhirtypes.MarkdownType | None
    indication__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    ingredient: list[fhirtypes.CodeableConceptType] | None
    legalStatusOfSupply: fhirtypes.CodeableConceptType | None
    marketingStatus: list[fhirtypes.MarketingStatusType] | None
    masterFile: list[fhirtypes.ReferenceType] | None
    name: list[fhirtypes.MedicinalProductDefinitionNameType]
    operation: list[fhirtypes.MedicinalProductDefinitionOperationType] | None
    packagedMedicinalProduct: list[fhirtypes.CodeableConceptType] | None
    pediatricUseIndicator: fhirtypes.CodeableConceptType | None
    route: list[fhirtypes.CodeableConceptType] | None
    specialMeasures: list[fhirtypes.CodeableConceptType] | None
    status: fhirtypes.CodeableConceptType | None
    statusDate: fhirtypes.DateTimeType | None
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicinalProductDefinitionCharacteristic(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueMarkdown: fhirtypes.MarkdownType | None
    valueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicinalProductDefinitionContact(backboneelement.BackboneElement):
    __resource_type__: str
    contact: fhirtypes.ReferenceType
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicinalProductDefinitionCrossReference(backboneelement.BackboneElement):
    __resource_type__: str
    product: fhirtypes.CodeableReferenceType
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicinalProductDefinitionName(backboneelement.BackboneElement):
    __resource_type__: str
    part: list[fhirtypes.MedicinalProductDefinitionNamePartType] | None
    productName: fhirtypes.StringType | None
    productName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    usage: list[fhirtypes.MedicinalProductDefinitionNameUsageType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MedicinalProductDefinitionNamePart(backboneelement.BackboneElement):
    __resource_type__: str
    part: fhirtypes.StringType | None
    part__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MedicinalProductDefinitionNameUsage(backboneelement.BackboneElement):
    __resource_type__: str
    country: fhirtypes.CodeableConceptType
    jurisdiction: fhirtypes.CodeableConceptType | None
    language: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class MedicinalProductDefinitionOperation(backboneelement.BackboneElement):
    __resource_type__: str
    confidentialityIndicator: fhirtypes.CodeableConceptType | None
    effectiveDate: fhirtypes.PeriodType | None
    organization: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeableReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
