from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class CoverageEligibilityResponse(domainresource.DomainResource):
    __resource_type__: str
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    disposition: fhirtypes.StringType | None
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    error: list[fhirtypes.CoverageEligibilityResponseErrorType] | None
    form: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    insurance: list[fhirtypes.CoverageEligibilityResponseInsuranceType] | None
    insurer: fhirtypes.ReferenceType
    outcome: fhirtypes.CodeType | None
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patient: fhirtypes.ReferenceType
    preAuthRef: fhirtypes.StringType | None
    preAuthRef__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: list[fhirtypes.CodeType | None] | None
    purpose__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    request: fhirtypes.ReferenceType
    requestor: fhirtypes.ReferenceType | None
    servicedDate: fhirtypes.DateType | None
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    servicedPeriod: fhirtypes.PeriodType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class CoverageEligibilityResponseError(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class CoverageEligibilityResponseInsurance(backboneelement.BackboneElement):
    __resource_type__: str
    benefitPeriod: fhirtypes.PeriodType | None
    coverage: fhirtypes.ReferenceType
    inforce: bool | None
    inforce__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    item: list[fhirtypes.CoverageEligibilityResponseInsuranceItemType] | None
    @classmethod
    def elements_sequence(cls): ...

class CoverageEligibilityResponseInsuranceItem(backboneelement.BackboneElement):
    __resource_type__: str
    authorizationRequired: bool | None
    authorizationRequired__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    authorizationSupporting: list[fhirtypes.CodeableConceptType] | None
    authorizationUrl: fhirtypes.UriType | None
    authorizationUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    benefit: list[fhirtypes.CoverageEligibilityResponseInsuranceItemBenefitType] | None
    category: fhirtypes.CodeableConceptType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    excluded: bool | None
    excluded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    network: fhirtypes.CodeableConceptType | None
    productOrService: fhirtypes.CodeableConceptType | None
    provider: fhirtypes.ReferenceType | None
    term: fhirtypes.CodeableConceptType | None
    unit: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class CoverageEligibilityResponseInsuranceItemBenefit(backboneelement.BackboneElement):
    __resource_type__: str
    allowedMoney: fhirtypes.MoneyType | None
    allowedString: fhirtypes.StringType | None
    allowedString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    allowedUnsignedInt: fhirtypes.UnsignedIntType | None
    allowedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    usedMoney: fhirtypes.MoneyType | None
    usedString: fhirtypes.StringType | None
    usedString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    usedUnsignedInt: fhirtypes.UnsignedIntType | None
    usedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
