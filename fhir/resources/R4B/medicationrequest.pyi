from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MedicationRequest(domainresource.DomainResource):
    __resource_type__: str
    authoredOn: fhirtypes.DateTimeType | None
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    courseOfTherapyType: fhirtypes.CodeableConceptType | None
    detectedIssue: list[fhirtypes.ReferenceType] | None
    dispenseRequest: fhirtypes.MedicationRequestDispenseRequestType | None
    doNotPerform: bool | None
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dosageInstruction: list[fhirtypes.DosageType] | None
    encounter: fhirtypes.ReferenceType | None
    eventHistory: list[fhirtypes.ReferenceType] | None
    groupIdentifier: fhirtypes.IdentifierType | None
    identifier: list[fhirtypes.IdentifierType] | None
    instantiatesCanonical: list[fhirtypes.CanonicalType | None] | None
    instantiatesCanonical__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    instantiatesUri: list[fhirtypes.UriType | None] | None
    instantiatesUri__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    insurance: list[fhirtypes.ReferenceType] | None
    intent: fhirtypes.CodeType | None
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    medicationCodeableConcept: fhirtypes.CodeableConceptType | None
    medicationReference: fhirtypes.ReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    performer: fhirtypes.ReferenceType | None
    performerType: fhirtypes.CodeableConceptType | None
    priorPrescription: fhirtypes.ReferenceType | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    recorder: fhirtypes.ReferenceType | None
    reportedBoolean: bool | None
    reportedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reportedReference: fhirtypes.ReferenceType | None
    requester: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.CodeableConceptType | None
    subject: fhirtypes.ReferenceType
    substitution: fhirtypes.MedicationRequestSubstitutionType | None
    supportingInformation: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationRequestDispenseRequest(backboneelement.BackboneElement):
    __resource_type__: str
    dispenseInterval: fhirtypes.DurationType | None
    expectedSupplyDuration: fhirtypes.DurationType | None
    initialFill: fhirtypes.MedicationRequestDispenseRequestInitialFillType | None
    numberOfRepeatsAllowed: fhirtypes.UnsignedIntType | None
    numberOfRepeatsAllowed__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    performer: fhirtypes.ReferenceType | None
    quantity: fhirtypes.QuantityType | None
    validityPeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationRequestDispenseRequestInitialFill(backboneelement.BackboneElement):
    __resource_type__: str
    duration: fhirtypes.DurationType | None
    quantity: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationRequestSubstitution(backboneelement.BackboneElement):
    __resource_type__: str
    allowedBoolean: bool | None
    allowedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    allowedCodeableConcept: fhirtypes.CodeableConceptType | None
    reason: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
