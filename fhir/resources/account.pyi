from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Account(domainresource.DomainResource):
    __resource_type__: str
    balance: list[fhirtypes.AccountBalanceType] | None
    billingStatus: fhirtypes.CodeableConceptType | None
    calculatedAt: fhirtypes.InstantType | None
    calculatedAt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    coverage: list[fhirtypes.AccountCoverageType] | None
    currency: fhirtypes.CodeableConceptType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    diagnosis: list[fhirtypes.AccountDiagnosisType] | None
    guarantor: list[fhirtypes.AccountGuarantorType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    owner: fhirtypes.ReferenceType | None
    procedure: list[fhirtypes.AccountProcedureType] | None
    relatedAccount: list[fhirtypes.AccountRelatedAccountType] | None
    servicePeriod: fhirtypes.PeriodType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class AccountBalance(backboneelement.BackboneElement):
    __resource_type__: str
    aggregate: fhirtypes.CodeableConceptType | None
    amount: fhirtypes.MoneyType
    estimate: bool | None
    estimate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    term: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class AccountCoverage(backboneelement.BackboneElement):
    __resource_type__: str
    coverage: fhirtypes.ReferenceType
    priority: fhirtypes.PositiveIntType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class AccountDiagnosis(backboneelement.BackboneElement):
    __resource_type__: str
    condition: fhirtypes.CodeableReferenceType
    dateOfDiagnosis: fhirtypes.DateTimeType | None
    dateOfDiagnosis__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    onAdmission: bool | None
    onAdmission__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    packageCode: list[fhirtypes.CodeableConceptType] | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class AccountGuarantor(backboneelement.BackboneElement):
    __resource_type__: str
    onHold: bool | None
    onHold__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    party: fhirtypes.ReferenceType
    period: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...

class AccountProcedure(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableReferenceType
    dateOfService: fhirtypes.DateTimeType | None
    dateOfService__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    device: list[fhirtypes.ReferenceType] | None
    packageCode: list[fhirtypes.CodeableConceptType] | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class AccountRelatedAccount(backboneelement.BackboneElement):
    __resource_type__: str
    account: fhirtypes.ReferenceType
    relationship: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
