from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class PlanDefinition(domainresource.DomainResource):
    __resource_type__: str
    action: list[fhirtypes.PlanDefinitionActionType] | None
    actor: list[fhirtypes.PlanDefinitionActorType] | None
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    asNeededBoolean: bool | None
    asNeededBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    asNeededCodeableConcept: fhirtypes.CodeableConceptType | None
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
    goal: list[fhirtypes.PlanDefinitionGoalType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    library: list[fhirtypes.CanonicalType | None] | None
    library__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    reviewer: list[fhirtypes.ContactDetailType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectCanonical: fhirtypes.CanonicalType | None
    subjectCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectCodeableConcept: fhirtypes.CodeableConceptType | None
    subjectReference: fhirtypes.ReferenceType | None
    subtitle: fhirtypes.StringType | None
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    topic: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    usage: fhirtypes.MarkdownType | None
    usage__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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

class PlanDefinitionAction(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.PlanDefinitionActionType] | None
    cardinalityBehavior: fhirtypes.CodeType | None
    cardinalityBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    code: fhirtypes.CodeableConceptType | None
    condition: list[fhirtypes.PlanDefinitionActionConditionType] | None
    definitionCanonical: fhirtypes.CanonicalType | None
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    definitionUri: fhirtypes.UriType | None
    definitionUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    documentation: list[fhirtypes.RelatedArtifactType] | None
    dynamicValue: list[fhirtypes.PlanDefinitionActionDynamicValueType] | None
    goalId: list[fhirtypes.IdType | None] | None
    goalId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    groupingBehavior: fhirtypes.CodeType | None
    groupingBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    input: list[fhirtypes.PlanDefinitionActionInputType] | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    location: fhirtypes.CodeableReferenceType | None
    output: list[fhirtypes.PlanDefinitionActionOutputType] | None
    participant: list[fhirtypes.PlanDefinitionActionParticipantType] | None
    precheckBehavior: fhirtypes.CodeType | None
    precheckBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    prefix: fhirtypes.StringType | None
    prefix__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reason: list[fhirtypes.CodeableConceptType] | None
    relatedAction: list[fhirtypes.PlanDefinitionActionRelatedActionType] | None
    requiredBehavior: fhirtypes.CodeType | None
    requiredBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    selectionBehavior: fhirtypes.CodeType | None
    selectionBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectCanonical: fhirtypes.CanonicalType | None
    subjectCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectCodeableConcept: fhirtypes.CodeableConceptType | None
    subjectReference: fhirtypes.ReferenceType | None
    textEquivalent: fhirtypes.MarkdownType | None
    textEquivalent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingAge: fhirtypes.AgeType | None
    timingDuration: fhirtypes.DurationType | None
    timingRange: fhirtypes.RangeType | None
    timingTiming: fhirtypes.TimingType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    transform: fhirtypes.CanonicalType | None
    transform__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    trigger: list[fhirtypes.TriggerDefinitionType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class PlanDefinitionActionCondition(backboneelement.BackboneElement):
    __resource_type__: str
    expression: fhirtypes.ExpressionType | None
    kind: fhirtypes.CodeType | None
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class PlanDefinitionActionDynamicValue(backboneelement.BackboneElement):
    __resource_type__: str
    expression: fhirtypes.ExpressionType | None
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class PlanDefinitionActionInput(backboneelement.BackboneElement):
    __resource_type__: str
    relatedData: fhirtypes.IdType | None
    relatedData__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    requirement: fhirtypes.DataRequirementType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class PlanDefinitionActionOutput(backboneelement.BackboneElement):
    __resource_type__: str
    relatedData: fhirtypes.StringType | None
    relatedData__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    requirement: fhirtypes.DataRequirementType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class PlanDefinitionActionParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    actorId: fhirtypes.StringType | None
    actorId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    function: fhirtypes.CodeableConceptType | None
    role: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    typeCanonical: fhirtypes.CanonicalType | None
    typeCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    typeReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class PlanDefinitionActionRelatedAction(backboneelement.BackboneElement):
    __resource_type__: str
    endRelationship: fhirtypes.CodeType | None
    endRelationship__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    offsetDuration: fhirtypes.DurationType | None
    offsetRange: fhirtypes.RangeType | None
    relationship: fhirtypes.CodeType | None
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetId: fhirtypes.IdType | None
    targetId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class PlanDefinitionActor(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    option: list[fhirtypes.PlanDefinitionActorOptionType]
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class PlanDefinitionActorOption(backboneelement.BackboneElement):
    __resource_type__: str
    role: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    typeCanonical: fhirtypes.CanonicalType | None
    typeCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    typeReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class PlanDefinitionGoal(backboneelement.BackboneElement):
    __resource_type__: str
    addresses: list[fhirtypes.CodeableConceptType] | None
    category: fhirtypes.CodeableConceptType | None
    description: fhirtypes.CodeableConceptType
    documentation: list[fhirtypes.RelatedArtifactType] | None
    priority: fhirtypes.CodeableConceptType | None
    start: fhirtypes.CodeableConceptType | None
    target: list[fhirtypes.PlanDefinitionGoalTargetType] | None
    @classmethod
    def elements_sequence(cls): ...

class PlanDefinitionGoalTarget(backboneelement.BackboneElement):
    __resource_type__: str
    detailBoolean: bool | None
    detailBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    detailCodeableConcept: fhirtypes.CodeableConceptType | None
    detailInteger: fhirtypes.IntegerType | None
    detailInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    detailQuantity: fhirtypes.QuantityType | None
    detailRange: fhirtypes.RangeType | None
    detailRatio: fhirtypes.RatioType | None
    detailString: fhirtypes.StringType | None
    detailString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    due: fhirtypes.DurationType | None
    measure: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
