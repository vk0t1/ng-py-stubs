from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Consent(domainresource.DomainResource):
    __resource_type__: str
    action: list[fhirtypes.CodeableConceptType] | None
    actor: list[fhirtypes.ConsentActorType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    consentingParty: list[fhirtypes.ReferenceType] | None
    data: list[fhirtypes.ConsentDataType] | None
    dataPeriod: fhirtypes.PeriodType | None
    dateTime: fhirtypes.DateTimeType | None
    dateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    except_fhir: list[fhirtypes.ConsentExceptType] | None
    identifier: fhirtypes.IdentifierType | None
    organization: list[fhirtypes.ReferenceType] | None
    patient: fhirtypes.ReferenceType
    period: fhirtypes.PeriodType | None
    policy: list[fhirtypes.ConsentPolicyType] | None
    policyRule: fhirtypes.UriType | None
    policyRule__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: list[fhirtypes.CodingType] | None
    securityLabel: list[fhirtypes.CodingType] | None
    sourceAttachment: fhirtypes.AttachmentType | None
    sourceIdentifier: fhirtypes.IdentifierType | None
    sourceReference: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ConsentActor(backboneelement.BackboneElement):
    __resource_type__: str
    reference: fhirtypes.ReferenceType
    role: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class ConsentData(backboneelement.BackboneElement):
    __resource_type__: str
    meaning: fhirtypes.CodeType | None
    meaning__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reference: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ConsentExcept(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.CodeableConceptType] | None
    actor: list[fhirtypes.ConsentExceptActorType] | None
    class_fhir: list[fhirtypes.CodingType] | None
    code: list[fhirtypes.CodingType] | None
    data: list[fhirtypes.ConsentExceptDataType] | None
    dataPeriod: fhirtypes.PeriodType | None
    period: fhirtypes.PeriodType | None
    purpose: list[fhirtypes.CodingType] | None
    securityLabel: list[fhirtypes.CodingType] | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ConsentExceptActor(backboneelement.BackboneElement):
    __resource_type__: str
    reference: fhirtypes.ReferenceType
    role: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class ConsentExceptData(backboneelement.BackboneElement):
    __resource_type__: str
    meaning: fhirtypes.CodeType | None
    meaning__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reference: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ConsentPolicy(backboneelement.BackboneElement):
    __resource_type__: str
    authority: fhirtypes.UriType | None
    authority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uri: fhirtypes.UriType | None
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
