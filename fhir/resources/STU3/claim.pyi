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
    employmentImpacted: fhirtypes.PeriodType | None
    enterer: fhirtypes.ReferenceType | None
    facility: fhirtypes.ReferenceType | None
    fundsReserve: fhirtypes.CodeableConceptType | None
    hospitalization: fhirtypes.PeriodType | None
    identifier: list[fhirtypes.IdentifierType] | None
    information: list[fhirtypes.ClaimInformationType] | None
    insurance: list[fhirtypes.ClaimInsuranceType] | None
    insurer: fhirtypes.ReferenceType | None
    item: list[fhirtypes.ClaimItemType] | None
    organization: fhirtypes.ReferenceType | None
    originalPrescription: fhirtypes.ReferenceType | None
    patient: fhirtypes.ReferenceType | None
    payee: fhirtypes.ClaimPayeeType | None
    prescription: fhirtypes.ReferenceType | None
    priority: fhirtypes.CodeableConceptType | None
    procedure: list[fhirtypes.ClaimProcedureType] | None
    provider: fhirtypes.ReferenceType | None
    referral: fhirtypes.ReferenceType | None
    related: list[fhirtypes.ClaimRelatedType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subType: list[fhirtypes.CodeableConceptType] | None
    total: fhirtypes.MoneyType | None
    type: fhirtypes.CodeableConceptType | None
    use: fhirtypes.CodeType | None
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

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
    qualification: fhirtypes.CodeableConceptType | None
    responsible: bool | None
    responsible__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    role: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimDiagnosis(backboneelement.BackboneElement):
    __resource_type__: str
    diagnosisCodeableConcept: fhirtypes.CodeableConceptType | None
    diagnosisReference: fhirtypes.ReferenceType | None
    packageCode: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ClaimInformation(backboneelement.BackboneElement):
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
    valueQuantity: fhirtypes.QuantityType | None
    valueReference: fhirtypes.ReferenceType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ClaimInsurance(backboneelement.BackboneElement):
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

class ClaimItem(backboneelement.BackboneElement):
    __resource_type__: str
    bodySite: fhirtypes.CodeableConceptType | None
    careTeamLinkId: list[fhirtypes.PositiveIntType | None] | None
    careTeamLinkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    category: fhirtypes.CodeableConceptType | None
    detail: list[fhirtypes.ClaimItemDetailType] | None
    diagnosisLinkId: list[fhirtypes.PositiveIntType | None] | None
    diagnosisLinkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    encounter: list[fhirtypes.ReferenceType] | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    informationLinkId: list[fhirtypes.PositiveIntType | None] | None
    informationLinkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    locationAddress: fhirtypes.AddressType | None
    locationCodeableConcept: fhirtypes.CodeableConceptType | None
    locationReference: fhirtypes.ReferenceType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    net: fhirtypes.MoneyType | None
    procedureLinkId: list[fhirtypes.PositiveIntType | None] | None
    procedureLinkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    programCode: list[fhirtypes.CodeableConceptType] | None
    quantity: fhirtypes.QuantityType | None
    revenue: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    service: fhirtypes.CodeableConceptType | None
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

class ClaimItemDetail(backboneelement.BackboneElement):
    __resource_type__: str
    category: fhirtypes.CodeableConceptType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    modifier: list[fhirtypes.CodeableConceptType] | None
    net: fhirtypes.MoneyType | None
    programCode: list[fhirtypes.CodeableConceptType] | None
    quantity: fhirtypes.QuantityType | None
    revenue: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    service: fhirtypes.CodeableConceptType | None
    subDetail: list[fhirtypes.ClaimItemDetailSubDetailType] | None
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
    programCode: list[fhirtypes.CodeableConceptType] | None
    quantity: fhirtypes.QuantityType | None
    revenue: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.PositiveIntType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    service: fhirtypes.CodeableConceptType | None
    udi: list[fhirtypes.ReferenceType] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClaimPayee(backboneelement.BackboneElement):
    __resource_type__: str
    party: fhirtypes.ReferenceType | None
    resourceType: fhirtypes.CodingType | None
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
