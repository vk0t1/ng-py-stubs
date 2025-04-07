from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Patient(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    address: list[fhirtypes.AddressType] | None
    birthDate: fhirtypes.DateType | None
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    communication: list[fhirtypes.PatientCommunicationType] | None
    contact: list[fhirtypes.PatientContactType] | None
    deceasedBoolean: bool | None
    deceasedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    deceasedDateTime: fhirtypes.DateTimeType | None
    deceasedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    gender: fhirtypes.CodeType | None
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    generalPractitioner: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    link: list[fhirtypes.PatientLinkType] | None
    managingOrganization: fhirtypes.ReferenceType | None
    maritalStatus: fhirtypes.CodeableConceptType | None
    multipleBirthBoolean: bool | None
    multipleBirthBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    multipleBirthInteger: fhirtypes.IntegerType | None
    multipleBirthInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: list[fhirtypes.HumanNameType] | None
    photo: list[fhirtypes.AttachmentType] | None
    telecom: list[fhirtypes.ContactPointType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class PatientCommunication(backboneelement.BackboneElement):
    __resource_type__: str
    language: fhirtypes.CodeableConceptType
    preferred: bool | None
    preferred__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class PatientContact(backboneelement.BackboneElement):
    __resource_type__: str
    address: fhirtypes.AddressType | None
    gender: fhirtypes.CodeType | None
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.HumanNameType | None
    organization: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    relationship: list[fhirtypes.CodeableConceptType] | None
    telecom: list[fhirtypes.ContactPointType] | None
    @classmethod
    def elements_sequence(cls): ...

class PatientLink(backboneelement.BackboneElement):
    __resource_type__: str
    other: fhirtypes.ReferenceType
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
