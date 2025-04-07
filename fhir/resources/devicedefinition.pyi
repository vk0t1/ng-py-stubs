from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DeviceDefinition(domainresource.DomainResource):
    __resource_type__: str
    chargeItem: list[fhirtypes.DeviceDefinitionChargeItemType] | None
    classification: list[fhirtypes.DeviceDefinitionClassificationType] | None
    conformsTo: list[fhirtypes.DeviceDefinitionConformsToType] | None
    contact: list[fhirtypes.ContactPointType] | None
    correctiveAction: fhirtypes.DeviceDefinitionCorrectiveActionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    deviceName: list[fhirtypes.DeviceDefinitionDeviceNameType] | None
    guideline: fhirtypes.DeviceDefinitionGuidelineType | None
    hasPart: list[fhirtypes.DeviceDefinitionHasPartType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    languageCode: list[fhirtypes.CodeableConceptType] | None
    link: list[fhirtypes.DeviceDefinitionLinkType] | None
    manufacturer: fhirtypes.ReferenceType | None
    material: list[fhirtypes.DeviceDefinitionMaterialType] | None
    modelNumber: fhirtypes.StringType | None
    modelNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    owner: fhirtypes.ReferenceType | None
    packaging: list[fhirtypes.DeviceDefinitionPackagingType] | None
    partNumber: fhirtypes.StringType | None
    partNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    productionIdentifierInUDI: list[fhirtypes.CodeType | None] | None
    productionIdentifierInUDI__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    property: list[fhirtypes.DeviceDefinitionPropertyType] | None
    regulatoryIdentifier: list[fhirtypes.DeviceDefinitionRegulatoryIdentifierType] | None
    safety: list[fhirtypes.CodeableConceptType] | None
    shelfLifeStorage: list[fhirtypes.ProductShelfLifeType] | None
    udiDeviceIdentifier: list[fhirtypes.DeviceDefinitionUdiDeviceIdentifierType] | None
    version: list[fhirtypes.DeviceDefinitionVersionType] | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionChargeItem(backboneelement.BackboneElement):
    __resource_type__: str
    chargeItemCode: fhirtypes.CodeableReferenceType
    count: fhirtypes.QuantityType
    effectivePeriod: fhirtypes.PeriodType | None
    useContext: list[fhirtypes.UsageContextType] | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionClassification(backboneelement.BackboneElement):
    __resource_type__: str
    justification: list[fhirtypes.RelatedArtifactType] | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionConformsTo(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType | None
    source: list[fhirtypes.RelatedArtifactType] | None
    specification: fhirtypes.CodeableConceptType
    version: list[fhirtypes.StringType | None] | None
    version__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionCorrectiveAction(backboneelement.BackboneElement):
    __resource_type__: str
    period: fhirtypes.PeriodType
    recall: bool | None
    recall__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    scope: fhirtypes.CodeType | None
    scope__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DeviceDefinitionGuideline(backboneelement.BackboneElement):
    __resource_type__: str
    contraindication: list[fhirtypes.CodeableConceptType] | None
    indication: list[fhirtypes.CodeableConceptType] | None
    intendedUse: fhirtypes.StringType | None
    intendedUse__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    usageInstruction: fhirtypes.MarkdownType | None
    usageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    warning: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionHasPart(backboneelement.BackboneElement):
    __resource_type__: str
    count: fhirtypes.IntegerType | None
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reference: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionLink(backboneelement.BackboneElement):
    __resource_type__: str
    relatedDevice: fhirtypes.CodeableReferenceType
    relation: fhirtypes.CodingType
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionMaterial(backboneelement.BackboneElement):
    __resource_type__: str
    allergenicIndicator: bool | None
    allergenicIndicator__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    alternate: bool | None
    alternate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    substance: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionPackaging(backboneelement.BackboneElement):
    __resource_type__: str
    count: fhirtypes.IntegerType | None
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    distributor: list[fhirtypes.DeviceDefinitionPackagingDistributorType] | None
    identifier: fhirtypes.IdentifierType | None
    packaging: list[fhirtypes.DeviceDefinitionPackagingType] | None
    type: fhirtypes.CodeableConceptType | None
    udiDeviceIdentifier: list[fhirtypes.DeviceDefinitionUdiDeviceIdentifierType] | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionPackagingDistributor(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    organizationReference: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceDefinitionProperty(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DeviceDefinitionRegulatoryIdentifier(backboneelement.BackboneElement):
    __resource_type__: str
    deviceIdentifier: fhirtypes.StringType | None
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    issuer: fhirtypes.UriType | None
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    jurisdiction: fhirtypes.UriType | None
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DeviceDefinitionUdiDeviceIdentifier(backboneelement.BackboneElement):
    __resource_type__: str
    deviceIdentifier: fhirtypes.StringType | None
    deviceIdentifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    issuer: fhirtypes.UriType | None
    issuer__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    jurisdiction: fhirtypes.UriType | None
    jurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    marketDistribution: list[fhirtypes.DeviceDefinitionUdiDeviceIdentifierMarketDistributionType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DeviceDefinitionUdiDeviceIdentifierMarketDistribution(backboneelement.BackboneElement):
    __resource_type__: str
    marketPeriod: fhirtypes.PeriodType
    subJurisdiction: fhirtypes.UriType | None
    subJurisdiction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DeviceDefinitionVersion(backboneelement.BackboneElement):
    __resource_type__: str
    component: fhirtypes.IdentifierType | None
    type: fhirtypes.CodeableConceptType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
