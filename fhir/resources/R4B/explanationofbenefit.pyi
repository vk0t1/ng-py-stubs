from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ExplanationOfBenefit(domainresource.DomainResource):
    __resource_type__: str
    accident: fhirtypes.ExplanationOfBenefitAccidentType | None
    addItem: list[fhirtypes.ExplanationOfBenefitAddItemType] | None
    adjudication: list[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None
    benefitBalance: list[fhirtypes.ExplanationOfBenefitBenefitBalanceType] | None
    benefitPeriod: fhirtypes.PeriodType | None
    billablePeriod: fhirtypes.PeriodType | None
    careTeam: list[fhirtypes.ExplanationOfBenefitCareTeamType] | None
    claim: fhirtypes.ReferenceType | None
    claimResponse: fhirtypes.ReferenceType | None
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    diagnosis: list[fhirtypes.ExplanationOfBenefitDiagnosisType] | None
    disposition: fhirtypes.StringType | None
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    enterer: fhirtypes.ReferenceType | None
    facility: fhirtypes.ReferenceType | None
    form: fhirtypes.AttachmentType | None
    formCode: fhirtypes.CodeableConceptType | None
    fundsReserve: fhirtypes.CodeableConceptType | None
    fundsReserveRequested: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    insurance: list[fhirtypes.ExplanationOfBenefitInsuranceType]
    insurer: fhirtypes.ReferenceType
    item: list[fhirtypes.ExplanationOfBenefitItemType] | None
    originalPrescription: fhirtypes.ReferenceType | None
    outcome: fhirtypes.CodeType | None
    outcome__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patient: fhirtypes.ReferenceType
    payee: fhirtypes.ExplanationOfBenefitPayeeType | None
    payment: fhirtypes.ExplanationOfBenefitPaymentType | None
    preAuthRef: list[fhirtypes.StringType | None] | None
    preAuthRef__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    preAuthRefPeriod: list[fhirtypes.PeriodType] | None
    precedence: fhirtypes.PositiveIntType | None
    precedence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    prescription: fhirtypes.ReferenceType | None
    priority: fhirtypes.CodeableConceptType | None
    procedure: list[fhirtypes.ExplanationOfBenefitProcedureType] | None
    processNote: list[fhirtypes.ExplanationOfBenefitProcessNoteType] | None
    provider: fhirtypes.ReferenceType
    referral: fhirtypes.ReferenceType | None
    related: list[fhirtypes.ExplanationOfBenefitRelatedType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subType: fhirtypes.CodeableConceptType | None
    supportingInfo: list[fhirtypes.ExplanationOfBenefitSupportingInfoType] | None
    total: list[fhirtypes.ExplanationOfBenefitTotalType] | None
    type: fhirtypes.CodeableConceptType
    use: fhirtypes.CodeType | None
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExplanationOfBenefitAccident(backboneelement.BackboneElement):
    __resource_type__: str
    date: fhirtypes.DateType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    locationAddress: fhirtypes.AddressType | None
    locationReference: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ExplanationOfBenefitAddItem(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None
    bodySite: fhirtypes.CodeableConceptType | None
    detail: list[fhirtypes.ExplanationOfBenefitAddItemDetailType] | None
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
    productOrService: fhirtypes.CodeableConceptType
    programCode: list[fhirtypes.CodeableConceptType] | None
    provider: list[fhirtypes.ReferenceType] | None
    quantity: fhirtypes.QuantityType | None
    servicedDate: fhirtypes.DateType | None
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    servicedPeriod: fhirtypes.PeriodType | None
    subDetailSequence: list[fhirtypes.PositiveIntType | None] | None
    subDetailSequence__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    subSite: list[fhirtypes.CodeableConceptType] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ExplanationOfBenefitAddItemDetail(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    net: fhirtypes.MoneyType | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    productOrService: fhirtypes.CodeableConceptType
    quantity: fhirtypes.QuantityType | None
    subDetail: list[fhirtypes.ExplanationOfBenefitAddItemDetailSubDetailType] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...

class ExplanationOfBenefitAddItemDetailSubDetail(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    net: fhirtypes.MoneyType | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    productOrService: fhirtypes.CodeableConceptType
    quantity: fhirtypes.QuantityType | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...

class ExplanationOfBenefitBenefitBalance(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    excluded: bool | None
    excluded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    financial: list[fhirtypes.ExplanationOfBenefitBenefitBalanceFinancialType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    network: fhirtypes.CodeableConceptType | None
    term: fhirtypes.CodeableConceptType | None
    unit: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ExplanationOfBenefitBenefitBalanceFinancial(backboneelement.BackboneElement):
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

class ExplanationOfBenefitCareTeam(backboneelement.BackboneElement):
    __resource_type__: str
    provider: fhirtypes.ReferenceType
    qualification: fhirtypes.CodeableConceptType | None
    responsible: bool | None
    responsible__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    role: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    __resource_type__: str
    diagnosisCodeableConcept: fhirtypes.CodeableConceptType | None
    diagnosisReference: fhirtypes.ReferenceType | None
    onAdmission: fhirtypes.CodeableConceptType | None
    packageCode: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ExplanationOfBenefitInsurance(backboneelement.BackboneElement):
    __resource_type__: str
    coverage: fhirtypes.ReferenceType
    focal: bool | None
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    preAuthRef: list[fhirtypes.StringType | None] | None
    preAuthRef__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExplanationOfBenefitItem(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None
    bodySite: fhirtypes.CodeableConceptType | None
    careTeamSequence: list[fhirtypes.PositiveIntType | None] | None
    careTeamSequence__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    category: fhirtypes.CodeableConceptType | None
    detail: list[fhirtypes.ExplanationOfBenefitItemDetailType] | None
    diagnosisSequence: list[fhirtypes.PositiveIntType | None] | None
    diagnosisSequence__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    encounter: list[fhirtypes.ReferenceType] | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    informationSequence: list[fhirtypes.PositiveIntType | None] | None
    informationSequence__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    locationAddress: fhirtypes.AddressType | None
    locationCodeableConcept: fhirtypes.CodeableConceptType | None
    locationReference: fhirtypes.ReferenceType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    net: fhirtypes.MoneyType | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    procedureSequence: list[fhirtypes.PositiveIntType | None] | None
    procedureSequence__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    productOrService: fhirtypes.CodeableConceptType
    programCode: list[fhirtypes.CodeableConceptType] | None
    quantity: fhirtypes.QuantityType | None
    revenue: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    servicedDate: fhirtypes.DateType | None
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    servicedPeriod: fhirtypes.PeriodType | None
    subSite: list[fhirtypes.CodeableConceptType] | None
    udi: list[fhirtypes.ReferenceType] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ExplanationOfBenefitItemAdjudication(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.MoneyType | None
    category: fhirtypes.CodeableConceptType
    reason: fhirtypes.CodeableConceptType | None
    value: fhirtypes.DecimalType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ExplanationOfBenefitItemDetail(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None
    category: fhirtypes.CodeableConceptType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    net: fhirtypes.MoneyType | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    productOrService: fhirtypes.CodeableConceptType
    programCode: list[fhirtypes.CodeableConceptType] | None
    quantity: fhirtypes.QuantityType | None
    revenue: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subDetail: list[fhirtypes.ExplanationOfBenefitItemDetailSubDetailType] | None
    udi: list[fhirtypes.ReferenceType] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    __resource_type__: str
    adjudication: list[fhirtypes.ExplanationOfBenefitItemAdjudicationType] | None
    category: fhirtypes.CodeableConceptType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    net: fhirtypes.MoneyType | None
    noteNumber: list[fhirtypes.PositiveIntType | None] | None
    noteNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    productOrService: fhirtypes.CodeableConceptType
    programCode: list[fhirtypes.CodeableConceptType] | None
    quantity: fhirtypes.QuantityType | None
    revenue: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    udi: list[fhirtypes.ReferenceType] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    __resource_type__: str
    party: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ExplanationOfBenefitPayment(backboneelement.BackboneElement):
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

class ExplanationOfBenefitProcedure(backboneelement.BackboneElement):
    __resource_type__: str
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    procedureCodeableConcept: fhirtypes.CodeableConceptType | None
    procedureReference: fhirtypes.ReferenceType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodeableConceptType] | None
    udi: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ExplanationOfBenefitProcessNote(backboneelement.BackboneElement):
    __resource_type__: str
    language: fhirtypes.CodeableConceptType | None
    number: fhirtypes.PositiveIntType | None
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ExplanationOfBenefitRelated(backboneelement.BackboneElement):
    __resource_type__: str
    claim: fhirtypes.ReferenceType | None
    reference: fhirtypes.IdentifierType | None
    relationship: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ExplanationOfBenefitSupportingInfo(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType
    code: fhirtypes.CodeableConceptType | None
    reason: fhirtypes.CodingType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingDate: fhirtypes.DateType | None
    timingDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingPeriod: fhirtypes.PeriodType | None
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueReference: fhirtypes.ReferenceType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ExplanationOfBenefitTotal(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.MoneyType
    category: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
