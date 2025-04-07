from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Encounter(domainresource.DomainResource):
    __resource_type__: str
    account: list[fhirtypes.ReferenceType] | None
    actualPeriod: fhirtypes.PeriodType | None
    admission: fhirtypes.EncounterAdmissionType | None
    appointment: list[fhirtypes.ReferenceType] | None
    basedOn: list[fhirtypes.ReferenceType] | None
    careTeam: list[fhirtypes.ReferenceType] | None
    class_fhir: list[fhirtypes.CodeableConceptType] | None
    diagnosis: list[fhirtypes.EncounterDiagnosisType] | None
    dietPreference: list[fhirtypes.CodeableConceptType] | None
    episodeOfCare: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    length: fhirtypes.DurationType | None
    location: list[fhirtypes.EncounterLocationType] | None
    partOf: fhirtypes.ReferenceType | None
    participant: list[fhirtypes.EncounterParticipantType] | None
    plannedEndDate: fhirtypes.DateTimeType | None
    plannedEndDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    plannedStartDate: fhirtypes.DateTimeType | None
    plannedStartDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    priority: fhirtypes.CodeableConceptType | None
    reason: list[fhirtypes.EncounterReasonType] | None
    serviceProvider: fhirtypes.ReferenceType | None
    serviceType: list[fhirtypes.CodeableReferenceType] | None
    specialArrangement: list[fhirtypes.CodeableConceptType] | None
    specialCourtesy: list[fhirtypes.CodeableConceptType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    subjectStatus: fhirtypes.CodeableConceptType | None
    type: list[fhirtypes.CodeableConceptType] | None
    virtualService: list[fhirtypes.VirtualServiceDetailType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class EncounterAdmission(backboneelement.BackboneElement):
    __resource_type__: str
    admitSource: fhirtypes.CodeableConceptType | None
    destination: fhirtypes.ReferenceType | None
    dischargeDisposition: fhirtypes.CodeableConceptType | None
    origin: fhirtypes.ReferenceType | None
    preAdmissionIdentifier: fhirtypes.IdentifierType | None
    reAdmission: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class EncounterDiagnosis(backboneelement.BackboneElement):
    __resource_type__: str
    condition: list[fhirtypes.CodeableReferenceType] | None
    use: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class EncounterLocation(backboneelement.BackboneElement):
    __resource_type__: str
    form: fhirtypes.CodeableConceptType | None
    location: fhirtypes.ReferenceType
    period: fhirtypes.PeriodType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class EncounterParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class EncounterReason(backboneelement.BackboneElement):
    __resource_type__: str
    use: list[fhirtypes.CodeableConceptType] | None
    value: list[fhirtypes.CodeableReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
