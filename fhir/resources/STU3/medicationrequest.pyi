from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MedicationRequest(domainresource.DomainResource):
    __resource_type__: str
    authoredOn: fhirtypes.DateTimeType | None
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    category: fhirtypes.CodeableConceptType | None
    context: fhirtypes.ReferenceType | None
    definition: list[fhirtypes.ReferenceType] | None
    detectedIssue: list[fhirtypes.ReferenceType] | None
    dispenseRequest: fhirtypes.MedicationRequestDispenseRequestType | None
    dosageInstruction: list[fhirtypes.DosageType] | None
    eventHistory: list[fhirtypes.ReferenceType] | None
    groupIdentifier: fhirtypes.IdentifierType | None
    identifier: list[fhirtypes.IdentifierType] | None
    intent: fhirtypes.CodeType | None
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    medicationCodeableConcept: fhirtypes.CodeableConceptType | None
    medicationReference: fhirtypes.ReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    priorPrescription: fhirtypes.ReferenceType | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    recorder: fhirtypes.ReferenceType | None
    requester: fhirtypes.MedicationRequestRequesterType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    substitution: fhirtypes.MedicationRequestSubstitutionType | None
    supportingInformation: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationRequestDispenseRequest(backboneelement.BackboneElement):
    __resource_type__: str
    expectedSupplyDuration: fhirtypes.DurationType | None
    numberOfRepeatsAllowed: fhirtypes.PositiveIntType | None
    numberOfRepeatsAllowed__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    performer: fhirtypes.ReferenceType | None
    quantity: fhirtypes.QuantityType | None
    validityPeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationRequestRequester(backboneelement.BackboneElement):
    __resource_type__: str
    agent: fhirtypes.ReferenceType
    onBehalfOf: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationRequestSubstitution(backboneelement.BackboneElement):
    __resource_type__: str
    allowed: bool | None
    allowed__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reason: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
