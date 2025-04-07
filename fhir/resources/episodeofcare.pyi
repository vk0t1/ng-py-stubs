from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class EpisodeOfCare(domainresource.DomainResource):
    __resource_type__: str
    account: list[fhirtypes.ReferenceType] | None
    careManager: fhirtypes.ReferenceType | None
    careTeam: list[fhirtypes.ReferenceType] | None
    diagnosis: list[fhirtypes.EpisodeOfCareDiagnosisType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    managingOrganization: fhirtypes.ReferenceType | None
    patient: fhirtypes.ReferenceType
    period: fhirtypes.PeriodType | None
    reason: list[fhirtypes.EpisodeOfCareReasonType] | None
    referralRequest: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusHistory: list[fhirtypes.EpisodeOfCareStatusHistoryType] | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class EpisodeOfCareDiagnosis(backboneelement.BackboneElement):
    __resource_type__: str
    condition: list[fhirtypes.CodeableReferenceType] | None
    use: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class EpisodeOfCareReason(backboneelement.BackboneElement):
    __resource_type__: str
    use: fhirtypes.CodeableConceptType | None
    value: list[fhirtypes.CodeableReferenceType] | None
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
