from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class EpisodeOfCare(domainresource.DomainResource):
    __resource_type__: str
    account: list[fhirtypes.ReferenceType] | None
    careManager: fhirtypes.ReferenceType | None
    diagnosis: list[fhirtypes.EpisodeOfCareDiagnosisType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    managingOrganization: fhirtypes.ReferenceType | None
    patient: fhirtypes.ReferenceType
    period: fhirtypes.PeriodType | None
    referralRequest: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusHistory: list[fhirtypes.EpisodeOfCareStatusHistoryType] | None
    team: list[fhirtypes.ReferenceType] | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class EpisodeOfCareDiagnosis(backboneelement.BackboneElement):
    __resource_type__: str
    condition: fhirtypes.ReferenceType
    rank: fhirtypes.PositiveIntType | None
    rank__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    role: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class EpisodeOfCareStatusHistory(backboneelement.BackboneElement):
    __resource_type__: str
    period: fhirtypes.PeriodType
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
