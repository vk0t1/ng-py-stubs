from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class EvidenceVariable(domainresource.DomainResource):
    __resource_type__: str
    actual: bool | None
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    author: list[fhirtypes.ContactDetailType] | None
    category: list[fhirtypes.EvidenceVariableCategoryType] | None
    characteristic: list[fhirtypes.EvidenceVariableCharacteristicType] | None
    characteristicCombination: fhirtypes.CodeType | None
    characteristicCombination__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contact: list[fhirtypes.ContactDetailType] | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    editor: list[fhirtypes.ContactDetailType] | None
    endorser: list[fhirtypes.ContactDetailType] | None
    handling: fhirtypes.CodeType | None
    handling__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    reviewer: list[fhirtypes.ContactDetailType] | None
    shortTitle: fhirtypes.StringType | None
    shortTitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subtitle: fhirtypes.StringType | None
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    definitionCanonical: fhirtypes.CanonicalType | None
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    definitionCodeableConcept: fhirtypes.CodeableConceptType | None
    definitionExpression: fhirtypes.ExpressionType | None
    definitionReference: fhirtypes.ReferenceType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    device: fhirtypes.ReferenceType | None
    exclude: bool | None
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    groupMeasure: fhirtypes.CodeType | None
    groupMeasure__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    method: fhirtypes.CodeableConceptType | None
    timeFromStart: fhirtypes.EvidenceVariableCharacteristicTimeFromStartType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class EvidenceVariableCharacteristicTimeFromStart(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    quantity: fhirtypes.QuantityType | None
    range: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...
