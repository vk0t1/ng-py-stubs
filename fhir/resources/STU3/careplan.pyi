from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class CarePlan(domainresource.DomainResource):
    __resource_type__: str
    activity: list[fhirtypes.CarePlanActivityType] | None
    addresses: list[fhirtypes.ReferenceType] | None
    author: list[fhirtypes.ReferenceType] | None
    basedOn: list[fhirtypes.ReferenceType] | None
    careTeam: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    context: fhirtypes.ReferenceType | None
    definition: list[fhirtypes.ReferenceType] | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    goal: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    intent: fhirtypes.CodeType | None
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    period: fhirtypes.PeriodType | None
    replaces: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    supportingInfo: list[fhirtypes.ReferenceType] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CarePlanActivity(backboneelement.BackboneElement):
    __resource_type__: str
    detail: fhirtypes.CarePlanActivityDetailType | None
    outcomeCodeableConcept: list[fhirtypes.CodeableConceptType] | None
    outcomeReference: list[fhirtypes.ReferenceType] | None
    progress: list[fhirtypes.AnnotationType] | None
    reference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class CarePlanActivityDetail(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType | None
    code: fhirtypes.CodeableConceptType | None
    dailyAmount: fhirtypes.QuantityType | None
    definition: fhirtypes.ReferenceType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    goal: list[fhirtypes.ReferenceType] | None
    location: fhirtypes.ReferenceType | None
    performer: list[fhirtypes.ReferenceType] | None
    productCodeableConcept: fhirtypes.CodeableConceptType | None
    productReference: fhirtypes.ReferenceType | None
    prohibited: bool | None
    prohibited__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.QuantityType | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    scheduledPeriod: fhirtypes.PeriodType | None
    scheduledString: fhirtypes.StringType | None
    scheduledString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    scheduledTiming: fhirtypes.TimingType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.StringType | None
    statusReason__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
