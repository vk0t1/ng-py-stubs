from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class RelatedPerson(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    address: list[fhirtypes.AddressType] | None
    birthDate: fhirtypes.DateType | None
    birthDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    gender: fhirtypes.CodeType | None
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    name: list[fhirtypes.HumanNameType] | None
    patient: fhirtypes.ReferenceType
    period: fhirtypes.PeriodType | None
    photo: list[fhirtypes.AttachmentType] | None
    relationship: fhirtypes.CodeableConceptType | None
    telecom: list[fhirtypes.ContactPointType] | None
    @classmethod
    def elements_sequence(cls): ...
