from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Goal(domainresource.DomainResource):
    __resource_type__: str
    achievementStatus: fhirtypes.CodeableConceptType | None
    addresses: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    continuous: bool | None
    continuous__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.CodeableConceptType
    identifier: list[fhirtypes.IdentifierType] | None
    lifecycleStatus: fhirtypes.CodeType | None
    lifecycleStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    outcome: list[fhirtypes.CodeableReferenceType] | None
    priority: fhirtypes.CodeableConceptType | None
    source: fhirtypes.ReferenceType | None
    startCodeableConcept: fhirtypes.CodeableConceptType | None
    startDate: fhirtypes.DateType | None
    startDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusDate: fhirtypes.DateType | None
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.StringType | None
    statusReason__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    target: list[fhirtypes.GoalTargetType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class GoalTarget(backboneelement.BackboneElement):
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
    dueDate: fhirtypes.DateType | None
    dueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dueDuration: fhirtypes.DurationType | None
    measure: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
