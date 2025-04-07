from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DeviceAssociation(domainresource.DomainResource):
    __resource_type__: str
    bodyStructure: fhirtypes.ReferenceType | None
    category: list[fhirtypes.CodeableConceptType] | None
    device: fhirtypes.ReferenceType
    identifier: list[fhirtypes.IdentifierType] | None
    operation: list[fhirtypes.DeviceAssociationOperationType] | None
    period: fhirtypes.PeriodType | None
    status: fhirtypes.CodeableConceptType
    statusReason: list[fhirtypes.CodeableConceptType] | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class DeviceAssociationOperation(backboneelement.BackboneElement):
    __resource_type__: str
    operator: list[fhirtypes.ReferenceType] | None
    period: fhirtypes.PeriodType | None
    status: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
