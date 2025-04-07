from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Account(domainresource.DomainResource):
    __resource_type__: str
    active: fhirtypes.PeriodType | None
    balance: fhirtypes.MoneyType | None
    coverage: list[fhirtypes.AccountCoverageType] | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    guarantor: list[fhirtypes.AccountGuarantorType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    owner: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class AccountCoverage(backboneelement.BackboneElement):
    __resource_type__: str
    coverage: fhirtypes.ReferenceType
    priority: fhirtypes.PositiveIntType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
