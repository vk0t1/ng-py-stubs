from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Consent(domainresource.DomainResource):
    __resource_type__: str
    category: list[fhirtypes.CodeableConceptType] | None
    controller: list[fhirtypes.ReferenceType] | None
    date: fhirtypes.DateType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    decision: fhirtypes.CodeType | None
    decision__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    grantee: list[fhirtypes.ReferenceType] | None
    grantor: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    manager: list[fhirtypes.ReferenceType] | None
    period: fhirtypes.PeriodType | None
    policyBasis: fhirtypes.ConsentPolicyBasisType | None
    policyText: list[fhirtypes.ReferenceType] | None
    provision: list[fhirtypes.ConsentProvisionType] | None
    regulatoryBasis: list[fhirtypes.CodeableConceptType] | None
    sourceAttachment: list[fhirtypes.AttachmentType] | None
    sourceReference: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    verification: list[fhirtypes.ConsentVerificationType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ConsentPolicyBasis(backboneelement.BackboneElement):
    __resource_type__: str
    reference: fhirtypes.ReferenceType | None
    url: fhirtypes.UrlType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ConsentProvision(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.CodeableConceptType] | None
    actor: list[fhirtypes.ConsentProvisionActorType] | None
    code: list[fhirtypes.CodeableConceptType] | None
    data: list[fhirtypes.ConsentProvisionDataType] | None
    dataPeriod: fhirtypes.PeriodType | None
    documentType: list[fhirtypes.CodingType] | None
    expression: fhirtypes.ExpressionType | None
    period: fhirtypes.PeriodType | None
    provision: list[fhirtypes.ConsentProvisionType] | None
    purpose: list[fhirtypes.CodingType] | None
    resourceType: list[fhirtypes.CodingType] | None
    securityLabel: list[fhirtypes.CodingType] | None
    @classmethod
    def elements_sequence(cls): ...

class ConsentProvisionActor(backboneelement.BackboneElement):
    __resource_type__: str
    reference: fhirtypes.ReferenceType | None
    role: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ConsentProvisionData(backboneelement.BackboneElement):
    __resource_type__: str
    meaning: fhirtypes.CodeType | None
    meaning__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reference: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ConsentVerification(backboneelement.BackboneElement):
    __resource_type__: str
    verificationDate: list[fhirtypes.DateTimeType | None] | None
    verificationDate__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    verificationType: fhirtypes.CodeableConceptType | None
    verified: bool | None
    verified__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    verifiedBy: fhirtypes.ReferenceType | None
    verifiedWith: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
