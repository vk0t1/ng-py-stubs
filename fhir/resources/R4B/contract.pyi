from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Contract(domainresource.DomainResource):
    __resource_type__: str
    alias: list[fhirtypes.StringType | None] | None
    alias__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    applies: fhirtypes.PeriodType | None
    author: fhirtypes.ReferenceType | None
    authority: list[fhirtypes.ReferenceType] | None
    contentDefinition: fhirtypes.ContractContentDefinitionType | None
    contentDerivative: fhirtypes.CodeableConceptType | None
    domain: list[fhirtypes.ReferenceType] | None
    expirationType: fhirtypes.CodeableConceptType | None
    friendly: list[fhirtypes.ContractFriendlyType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    instantiatesCanonical: fhirtypes.ReferenceType | None
    instantiatesUri: fhirtypes.UriType | None
    instantiatesUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    issued: fhirtypes.DateTimeType | None
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    legal: list[fhirtypes.ContractLegalType] | None
    legalState: fhirtypes.CodeableConceptType | None
    legallyBindingAttachment: fhirtypes.AttachmentType | None
    legallyBindingReference: fhirtypes.ReferenceType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relevantHistory: list[fhirtypes.ReferenceType] | None
    rule: list[fhirtypes.ContractRuleType] | None
    scope: fhirtypes.CodeableConceptType | None
    signer: list[fhirtypes.ContractSignerType] | None
    site: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subType: list[fhirtypes.CodeableConceptType] | None
    subject: list[fhirtypes.ReferenceType] | None
    subtitle: fhirtypes.StringType | None
    subtitle__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    supportingInfo: list[fhirtypes.ReferenceType] | None
    term: list[fhirtypes.ContractTermType] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    topicCodeableConcept: fhirtypes.CodeableConceptType | None
    topicReference: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ContractContentDefinition(backboneelement.BackboneElement):
    __resource_type__: str
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publicationDate: fhirtypes.DateTimeType | None
    publicationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publicationStatus: fhirtypes.CodeType | None
    publicationStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.ReferenceType | None
    subType: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ContractFriendly(backboneelement.BackboneElement):
    __resource_type__: str
    contentAttachment: fhirtypes.AttachmentType | None
    contentReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ContractLegal(backboneelement.BackboneElement):
    __resource_type__: str
    contentAttachment: fhirtypes.AttachmentType | None
    contentReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ContractRule(backboneelement.BackboneElement):
    __resource_type__: str
    contentAttachment: fhirtypes.AttachmentType | None
    contentReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ContractSigner(backboneelement.BackboneElement):
    __resource_type__: str
    party: fhirtypes.ReferenceType
    signature: list[fhirtypes.SignatureType]
    type: fhirtypes.CodingType
    @classmethod
    def elements_sequence(cls): ...

class ContractTerm(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.ContractTermActionType] | None
    applies: fhirtypes.PeriodType | None
    asset: list[fhirtypes.ContractTermAssetType] | None
    group: list[fhirtypes.ContractTermType] | None
    identifier: fhirtypes.IdentifierType | None
    issued: fhirtypes.DateTimeType | None
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    offer: fhirtypes.ContractTermOfferType
    securityLabel: list[fhirtypes.ContractTermSecurityLabelType] | None
    subType: fhirtypes.CodeableConceptType | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    topicCodeableConcept: fhirtypes.CodeableConceptType | None
    topicReference: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ContractTermAction(backboneelement.BackboneElement):
    __resource_type__: str
    context: fhirtypes.ReferenceType | None
    contextLinkId: list[fhirtypes.StringType | None] | None
    contextLinkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    doNotPerform: bool | None
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    intent: fhirtypes.CodeableConceptType
    linkId: list[fhirtypes.StringType | None] | None
    linkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrencePeriod: fhirtypes.PeriodType | None
    occurrenceTiming: fhirtypes.TimingType | None
    performer: fhirtypes.ReferenceType | None
    performerLinkId: list[fhirtypes.StringType | None] | None
    performerLinkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    performerRole: fhirtypes.CodeableConceptType | None
    performerType: list[fhirtypes.CodeableConceptType] | None
    reason: list[fhirtypes.StringType | None] | None
    reason__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonLinkId: list[fhirtypes.StringType | None] | None
    reasonLinkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    requester: list[fhirtypes.ReferenceType] | None
    requesterLinkId: list[fhirtypes.StringType | None] | None
    requesterLinkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    securityLabelNumber: list[fhirtypes.UnsignedIntType | None] | None
    securityLabelNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    status: fhirtypes.CodeableConceptType
    subject: list[fhirtypes.ContractTermActionSubjectType] | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ContractTermActionSubject(backboneelement.BackboneElement):
    __resource_type__: str
    reference: list[fhirtypes.ReferenceType]
    role: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ContractTermAsset(backboneelement.BackboneElement):
    __resource_type__: str
    answer: list[fhirtypes.ContractTermOfferAnswerType] | None
    condition: fhirtypes.StringType | None
    condition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    context: list[fhirtypes.ContractTermAssetContextType] | None
    linkId: list[fhirtypes.StringType | None] | None
    linkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    period: list[fhirtypes.PeriodType] | None
    periodType: list[fhirtypes.CodeableConceptType] | None
    relationship: fhirtypes.CodingType | None
    scope: fhirtypes.CodeableConceptType | None
    securityLabelNumber: list[fhirtypes.UnsignedIntType | None] | None
    securityLabelNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    subtype: list[fhirtypes.CodeableConceptType] | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodeableConceptType] | None
    typeReference: list[fhirtypes.ReferenceType] | None
    usePeriod: list[fhirtypes.PeriodType] | None
    valuedItem: list[fhirtypes.ContractTermAssetValuedItemType] | None
    @classmethod
    def elements_sequence(cls): ...

