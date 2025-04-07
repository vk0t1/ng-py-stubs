from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Consent(domainresource.DomainResource):
    __resource_type__: str
    category: list[fhirtypes.CodeableConceptType]
    dateTime: fhirtypes.DateTimeType | None
    dateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    organization: list[fhirtypes.ReferenceType] | None
    patient: fhirtypes.ReferenceType | None
    performer: list[fhirtypes.ReferenceType] | None
    policy: list[fhirtypes.ConsentPolicyType] | None
    policyRule: fhirtypes.CodeableConceptType | None
    provision: fhirtypes.ConsentProvisionType | None
    scope: fhirtypes.CodeableConceptType
    sourceAttachment: fhirtypes.AttachmentType | None
    sourceReference: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    verification: list[fhirtypes.ConsentVerificationType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ConsentPolicy(backboneelement.BackboneElement):
    __resource_type__: str
    authority: fhirtypes.UriType | None
    authority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uri: fhirtypes.UriType | None
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ConsentProvision(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.CodeableConceptType] | None
    actor: list[fhirtypes.ConsentProvisionActorType] | None
    class_fhir: list[fhirtypes.CodingType] | None
    code: list[fhirtypes.CodeableConceptType] | None
    data: list[fhirtypes.ConsentProvisionDataType] | None
    dataPeriod: fhirtypes.PeriodType | None
    period: fhirtypes.PeriodType | None
    provision: list[fhirtypes.ConsentProvisionType] | None
    purpose: list[fhirtypes.CodingType] | None
    securityLabel: list[fhirtypes.CodingType] | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ConsentProvisionActor(backboneelement.BackboneElement):
    __resource_type__: str
    reference: fhirtypes.ReferenceType
    role: fhirtypes.CodeableConceptType
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
    verificationDate: fhirtypes.DateTimeType | None
    verificationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    verified: bool | None
    verified__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    verifiedWith: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
