from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ClaimResponse(domainresource.DomainResource):
    __resource_type__: str
    addItem: list[fhirtypes.ClaimResponseAddItemType] | None
    adjudication: list[fhirtypes.ClaimResponseItemAdjudicationType] | None
    communicationRequest: list[fhirtypes.ReferenceType] | None
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    decision: fhirtypes.CodeableConceptType | None
    diagnosisRelatedGroup: fhirtypes.CodeableConceptType | None
    disposition: fhirtypes.StringType | None
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: list[fhirtypes.ReferenceType] | None
    error: list[fhirtypes.ClaimResponseErrorType] | None
    event: list[fhirtypes.ClaimResponseEventType] | None
    form: fhirtypes.AttachmentType | None
    formCode: fhirtypes.CodeableConceptType | None
    fundsReserve: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    insurance: list[fhirtypes.ClaimResponseInsuranceType] | None
    insurer: fhirtypes.ReferenceType | None
    item: list[fhirtypes.ClaimResponseItemType] | None
    outcome: fhirtypes.CodeType | None
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patient: fhirtypes.ReferenceType
    payeeType: fhirtypes.CodeableConceptType | None
    payment: fhirtypes.ClaimResponsePaymentType | None
    preAuthPeriod: fhirtypes.PeriodType | None
    preAuthRef: fhirtypes.StringType | None
    preAuthRef__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    processNote: list[fhirtypes.ClaimResponseProcessNoteType] | None
    request: fhirtypes.ReferenceType | None
    requestor: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subType: fhirtypes.CodeableConceptType | None
    total: list[fhirtypes.ClaimResponseTotalType] | None
    traceNumber: list[fhirtypes.IdentifierType] | None
    type: fhirtypes.CodeableConceptType
    use: fhirtypes.CodeType | None
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimResponseAddItem(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ClaimResponseItemAdjudicationType] | None
    bodySite: list[fhirtypes.ClaimResponseAddItemBodySiteType] | None
    detail: list[fhirtypes.ClaimResponseAddItemDetailType] | None
    detailSequence: list[fhirtypes.PositiveIntType | None] | None
    detailSequence__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    itemSequence: list[fhirtypes.PositiveIntType | None] | None
    itemSequence__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    locationAddress: fhirtypes.AddressType | None
    locationCodeableConcept: fhirtypes.CodeableConceptType | None
    locationReference: fhirtypes.ReferenceType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    net: fhirtypes.MoneyType | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    productOrService: fhirtypes.CodeableConceptType | None
    productOrServiceEnd: fhirtypes.CodeableConceptType | None
    programCode: list[fhirtypes.CodeableConceptType] | None
    provider: list[fhirtypes.ReferenceType] | None
    quantity: fhirtypes.QuantityType | None
    request: list[fhirtypes.ReferenceType] | None
    revenue: fhirtypes.CodeableConceptType | None
    reviewOutcome: fhirtypes.ClaimResponseItemReviewOutcomeType | None
    servicedDate: fhirtypes.DateType | None
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    servicedPeriod: fhirtypes.PeriodType | None
    subdetailSequence: list[fhirtypes.PositiveIntType | None] | None
    subdetailSequence__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    tax: fhirtypes.MoneyType | None
    traceNumber: list[fhirtypes.IdentifierType] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ClaimResponseAddItemBodySite(backboneelement.BackboneElement):
    __resource_type__: str
    site: list[fhirtypes.CodeableReferenceType]
    subSite: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ClaimResponseItemAdjudicationType] | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    net: fhirtypes.MoneyType | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    productOrService: fhirtypes.CodeableConceptType | None
    productOrServiceEnd: fhirtypes.CodeableConceptType | None
    quantity: fhirtypes.QuantityType | None
    revenue: fhirtypes.CodeableConceptType | None
    reviewOutcome: fhirtypes.ClaimResponseItemReviewOutcomeType | None
    subDetail: list[fhirtypes.ClaimResponseAddItemDetailSubDetailType] | None
    tax: fhirtypes.MoneyType | None
    traceNumber: list[fhirtypes.IdentifierType] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimResponseAddItemDetailSubDetail(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ClaimResponseItemAdjudicationType] | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    net: fhirtypes.MoneyType | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    productOrService: fhirtypes.CodeableConceptType | None
    productOrServiceEnd: fhirtypes.CodeableConceptType | None
    quantity: fhirtypes.QuantityType | None
    revenue: fhirtypes.CodeableConceptType | None
    reviewOutcome: fhirtypes.ClaimResponseItemReviewOutcomeType | None
    tax: fhirtypes.MoneyType | None
    traceNumber: list[fhirtypes.IdentifierType] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimResponseError(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    detailSequence: fhirtypes.PositiveIntType | None
    detailSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    expression: list[fhirtypes.StringType | None] | None
    expression__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    itemSequence: fhirtypes.PositiveIntType | None
    itemSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subDetailSequence: fhirtypes.PositiveIntType | None
    subDetailSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimResponseEvent(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    whenDateTime: fhirtypes.DateTimeType | None
    whenDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    whenPeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ClaimResponseInsurance(backboneelement.BackboneElement):
    __resource_type__: str
    businessArrangement: fhirtypes.StringType | None
    businessArrangement__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    claimResponse: fhirtypes.ReferenceType | None
    coverage: fhirtypes.ReferenceType
    focal: bool | None
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimResponseItem(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ClaimResponseItemAdjudicationType] | None
    detail: list[fhirtypes.ClaimResponseItemDetailType] | None
    itemSequence: fhirtypes.PositiveIntType | None
    itemSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    reviewOutcome: fhirtypes.ClaimResponseItemReviewOutcomeType | None
    traceNumber: list[fhirtypes.IdentifierType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.MoneyType | None
    category: fhirtypes.CodeableConceptType
    quantity: fhirtypes.QuantityType | None
    reason: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimResponseItemDetail(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ClaimResponseItemAdjudicationType] | None
    detailSequence: fhirtypes.PositiveIntType | None
    detailSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    reviewOutcome: fhirtypes.ClaimResponseItemReviewOutcomeType | None
    subDetail: list[fhirtypes.ClaimResponseItemDetailSubDetailType] | None
    traceNumber: list[fhirtypes.IdentifierType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ClaimResponseItemAdjudicationType] | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    reviewOutcome: fhirtypes.ClaimResponseItemReviewOutcomeType | None
    subDetailSequence: fhirtypes.PositiveIntType | None
    subDetailSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    traceNumber: list[fhirtypes.IdentifierType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimResponseItemReviewOutcome(backboneelement.BackboneElement):
    __resource_type__: str
    decision: fhirtypes.CodeableConceptType | None
    preAuthPeriod: fhirtypes.PeriodType | None
    preAuthRef: fhirtypes.StringType | None
    preAuthRef__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reason: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimResponsePayment(backboneelement.BackboneElement):
    __resource_type__: str
    adjustment: fhirtypes.MoneyType | None
    adjustmentReason: fhirtypes.CodeableConceptType | None
    amount: fhirtypes.MoneyType
    date: fhirtypes.DateType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    type: fhirtypes.CodeableConceptType
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
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimResponseTotal(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.MoneyType
    category: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
