from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class RequestGroup(domainresource.DomainResource):
    __resource_type__: str
    action: list[fhirtypes.RequestGroupActionType] | None
    author: fhirtypes.ReferenceType | None
    authoredOn: fhirtypes.DateTimeType | None
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    code: fhirtypes.CodeableConceptType | None
    encounter: fhirtypes.ReferenceType | None
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
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    replaces: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class RequestGroupAction(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.RequestGroupActionType] | None
    cardinalityBehavior: fhirtypes.CodeType | None
    cardinalityBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    code: list[fhirtypes.CodeableConceptType] | None
    condition: list[fhirtypes.RequestGroupActionConditionType] | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    documentation: list[fhirtypes.RelatedArtifactType] | None
    groupingBehavior: fhirtypes.CodeType | None
    groupingBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    participant: list[fhirtypes.ReferenceType] | None
    precheckBehavior: fhirtypes.CodeType | None
    precheckBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    prefix: fhirtypes.StringType | None
    prefix__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relatedAction: list[fhirtypes.RequestGroupActionRelatedActionType] | None
    requiredBehavior: fhirtypes.CodeType | None
    requiredBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resource: fhirtypes.ReferenceType | None
    selectionBehavior: fhirtypes.CodeType | None
    selectionBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    textEquivalent: fhirtypes.StringType | None
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
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class RequestGroupActionCondition(backboneelement.BackboneElement):
    __resource_type__: str
    expression: fhirtypes.ExpressionType | None
    kind: fhirtypes.CodeType | None
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class RequestGroupActionRelatedAction(backboneelement.BackboneElement):
    __resource_type__: str
    actionId: fhirtypes.IdType | None
    actionId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    offsetDuration: fhirtypes.DurationType | None
    offsetRange: fhirtypes.RangeType | None
    relationship: fhirtypes.CodeType | None
    relationship__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
