from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ConditionDefinition(domainresource.DomainResource):
    __resource_type__: str
    bodySite: fhirtypes.CodeableConceptType | None
    code: fhirtypes.CodeableConceptType
    contact: list[fhirtypes.ContactDetailType] | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    definition: list[fhirtypes.UriType | None] | None
    definition__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    hasBodySite: bool | None
    hasBodySite__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    hasSeverity: bool | None
    hasSeverity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    hasStage: bool | None
    hasStage__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    medication: list[fhirtypes.ConditionDefinitionMedicationType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    observation: list[fhirtypes.ConditionDefinitionObservationType] | None
    plan: list[fhirtypes.ConditionDefinitionPlanType] | None
    precondition: list[fhirtypes.ConditionDefinitionPreconditionType] | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    questionnaire: list[fhirtypes.ConditionDefinitionQuestionnaireType] | None
    severity: fhirtypes.CodeableConceptType | None
    stage: fhirtypes.CodeableConceptType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subtitle: fhirtypes.StringType | None
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    team: list[fhirtypes.ReferenceType] | None
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

class ConditionDefinitionMedication(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType | None
    code: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ConditionDefinitionObservation(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType | None
    code: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ConditionDefinitionPlan(backboneelement.BackboneElement):
    __resource_type__: str
    reference: fhirtypes.ReferenceType
    role: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ConditionDefinitionPrecondition(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ConditionDefinitionQuestionnaire(backboneelement.BackboneElement):
    __resource_type__: str
    purpose: fhirtypes.CodeType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reference: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
