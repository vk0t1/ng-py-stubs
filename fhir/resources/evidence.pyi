from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Evidence(domainresource.DomainResource):
    __resource_type__: str
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    assertion: fhirtypes.MarkdownType | None
    assertion__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    author: list[fhirtypes.ContactDetailType] | None
    certainty: list[fhirtypes.EvidenceCertaintyType] | None
    citeAsMarkdown: fhirtypes.MarkdownType | None
    citeAsMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    citeAsReference: fhirtypes.ReferenceType | None
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
    endorser: list[fhirtypes.ContactDetailType] | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    statistic: list[fhirtypes.EvidenceStatisticType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    studyDesign: list[fhirtypes.CodeableConceptType] | None
    synthesisType: fhirtypes.CodeableConceptType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    variableDefinition: list[fhirtypes.EvidenceVariableDefinitionType]
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    versionAlgorithmCoding: fhirtypes.CodingType | None
    versionAlgorithmString: fhirtypes.StringType | None
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class EvidenceCertainty(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    rater: fhirtypes.StringType | None
    rater__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rating: fhirtypes.CodeableConceptType | None
    subcomponent: list[fhirtypes.EvidenceCertaintyType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class EvidenceStatistic(backboneelement.BackboneElement):
    __resource_type__: str
    attributeEstimate: list[fhirtypes.EvidenceStatisticAttributeEstimateType] | None
    category: fhirtypes.CodeableConceptType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modelCharacteristic: list[fhirtypes.EvidenceStatisticModelCharacteristicType] | None
    note: list[fhirtypes.AnnotationType] | None
    numberAffected: fhirtypes.UnsignedIntType | None
    numberAffected__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    numberOfEvents: fhirtypes.UnsignedIntType | None
    numberOfEvents__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.QuantityType | None
    sampleSize: fhirtypes.EvidenceStatisticSampleSizeType | None
    statisticType: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class EvidenceStatisticAttributeEstimate(backboneelement.BackboneElement):
    __resource_type__: str
    attributeEstimate: list[fhirtypes.EvidenceStatisticAttributeEstimateType] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    level: fhirtypes.DecimalType | None
    level__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    quantity: fhirtypes.QuantityType | None
    range: fhirtypes.RangeType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class EvidenceStatisticModelCharacteristic(backboneelement.BackboneElement):
    __resource_type__: str
    attributeEstimate: list[fhirtypes.EvidenceStatisticAttributeEstimateType] | None
    code: fhirtypes.CodeableConceptType
    value: fhirtypes.QuantityType | None
    variable: list[fhirtypes.EvidenceStatisticModelCharacteristicVariableType] | None
    @classmethod
    def elements_sequence(cls): ...

class EvidenceStatisticModelCharacteristicVariable(backboneelement.BackboneElement):
    __resource_type__: str
    handling: fhirtypes.CodeType | None
    handling__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCategory: list[fhirtypes.CodeableConceptType] | None
    valueQuantity: list[fhirtypes.QuantityType] | None
    valueRange: list[fhirtypes.RangeType] | None
    variableDefinition: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...

class EvidenceStatisticSampleSize(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    knownDataCount: fhirtypes.UnsignedIntType | None
    knownDataCount__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    numberOfParticipants: fhirtypes.UnsignedIntType | None
    numberOfParticipants__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    numberOfStudies: fhirtypes.UnsignedIntType | None
    numberOfStudies__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class EvidenceVariableDefinition(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    directnessMatch: fhirtypes.CodeableConceptType | None
    intended: fhirtypes.ReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    observed: fhirtypes.ReferenceType | None
    variableRole: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
