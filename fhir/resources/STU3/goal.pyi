from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Goal(domainresource.DomainResource):
    __resource_type__: str
    addresses: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    description: fhirtypes.CodeableConceptType
    expressedBy: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    note: list[fhirtypes.AnnotationType] | None
    outcomeCode: list[fhirtypes.CodeableConceptType] | None
    outcomeReference: list[fhirtypes.ReferenceType] | None
    priority: fhirtypes.CodeableConceptType | None
    startCodeableConcept: fhirtypes.CodeableConceptType | None
    startDate: fhirtypes.DateType | None
    startDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusDate: fhirtypes.DateType | None
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.StringType | None
    statusReason__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    target: fhirtypes.GoalTargetType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class GoalTarget(backboneelement.BackboneElement):
    __resource_type__: str
    detailCodeableConcept: fhirtypes.CodeableConceptType | None
    detailQuantity: fhirtypes.QuantityType | None
    detailRange: fhirtypes.RangeType | None
    dueDate: fhirtypes.DateType | None
    dueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dueDuration: fhirtypes.DurationType | None
    measure: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
