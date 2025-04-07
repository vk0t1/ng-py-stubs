from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class CareTeam(domainresource.DomainResource):
    __resource_type__: str
    category: list[fhirtypes.CodeableConceptType] | None
    context: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    managingOrganization: list[fhirtypes.ReferenceType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    participant: list[fhirtypes.CareTeamParticipantType] | None
    period: fhirtypes.PeriodType | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class CareTeamParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    member: fhirtypes.ReferenceType | None
    onBehalfOf: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    role: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
