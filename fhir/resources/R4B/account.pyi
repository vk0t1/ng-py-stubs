from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Account(domainresource.DomainResource):
    __resource_type__: str
    coverage: list[fhirtypes.AccountCoverageType] | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    guarantor: list[fhirtypes.AccountGuarantorType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    owner: fhirtypes.ReferenceType | None
    partOf: fhirtypes.ReferenceType | None
    servicePeriod: fhirtypes.PeriodType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

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
