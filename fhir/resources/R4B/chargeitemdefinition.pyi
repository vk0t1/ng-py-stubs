from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ChargeItemDefinition(domainresource.DomainResource):
    __resource_type__: str
    applicability: list[fhirtypes.ChargeItemDefinitionApplicabilityType] | None
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    code: fhirtypes.CodeableConceptType | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    derivedFromUri: list[fhirtypes.UriType | None] | None
    derivedFromUri__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectivePeriod: fhirtypes.PeriodType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    instance: list[fhirtypes.ReferenceType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    partOf: list[fhirtypes.CanonicalType | None] | None
    partOf__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    propertyGroup: list[fhirtypes.ChargeItemDefinitionPropertyGroupType] | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    replaces: list[fhirtypes.CanonicalType | None] | None
    replaces__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ChargeItemDefinitionApplicability(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    expression: fhirtypes.StringType | None
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    language: fhirtypes.StringType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ChargeItemDefinitionPropertyGroup(backboneelement.BackboneElement):
    __resource_type__: str
    applicability: list[fhirtypes.ChargeItemDefinitionApplicabilityType] | None
    priceComponent: list[fhirtypes.ChargeItemDefinitionPropertyGroupPriceComponentType] | None
    @classmethod
    def elements_sequence(cls): ...

class ChargeItemDefinitionPropertyGroupPriceComponent(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.MoneyType | None
    code: fhirtypes.CodeableConceptType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
