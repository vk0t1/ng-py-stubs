from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Practitioner(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    address: list[fhirtypes.AddressType] | None
    birthDate: fhirtypes.DateType | None
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    communication: list[fhirtypes.CodeableConceptType] | None
    gender: fhirtypes.CodeType | None
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    name: list[fhirtypes.HumanNameType] | None
    photo: list[fhirtypes.AttachmentType] | None
    qualification: list[fhirtypes.PractitionerQualificationType] | None
    telecom: list[fhirtypes.ContactPointType] | None
    @classmethod
    def elements_sequence(cls): ...

class PractitionerQualification(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    identifier: list[fhirtypes.IdentifierType] | None
    issuer: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