class ContractTermAssetContext(backboneelement.BackboneElement):
    __resource_type__: str
    code: list[fhirtypes.CodeableConceptType] | None
    reference: fhirtypes.ReferenceType | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ContractTermAssetValuedItem(backboneelement.BackboneElement):
    __resource_type__: str
    effectiveTime: fhirtypes.DateTimeType | None
    effectiveTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    entityCodeableConcept: fhirtypes.CodeableConceptType | None
    entityReference: fhirtypes.ReferenceType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    linkId: list[fhirtypes.StringType | None] | None
    linkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    net: fhirtypes.MoneyType | None
    payment: fhirtypes.StringType | None
    payment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    paymentDate: fhirtypes.DateTimeType | None
    paymentDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    points: fhirtypes.DecimalType | None
    points__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.QuantityType | None
    recipient: fhirtypes.ReferenceType | None
    responsible: fhirtypes.ReferenceType | None
    securityLabelNumber: list[fhirtypes.UnsignedIntType | None] | None
    securityLabelNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ContractTermOffer(backboneelement.BackboneElement):
    __resource_type__: str
    answer: list[fhirtypes.ContractTermOfferAnswerType] | None
    decision: fhirtypes.CodeableConceptType | None
    decisionMode: list[fhirtypes.CodeableConceptType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    linkId: list[fhirtypes.StringType | None] | None
    linkId__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    party: list[fhirtypes.ContractTermOfferPartyType] | None
    securityLabelNumber: list[fhirtypes.UnsignedIntType | None] | None
    securityLabelNumber__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    topic: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ContractTermOfferAnswer(backboneelement.BackboneElement):
    __resource_type__: str
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCoding: fhirtypes.CodingType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueReference: fhirtypes.ReferenceType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTime: fhirtypes.TimeType | None
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueUri: fhirtypes.UriType | None
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ContractTermOfferParty(backboneelement.BackboneElement):
    __resource_type__: str
    reference: list[fhirtypes.ReferenceType]
    role: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class ContractTermSecurityLabel(backboneelement.BackboneElement):
    __resource_type__: str
    category: list[fhirtypes.CodingType] | None
    classification: fhirtypes.CodingType
    control: list[fhirtypes.CodingType] | None
    number: list[fhirtypes.UnsignedIntType | None] | None
    number__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...
