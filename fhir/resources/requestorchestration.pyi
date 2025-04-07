from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class RequestOrchestration(domainresource.DomainResource):
    __resource_type__: str
    action: list[fhirtypes.RequestOrchestrationActionType] | None
    author: fhirtypes.ReferenceType | None
    authoredOn: fhirtypes.DateTimeType | None
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    code: fhirtypes.CodeableConceptType | None
    encounter: fhirtypes.ReferenceType | None
    goal: list[fhirtypes.ReferenceType] | None
    groupIdentifier: fhirtypes.IdentifierType | None
    identifier: list[fhirtypes.IdentifierType] | None
    instantiatesCanonical: list[fhirtypes.CanonicalType | None] | None
    instantiatesCanonical__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    instantiatesUri: list[fhirtypes.UriType | None] | None
    instantiatesUri__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    intent: fhirtypes.CodeType | None
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    replaces: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class RequestOrchestrationAction(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.RequestOrchestrationActionType] | None
    cardinalityBehavior: fhirtypes.CodeType | None
    cardinalityBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    code: list[fhirtypes.CodeableConceptType] | None
    condition: list[fhirtypes.RequestOrchestrationActionConditionType] | None
    definitionCanonical: fhirtypes.CanonicalType | None
    definitionCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    definitionUri: fhirtypes.UriType | None
    definitionUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    documentation: list[fhirtypes.RelatedArtifactType] | None
    dynamicValue: list[fhirtypes.RequestOrchestrationActionDynamicValueType] | None
    goal: list[fhirtypes.ReferenceType] | None
    groupingBehavior: fhirtypes.CodeType | None
    groupingBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    input: list[fhirtypes.RequestOrchestrationActionInputType] | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    location: fhirtypes.CodeableReferenceType | None
    output: list[fhirtypes.RequestOrchestrationActionOutputType] | None
    participant: list[fhirtypes.RequestOrchestrationActionParticipantType] | None
    precheckBehavior: fhirtypes.CodeType | None
    precheckBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    prefix: fhirtypes.StringType | None
    prefix__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relatedAction: list[fhirtypes.RequestOrchestrationActionRelatedActionType] | None
    requiredBehavior: fhirtypes.CodeType | None
    requiredBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resource: fhirtypes.ReferenceType | None
    selectionBehavior: fhirtypes.CodeType | None
    selectionBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    textEquivalent: fhirtypes.MarkdownType | None
    textEquivalent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingAge: fhirtypes.AgeType | None
    timingDateTime: fhirtypes.DateTimeType | None
    timingDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingDuration: fhirtypes.DurationType | None
    timingPeriod: fhirtypes.PeriodType | None
    timingRange: fhirtypes.RangeType | None
    timingTiming: fhirtypes.TimingType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    transform: fhirtypes.CanonicalType | None
    transform__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class RequestOrchestrationActionCondition(backboneelement.BackboneElement):
    __resource_type__: str
    expression: fhirtypes.ExpressionType | None
    kind: fhirtypes.CodeType | None
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class RequestOrchestrationActionDynamicValue(backboneelement.BackboneElement):
    __resource_type__: str
    expression: fhirtypes.ExpressionType | None
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class RequestOrchestrationActionInput(backboneelement.BackboneElement):
    __resource_type__: str
    relatedData: fhirtypes.IdType | None
    relatedData__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    requirement: fhirtypes.DataRequirementType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class RequestOrchestrationActionOutput(backboneelement.BackboneElement):
    __resource_type__: str
    relatedData: fhirtypes.StringType | None
    relatedData__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    requirement: fhirtypes.DataRequirementType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class RequestOrchestrationActionParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    actorCanonical: fhirtypes.CanonicalType | None
    actorCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    actorReference: fhirtypes.ReferenceType | None
    function: fhirtypes.CodeableConceptType | None
    role: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    typeCanonical: fhirtypes.CanonicalType | None
    typeCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    typeReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class RequestOrchestrationActionRelatedAction(backboneelement.BackboneElement):
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
