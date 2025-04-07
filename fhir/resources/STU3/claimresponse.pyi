from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ClaimResponse(domainresource.DomainResource):
    __resource_type__: str
    addItem: list[fhirtypes.ClaimResponseAddItemType] | None
    communicationRequest: list[fhirtypes.ReferenceType] | None
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    disposition: fhirtypes.StringType | None
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    error: list[fhirtypes.ClaimResponseErrorType] | None
    form: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    insurance: list[fhirtypes.ClaimResponseInsuranceType] | None
    insurer: fhirtypes.ReferenceType | None
    item: list[fhirtypes.ClaimResponseItemType] | None
    outcome: fhirtypes.CodeableConceptType | None
    patient: fhirtypes.ReferenceType | None
    payeeType: fhirtypes.CodeableConceptType | None
    payment: fhirtypes.ClaimResponsePaymentType | None
    processNote: list[fhirtypes.ClaimResponseProcessNoteType] | None
    request: fhirtypes.ReferenceType | None
    requestOrganization: fhirtypes.ReferenceType | None
    requestProvider: fhirtypes.ReferenceType | None
    reserved: fhirtypes.CodingType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    totalBenefit: fhirtypes.MoneyType | None
    totalCost: fhirtypes.MoneyType | None
    unallocDeductable: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimResponseAddItem(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ClaimResponseItemAdjudicationType] | None
    category: fhirtypes.CodeableConceptType | None
    detail: list[fhirtypes.ClaimResponseAddItemDetailType] | None
    fee: fhirtypes.MoneyType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    revenue: fhirtypes.CodeableConceptType | None
    sequenceLinkId: list[fhirtypes.PositiveIntType | None] | None
    sequenceLinkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    service: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ClaimResponseItemAdjudicationType] | None
    category: fhirtypes.CodeableConceptType | None
    fee: fhirtypes.MoneyType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    revenue: fhirtypes.CodeableConceptType | None
    service: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimResponseError(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    detailSequenceLinkId: fhirtypes.PositiveIntType | None
    detailSequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sequenceLinkId: fhirtypes.PositiveIntType | None
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subdetailSequenceLinkId: fhirtypes.PositiveIntType | None
    subdetailSequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimResponseInsurance(backboneelement.BackboneElement):
    __resource_type__: str
    businessArrangement: fhirtypes.StringType | None
    businessArrangement__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    claimResponse: fhirtypes.ReferenceType | None
    coverage: fhirtypes.ReferenceType
    focal: bool | None
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    preAuthRef: list[fhirtypes.StringType | None] | None
    preAuthRef__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimResponseItem(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ClaimResponseItemAdjudicationType] | None
    detail: list[fhirtypes.ClaimResponseItemDetailType] | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    sequenceLinkId: fhirtypes.PositiveIntType | None
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.MoneyType | None
    category: fhirtypes.CodeableConceptType
    reason: fhirtypes.CodeableConceptType | None
    value: fhirtypes.DecimalType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimResponseItemDetail(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ClaimResponseItemAdjudicationType] | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    sequenceLinkId: fhirtypes.PositiveIntType | None
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subDetail: list[fhirtypes.ClaimResponseItemDetailSubDetailType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ClaimResponseItemAdjudicationType] | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    sequenceLinkId: fhirtypes.PositiveIntType | None
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimResponsePayment(backboneelement.BackboneElement):
    __resource_type__: str
    adjustment: fhirtypes.MoneyType | None
    adjustmentReason: fhirtypes.CodeableConceptType | None
    amount: fhirtypes.MoneyType | None
    date: fhirtypes.DateType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimResponseProcessNote(backboneelement.BackboneElement):
    __resource_type__: str
    language: fhirtypes.CodeableConceptType | None
    number: fhirtypes.PositiveIntType | None
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
