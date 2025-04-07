from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class InsurancePlan(domainresource.DomainResource):
    __resource_type__: str
    administeredBy: fhirtypes.ReferenceType | None
    alias: list[fhirtypes.StringType | None] | None
    alias__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    contact: list[fhirtypes.ExtendedContactDetailType] | None
    coverage: list[fhirtypes.InsurancePlanCoverageType] | None
    coverageArea: list[fhirtypes.ReferenceType] | None
    endpoint: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    network: list[fhirtypes.ReferenceType] | None
    ownedBy: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    plan: list[fhirtypes.InsurancePlanPlanType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class InsurancePlanCoverage(backboneelement.BackboneElement):
    __resource_type__: str
    benefit: list[fhirtypes.InsurancePlanCoverageBenefitType]
    network: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class InsurancePlanCoverageBenefit(backboneelement.BackboneElement):
    __resource_type__: str
    limit: list[fhirtypes.InsurancePlanCoverageBenefitLimitType] | None
    requirement: fhirtypes.StringType | None
    requirement__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class InsurancePlanCoverageBenefitLimit(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    value: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...

class InsurancePlanPlan(backboneelement.BackboneElement):
    __resource_type__: str
    coverageArea: list[fhirtypes.ReferenceType] | None
    generalCost: list[fhirtypes.InsurancePlanPlanGeneralCostType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    network: list[fhirtypes.ReferenceType] | None
    specificCost: list[fhirtypes.InsurancePlanPlanSpecificCostType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class InsurancePlanPlanGeneralCost(backboneelement.BackboneElement):
    __resource_type__: str
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    cost: fhirtypes.MoneyType | None
    groupSize: fhirtypes.PositiveIntType | None
    groupSize__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class InsurancePlanPlanSpecificCost(backboneelement.BackboneElement):
    __resource_type__: str
    benefit: list[fhirtypes.InsurancePlanPlanSpecificCostBenefitType] | None
    category: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class InsurancePlanPlanSpecificCostBenefit(backboneelement.BackboneElement):
    __resource_type__: str
    cost: list[fhirtypes.InsurancePlanPlanSpecificCostBenefitCostType] | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class InsurancePlanPlanSpecificCostBenefitCost(backboneelement.BackboneElement):
    __resource_type__: str
    applicability: fhirtypes.CodeableConceptType | None
    qualifiers: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType
    value: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
