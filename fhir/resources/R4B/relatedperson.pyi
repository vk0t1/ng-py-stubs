from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class RelatedPerson(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    address: list[fhirtypes.AddressType] | None
    birthDate: fhirtypes.DateType | None
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    communication: list[fhirtypes.RelatedPersonCommunicationType] | None
    gender: fhirtypes.CodeType | None
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    name: list[fhirtypes.HumanNameType] | None
    patient: fhirtypes.ReferenceType
    period: fhirtypes.PeriodType | None
    photo: list[fhirtypes.AttachmentType] | None
    relationship: list[fhirtypes.CodeableConceptType] | None
    telecom: list[fhirtypes.ContactPointType] | None
    @classmethod
    def elements_sequence(cls): ...

class RelatedPersonCommunication(backboneelement.BackboneElement):
    __resource_type__: str
    language: fhirtypes.CodeableConceptType
    preferred: bool | None
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
