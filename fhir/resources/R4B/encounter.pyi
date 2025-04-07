from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Encounter(domainresource.DomainResource):
    __resource_type__: str
    account: list[fhirtypes.ReferenceType] | None
    appointment: list[fhirtypes.ReferenceType] | None
    basedOn: list[fhirtypes.ReferenceType] | None
    classHistory: list[fhirtypes.EncounterClassHistoryType] | None
    class_fhir: fhirtypes.CodingType
    diagnosis: list[fhirtypes.EncounterDiagnosisType] | None
    episodeOfCare: list[fhirtypes.ReferenceType] | None
    hospitalization: fhirtypes.EncounterHospitalizationType | None
    identifier: list[fhirtypes.IdentifierType] | None
    length: fhirtypes.DurationType | None
    location: list[fhirtypes.EncounterLocationType] | None
    partOf: fhirtypes.ReferenceType | None
    participant: list[fhirtypes.EncounterParticipantType] | None
    period: fhirtypes.PeriodType | None
    priority: fhirtypes.CodeableConceptType | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    serviceProvider: fhirtypes.ReferenceType | None
    serviceType: fhirtypes.CodeableConceptType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusHistory: list[fhirtypes.EncounterStatusHistoryType] | None
    subject: fhirtypes.ReferenceType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class EncounterClassHistory(backboneelement.BackboneElement):
    __resource_type__: str
    class_fhir: fhirtypes.CodingType
    period: fhirtypes.PeriodType
    @classmethod
    def elements_sequence(cls): ...

class EncounterDiagnosis(backboneelement.BackboneElement):
    __resource_type__: str
    condition: fhirtypes.ReferenceType
    rank: fhirtypes.PositiveIntType | None
    rank__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    use: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class EncounterHospitalization(backboneelement.BackboneElement):
    __resource_type__: str
    admitSource: fhirtypes.CodeableConceptType | None
    destination: fhirtypes.ReferenceType | None
    dietPreference: list[fhirtypes.CodeableConceptType] | None
    dischargeDisposition: fhirtypes.CodeableConceptType | None
    origin: fhirtypes.ReferenceType | None
    preAdmissionIdentifier: fhirtypes.IdentifierType | None
    reAdmission: fhirtypes.CodeableConceptType | None
    specialArrangement: list[fhirtypes.CodeableConceptType] | None
    specialCourtesy: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class EncounterLocation(backboneelement.BackboneElement):
    __resource_type__: str
    location: fhirtypes.ReferenceType
    period: fhirtypes.PeriodType | None
    physicalType: fhirtypes.CodeableConceptType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class EncounterParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    individual: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class EncounterStatusHistory(backboneelement.BackboneElement):
    __resource_type__: str
    period: fhirtypes.PeriodType
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
