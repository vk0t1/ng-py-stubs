from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Coverage(domainresource.DomainResource):
    __resource_type__: str
    beneficiary: fhirtypes.ReferenceType
    class_fhir: list[fhirtypes.CoverageClassType] | None
    contract: list[fhirtypes.ReferenceType] | None
    costToBeneficiary: list[fhirtypes.CoverageCostToBeneficiaryType] | None
    dependent: fhirtypes.StringType | None
    dependent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    insurancePlan: fhirtypes.ReferenceType | None
    insurer: fhirtypes.ReferenceType | None
    kind: fhirtypes.CodeType | None
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    network: fhirtypes.StringType | None
    network__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    order: fhirtypes.PositiveIntType | None
    order__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    paymentBy: list[fhirtypes.CoveragePaymentByType] | None
    period: fhirtypes.PeriodType | None
    policyHolder: fhirtypes.ReferenceType | None
    relationship: fhirtypes.CodeableConceptType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subrogation: bool | None
    subrogation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subscriber: fhirtypes.ReferenceType | None
    subscriberId: list[fhirtypes.IdentifierType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CoverageClass(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    value: fhirtypes.IdentifierType
    @classmethod
    def elements_sequence(cls): ...

class CoverageCostToBeneficiary(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType | None
    exception: list[fhirtypes.CoverageCostToBeneficiaryExceptionType] | None
    network: fhirtypes.CodeableConceptType | None
    term: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeableConceptType | None
    unit: fhirtypes.CodeableConceptType | None
    valueMoney: fhirtypes.MoneyType | None
    valueQuantity: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class CoverageCostToBeneficiaryException(backboneelement.BackboneElement):
    __resource_type__: str
    period: fhirtypes.PeriodType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class CoveragePaymentBy(backboneelement.BackboneElement):
    __resource_type__: str
    party: fhirtypes.ReferenceType
    responsibility: fhirtypes.StringType | None
    responsibility__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
