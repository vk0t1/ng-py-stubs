from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class EligibilityResponse(domainresource.DomainResource):
    __resource_type__: str
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    disposition: fhirtypes.StringType | None
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    error: list[fhirtypes.EligibilityResponseErrorType] | None
    form: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    inforce: bool | None
    inforce__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    insurance: list[fhirtypes.EligibilityResponseInsuranceType] | None
    insurer: fhirtypes.ReferenceType | None
    outcome: fhirtypes.CodeableConceptType | None
    request: fhirtypes.ReferenceType | None
    requestOrganization: fhirtypes.ReferenceType | None
    requestProvider: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class EligibilityResponseError(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class EligibilityResponseInsurance(backboneelement.BackboneElement):
    __resource_type__: str
    benefitBalance: list[fhirtypes.EligibilityResponseInsuranceBenefitBalanceType] | None
    contract: fhirtypes.ReferenceType | None
    coverage: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class EligibilityResponseInsuranceBenefitBalance(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    excluded: bool | None
    excluded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    financial: list[fhirtypes.EligibilityResponseInsuranceBenefitBalanceFinancialType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    network: fhirtypes.CodeableConceptType | None
    subCategory: fhirtypes.CodeableConceptType | None
    term: fhirtypes.CodeableConceptType | None
    unit: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class EligibilityResponseInsuranceBenefitBalanceFinancial(backboneelement.BackboneElement):
    __resource_type__: str
    allowedMoney: fhirtypes.MoneyType | None
    allowedString: fhirtypes.StringType | None
    allowedString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    allowedUnsignedInt: fhirtypes.UnsignedIntType | None
    allowedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    usedMoney: fhirtypes.MoneyType | None
    usedUnsignedInt: fhirtypes.UnsignedIntType | None
    usedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
