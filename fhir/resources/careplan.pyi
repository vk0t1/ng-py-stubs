from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class CarePlan(domainresource.DomainResource):
    __resource_type__: str
    activity: list[fhirtypes.CarePlanActivityType] | None
    addresses: list[fhirtypes.CodeableReferenceType] | None
    basedOn: list[fhirtypes.ReferenceType] | None
    careTeam: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    contributor: list[fhirtypes.ReferenceType] | None
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    custodian: fhirtypes.ReferenceType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    goal: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    instantiatesCanonical: list[fhirtypes.CanonicalType | None] | None
    instantiatesCanonical__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    instantiatesUri: list[fhirtypes.UriType | None] | None
    instantiatesUri__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
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
    performedActivity: list[fhirtypes.CodeableReferenceType] | None
    plannedActivityReference: fhirtypes.ReferenceType | None
    progress: list[fhirtypes.AnnotationType] | None
    @classmethod
    def elements_sequence(cls): ...
