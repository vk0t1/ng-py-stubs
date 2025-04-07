from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Claim(domainresource.DomainResource):
    __resource_type__: str
    accident: fhirtypes.ClaimAccidentType | None
    billablePeriod: fhirtypes.PeriodType | None
    careTeam: list[fhirtypes.ClaimCareTeamType] | None
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    diagnosis: list[fhirtypes.ClaimDiagnosisType] | None
    diagnosisRelatedGroup: fhirtypes.CodeableConceptType | None
    encounter: list[fhirtypes.ReferenceType] | None
    enterer: fhirtypes.ReferenceType | None
    event: list[fhirtypes.ClaimEventType] | None
    facility: fhirtypes.ReferenceType | None
    fundsReserve: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    insurance: list[fhirtypes.ClaimInsuranceType] | None
    insurer: fhirtypes.ReferenceType | None
    item: list[fhirtypes.ClaimItemType] | None
    originalPrescription: fhirtypes.ReferenceType | None
    patient: fhirtypes.ReferenceType
    patientPaid: fhirtypes.MoneyType | None
    payee: fhirtypes.ClaimPayeeType | None
    prescription: fhirtypes.ReferenceType | None
    priority: fhirtypes.CodeableConceptType | None
    procedure: list[fhirtypes.ClaimProcedureType] | None
    provider: fhirtypes.ReferenceType | None
    referral: fhirtypes.ReferenceType | None
    related: list[fhirtypes.ClaimRelatedType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subType: fhirtypes.CodeableConceptType | None
    supportingInfo: list[fhirtypes.ClaimSupportingInfoType] | None
    total: fhirtypes.MoneyType | None
    traceNumber: list[fhirtypes.IdentifierType] | None
    type: fhirtypes.CodeableConceptType
    use: fhirtypes.CodeType | None
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimAccident(backboneelement.BackboneElement):
    __resource_type__: str
    date: fhirtypes.DateType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    locationAddress: fhirtypes.AddressType | None
    locationReference: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ClaimCareTeam(backboneelement.BackboneElement):
    __resource_type__: str
    provider: fhirtypes.ReferenceType
    responsible: bool | None
    responsible__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    role: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    specialty: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimDiagnosis(backboneelement.BackboneElement):
    __resource_type__: str
    diagnosisCodeableConcept: fhirtypes.CodeableConceptType | None
    diagnosisReference: fhirtypes.ReferenceType | None
    onAdmission: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ClaimEvent(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    whenDateTime: fhirtypes.DateTimeType | None
    whenDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    whenPeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ClaimInsurance(backboneelement.BackboneElement):
    __resource_type__: str
    businessArrangement: fhirtypes.StringType | None
    businessArrangement__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    claimResponse: fhirtypes.ReferenceType | None
    coverage: fhirtypes.ReferenceType
    focal: bool | None
    focal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    preAuthRef: list[fhirtypes.StringType | None] | None
    preAuthRef__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimItem(backboneelement.BackboneElement):
    __resource_type__: str
    bodySite: list[fhirtypes.ClaimItemBodySiteType] | None
    careTeamSequence: list[fhirtypes.PositiveIntType | None] | None
    careTeamSequence__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    category: fhirtypes.CodeableConceptType | None
    detail: list[fhirtypes.ClaimItemDetailType] | None
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
    patientPaid: fhirtypes.MoneyType | None
    procedureSequence: list[fhirtypes.PositiveIntType | None] | None
    procedureSequence__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    productOrService: fhirtypes.CodeableConceptType | None
    productOrServiceEnd: fhirtypes.CodeableConceptType | None
    programCode: list[fhirtypes.CodeableConceptType] | None
    quantity: fhirtypes.QuantityType | None
    request: list[fhirtypes.ReferenceType] | None
    revenue: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    servicedDate: fhirtypes.DateType | None
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    servicedPeriod: fhirtypes.PeriodType | None
    tax: fhirtypes.MoneyType | None
    traceNumber: list[fhirtypes.IdentifierType] | None
    udi: list[fhirtypes.ReferenceType] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ClaimItemBodySite(backboneelement.BackboneElement):
    __resource_type__: str
    site: list[fhirtypes.CodeableReferenceType]
    subSite: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimItemDetail(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    net: fhirtypes.MoneyType | None
    patientPaid: fhirtypes.MoneyType | None
    productOrService: fhirtypes.CodeableConceptType | None
    productOrServiceEnd: fhirtypes.CodeableConceptType | None
    programCode: list[fhirtypes.CodeableConceptType] | None
    quantity: fhirtypes.QuantityType | None
    revenue: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subDetail: list[fhirtypes.ClaimItemDetailSubDetailType] | None
    tax: fhirtypes.MoneyType | None
    traceNumber: list[fhirtypes.IdentifierType] | None
    udi: list[fhirtypes.ReferenceType] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    net: fhirtypes.MoneyType | None
    patientPaid: fhirtypes.MoneyType | None
    productOrService: fhirtypes.CodeableConceptType | None
    productOrServiceEnd: fhirtypes.CodeableConceptType | None
    programCode: list[fhirtypes.CodeableConceptType] | None
    quantity: fhirtypes.QuantityType | None
    revenue: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    tax: fhirtypes.MoneyType | None
    traceNumber: list[fhirtypes.IdentifierType] | None
    udi: list[fhirtypes.ReferenceType] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimPayee(backboneelement.BackboneElement):
    __resource_type__: str
    party: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class ClaimProcedure(backboneelement.BackboneElement):
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

class ClaimRelated(backboneelement.BackboneElement):
    __resource_type__: str
    claim: fhirtypes.ReferenceType | None
    reference: fhirtypes.IdentifierType | None
    relationship: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ClaimSupportingInfo(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType
    code: fhirtypes.CodeableConceptType | None
    reason: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingDate: fhirtypes.DateType | None
    timingDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timingPeriod: fhirtypes.PeriodType | None
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueIdentifier: fhirtypes.IdentifierType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueReference: fhirtypes.ReferenceType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
