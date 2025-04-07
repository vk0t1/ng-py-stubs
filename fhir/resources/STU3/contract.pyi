from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Contract(domainresource.DomainResource):
    __resource_type__: str
    action: list[fhirtypes.CodeableConceptType] | None
    actionReason: list[fhirtypes.CodeableConceptType] | None
    agent: list[fhirtypes.ContractAgentType] | None
    applies: fhirtypes.PeriodType | None
    authority: list[fhirtypes.ReferenceType] | None
    bindingAttachment: fhirtypes.AttachmentType | None
    bindingReference: fhirtypes.ReferenceType | None
    contentDerivative: fhirtypes.CodeableConceptType | None
    decisionType: fhirtypes.CodeableConceptType | None
    domain: list[fhirtypes.ReferenceType] | None
    friendly: list[fhirtypes.ContractFriendlyType] | None
    identifier: fhirtypes.IdentifierType | None
    issued: fhirtypes.DateTimeType | None
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    legal: list[fhirtypes.ContractLegalType] | None
    rule: list[fhirtypes.ContractRuleType] | None
    securityLabel: list[fhirtypes.CodingType] | None
    signer: list[fhirtypes.ContractSignerType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subType: list[fhirtypes.CodeableConceptType] | None
    subject: list[fhirtypes.ReferenceType] | None
    term: list[fhirtypes.ContractTermType] | None
    topic: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeableConceptType | None
    valuedItem: list[fhirtypes.ContractValuedItemType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ContractAgent(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    role: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

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
    action: list[fhirtypes.CodeableConceptType] | None
    actionReason: list[fhirtypes.CodeableConceptType] | None
    agent: list[fhirtypes.ContractTermAgentType] | None
    applies: fhirtypes.PeriodType | None
    group: list[fhirtypes.ContractTermType] | None
    identifier: fhirtypes.IdentifierType | None
    issued: fhirtypes.DateTimeType | None
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    securityLabel: list[fhirtypes.CodingType] | None
    subType: fhirtypes.CodeableConceptType | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    topic: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeableConceptType | None
    valuedItem: list[fhirtypes.ContractTermValuedItemType] | None
    @classmethod
    def elements_sequence(cls): ...

class ContractTermAgent(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    role: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class ContractTermValuedItem(backboneelement.BackboneElement):
    __resource_type__: str
    effectiveTime: fhirtypes.DateTimeType | None
    effectiveTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    entityCodeableConcept: fhirtypes.CodeableConceptType | None
    entityReference: fhirtypes.ReferenceType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    net: fhirtypes.MoneyType | None
    points: fhirtypes.DecimalType | None
    points__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.QuantityType | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ContractValuedItem(backboneelement.BackboneElement):
    __resource_type__: str
    effectiveTime: fhirtypes.DateTimeType | None
    effectiveTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    entityCodeableConcept: fhirtypes.CodeableConceptType | None
    entityReference: fhirtypes.ReferenceType | None
    factor: fhirtypes.DecimalType | None
    factor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    net: fhirtypes.MoneyType | None
    points: fhirtypes.DecimalType | None
    points__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.QuantityType | None
    unitPrice: fhirtypes.MoneyType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
