from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class EvidenceVariable(domainresource.DomainResource):
    __resource_type__: str
    actual: bool | None
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    author: list[fhirtypes.ContactDetailType] | None
    category: list[fhirtypes.EvidenceVariableCategoryType] | None
    characteristic: list[fhirtypes.EvidenceVariableCharacteristicType] | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyrightLabel: fhirtypes.StringType | None
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    editor: list[fhirtypes.ContactDetailType] | None
    effectivePeriod: fhirtypes.PeriodType | None
    endorser: list[fhirtypes.ContactDetailType] | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    handling: fhirtypes.CodeType | None
    handling__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    reviewer: list[fhirtypes.ContactDetailType] | None
    shortTitle: fhirtypes.StringType | None
    shortTitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    versionAlgorithmCoding: fhirtypes.CodingType | None
    versionAlgorithmString: fhirtypes.StringType | None
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class EvidenceVariableCategory(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class EvidenceVariableCharacteristic(backboneelement.BackboneElement):
    __resource_type__: str
    definitionByCombination: fhirtypes.EvidenceVariableCharacteristicDefinitionByCombinationType | None
    definitionByTypeAndValue: fhirtypes.EvidenceVariableCharacteristicDefinitionByTypeAndValueType | None
    definitionCanonical: fhirtypes.CanonicalType | None
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    definitionCodeableConcept: fhirtypes.CodeableConceptType | None
    definitionExpression: fhirtypes.ExpressionType | None
    definitionId: fhirtypes.IdType | None
    definitionId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    definitionReference: fhirtypes.ReferenceType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    durationQuantity: fhirtypes.QuantityType | None
    durationRange: fhirtypes.RangeType | None
    exclude: bool | None
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    instancesQuantity: fhirtypes.QuantityType | None
    instancesRange: fhirtypes.RangeType | None
    linkId: fhirtypes.IdType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    timeFromEvent: list[fhirtypes.EvidenceVariableCharacteristicTimeFromEventType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class EvidenceVariableCharacteristicDefinitionByCombination(backboneelement.BackboneElement):
    __resource_type__: str
    characteristic: list[fhirtypes.EvidenceVariableCharacteristicType]
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    threshold: fhirtypes.PositiveIntType | None
    threshold__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class EvidenceVariableCharacteristicDefinitionByTypeAndValue(backboneelement.BackboneElement):
    __resource_type__: str
    device: fhirtypes.ReferenceType | None
    method: list[fhirtypes.CodeableConceptType] | None
    offset: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeableConceptType
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueId: fhirtypes.IdType | None
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class EvidenceVariableCharacteristicTimeFromEvent(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    eventCodeableConcept: fhirtypes.CodeableConceptType | None
    eventDateTime: fhirtypes.DateTimeType | None
    eventDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    eventId: fhirtypes.IdType | None
    eventId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    eventReference: fhirtypes.ReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    quantity: fhirtypes.QuantityType | None
    range: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
