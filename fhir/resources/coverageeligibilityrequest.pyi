from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class CoverageEligibilityRequest(domainresource.DomainResource):
    __resource_type__: str
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    enterer: fhirtypes.ReferenceType | None
    event: list[fhirtypes.CoverageEligibilityRequestEventType] | None
    facility: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    insurance: list[fhirtypes.CoverageEligibilityRequestInsuranceType] | None
    insurer: fhirtypes.ReferenceType
    item: list[fhirtypes.CoverageEligibilityRequestItemType] | None
    patient: fhirtypes.ReferenceType
    priority: fhirtypes.CodeableConceptType | None
    provider: fhirtypes.ReferenceType | None
    purpose: list[fhirtypes.CodeType | None] | None
    purpose__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    servicedDate: fhirtypes.DateType | None
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    servicedPeriod: fhirtypes.PeriodType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    supportingInfo: list[fhirtypes.CoverageEligibilityRequestSupportingInfoType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class CoverageEligibilityRequestEvent(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    whenDateTime: fhirtypes.DateTimeType | None
    whenDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    whenPeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class CoverageEligibilityRequestInsurance(backboneelement.BackboneElement):
    __resource_type__: str
    businessArrangement: fhirtypes.StringType | None
    businessArrangement__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    coverage: fhirtypes.ReferenceType
    focal: bool | None
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class CoverageEligibilityRequestItem(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType | None
    detail: list[fhirtypes.ReferenceType] | None
    diagnosis: list[fhirtypes.CoverageEligibilityRequestItemDiagnosisType] | None
    facility: fhirtypes.ReferenceType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    productOrService: fhirtypes.CodeableConceptType | None
    provider: fhirtypes.ReferenceType | None
    quantity: fhirtypes.QuantityType | None
    supportingInfoSequence: list[fhirtypes.PositiveIntType | None] | None
    supportingInfoSequence__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...

class CoverageEligibilityRequestItemDiagnosis(backboneelement.BackboneElement):
    __resource_type__: str
    diagnosisCodeableConcept: fhirtypes.CodeableConceptType | None
    diagnosisReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class CoverageEligibilityRequestSupportingInfo(backboneelement.BackboneElement):
    __resource_type__: str
    appliesToAll: bool | None
    appliesToAll__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    information: fhirtypes.ReferenceType
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
