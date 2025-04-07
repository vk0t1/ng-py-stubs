from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ConceptMap(domainresource.DomainResource):
    __resource_type__: str
    additionalAttribute: list[fhirtypes.ConceptMapAdditionalAttributeType] | None
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    author: list[fhirtypes.ContactDetailType] | None
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
    group: list[fhirtypes.ConceptMapGroupType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    property: list[fhirtypes.ConceptMapPropertyType] | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    reviewer: list[fhirtypes.ContactDetailType] | None
    sourceScopeCanonical: fhirtypes.CanonicalType | None
    sourceScopeCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sourceScopeUri: fhirtypes.UriType | None
    sourceScopeUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetScopeCanonical: fhirtypes.CanonicalType | None
    targetScopeCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetScopeUri: fhirtypes.UriType | None
    targetScopeUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    topic: list[fhirtypes.CodeableConceptType] | None
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

class ConceptMapAdditionalAttribute(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uri: fhirtypes.UriType | None
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ConceptMapGroup(backboneelement.BackboneElement):
    __resource_type__: str
    element: list[fhirtypes.ConceptMapGroupElementType]
    source: fhirtypes.CanonicalType | None
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    target: fhirtypes.CanonicalType | None
    target__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    unmapped: fhirtypes.ConceptMapGroupUnmappedType | None
    @classmethod
    def elements_sequence(cls): ...

class ConceptMapGroupElement(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    noMap: bool | None
    noMap__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    target: list[fhirtypes.ConceptMapGroupElementTargetType] | None
    valueSet: fhirtypes.CanonicalType | None
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ConceptMapGroupElementTarget(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dependsOn: list[fhirtypes.ConceptMapGroupElementTargetDependsOnType] | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    product: list[fhirtypes.ConceptMapGroupElementTargetDependsOnType] | None
    property: list[fhirtypes.ConceptMapGroupElementTargetPropertyType] | None
    relationship: fhirtypes.CodeType | None
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueSet: fhirtypes.CanonicalType | None
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ConceptMapGroupElementTargetDependsOn(backboneelement.BackboneElement):
    __resource_type__: str
    attribute: fhirtypes.CodeType | None
    attribute__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCode: fhirtypes.CodeType | None
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCoding: fhirtypes.CodingType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueSet: fhirtypes.CanonicalType | None
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ConceptMapGroupElementTargetProperty(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCode: fhirtypes.CodeType | None
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCoding: fhirtypes.CodingType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ConceptMapGroupUnmapped(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    otherMap: fhirtypes.CanonicalType | None
    otherMap__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relationship: fhirtypes.CodeType | None
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueSet: fhirtypes.CanonicalType | None
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ConceptMapProperty(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    system: fhirtypes.CanonicalType | None
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uri: fhirtypes.UriType | None
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
