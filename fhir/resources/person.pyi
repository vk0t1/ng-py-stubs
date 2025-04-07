from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Person(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    address: list[fhirtypes.AddressType] | None
    birthDate: fhirtypes.DateType | None
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    communication: list[fhirtypes.PersonCommunicationType] | None
    deceasedBoolean: bool | None
    deceasedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    deceasedDateTime: fhirtypes.DateTimeType | None
    deceasedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    gender: fhirtypes.CodeType | None
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    link: list[fhirtypes.PersonLinkType] | None
    managingOrganization: fhirtypes.ReferenceType | None
    maritalStatus: fhirtypes.CodeableConceptType | None
    name: list[fhirtypes.HumanNameType] | None
    photo: list[fhirtypes.AttachmentType] | None
    telecom: list[fhirtypes.ContactPointType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class PersonCommunication(backboneelement.BackboneElement):
    __resource_type__: str
    language: fhirtypes.CodeableConceptType
    preferred: bool | None
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class PersonLink(backboneelement.BackboneElement):
    __resource_type__: str
    assurance: fhirtypes.CodeType | None
    assurance__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    target: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
