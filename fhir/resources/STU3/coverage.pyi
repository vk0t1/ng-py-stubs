from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Coverage(domainresource.DomainResource):
    __resource_type__: str
    beneficiary: fhirtypes.ReferenceType | None
    contract: list[fhirtypes.ReferenceType] | None
    dependent: fhirtypes.StringType | None
    dependent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    grouping: fhirtypes.CoverageGroupingType | None
    identifier: list[fhirtypes.IdentifierType] | None
    network: fhirtypes.StringType | None
    network__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    order: fhirtypes.PositiveIntType | None
    order__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    payor: list[fhirtypes.ReferenceType] | None
    period: fhirtypes.PeriodType | None
    policyHolder: fhirtypes.ReferenceType | None
    relationship: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.StringType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subscriber: fhirtypes.ReferenceType | None
    subscriberId: fhirtypes.StringType | None
    subscriberId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class CoverageGrouping(backboneelement.BackboneElement):
    __resource_type__: str
    classDisplay: fhirtypes.StringType | None
    classDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    class_fhir: fhirtypes.StringType | None
    class__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    group: fhirtypes.StringType | None
    group__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    groupDisplay: fhirtypes.StringType | None
    groupDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    plan: fhirtypes.StringType | None
    plan__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    planDisplay: fhirtypes.StringType | None
    planDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subClass: fhirtypes.StringType | None
    subClass__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subClassDisplay: fhirtypes.StringType | None
    subClassDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subGroup: fhirtypes.StringType | None
    subGroup__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subGroupDisplay: fhirtypes.StringType | None
    subGroupDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subPlan: fhirtypes.StringType | None
    subPlan__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subPlanDisplay: fhirtypes.StringType | None
    subPlanDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
