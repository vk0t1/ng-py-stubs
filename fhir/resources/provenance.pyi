from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Provenance(domainresource.DomainResource):
    __resource_type__: str
    activity: fhirtypes.CodeableConceptType | None
    agent: list[fhirtypes.ProvenanceAgentType]
    authorization: list[fhirtypes.CodeableReferenceType] | None
    basedOn: list[fhirtypes.ReferenceType] | None
    encounter: fhirtypes.ReferenceType | None
    entity: list[fhirtypes.ProvenanceEntityType] | None
    location: fhirtypes.ReferenceType | None
    occurredDateTime: fhirtypes.DateTimeType | None
    occurredDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurredPeriod: fhirtypes.PeriodType | None
    patient: fhirtypes.ReferenceType | None
    policy: list[fhirtypes.UriType | None] | None
    policy__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    recorded: fhirtypes.InstantType | None
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    signature: list[fhirtypes.SignatureType] | None
    target: list[fhirtypes.ReferenceType]
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ProvenanceAgent(backboneelement.BackboneElement):
    __resource_type__: str
    onBehalfOf: fhirtypes.ReferenceType | None
    role: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType | None
    who: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...

class ProvenanceEntity(backboneelement.BackboneElement):
    __resource_type__: str
    agent: list[fhirtypes.ProvenanceAgentType] | None
    role: fhirtypes.CodeType | None
    role__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    what: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
