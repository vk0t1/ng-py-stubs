from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Organization(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    address: list[fhirtypes.AddressType] | None
    alias: list[fhirtypes.StringType | None] | None
    alias__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    contact: list[fhirtypes.OrganizationContactType] | None
    endpoint: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    partOf: fhirtypes.ReferenceType | None
    telecom: list[fhirtypes.ContactPointType] | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class OrganizationContact(backboneelement.BackboneElement):
    __resource_type__: str
    address: fhirtypes.AddressType | None
    name: fhirtypes.HumanNameType | None
    purpose: fhirtypes.CodeableConceptType | None
    telecom: list[fhirtypes.ContactPointType] | None
    @classmethod
    def elements_sequence(cls): ...
