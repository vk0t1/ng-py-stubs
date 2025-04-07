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
    device: list[fhirtypes.CodeableReferenceType] | None
    dispenseRequest: fhirtypes.MedicationRequestDispenseRequestType | None
    doNotPerform: bool | None
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dosageInstruction: list[fhirtypes.DosageType] | None
    effectiveDosePeriod: fhirtypes.PeriodType | None
    encounter: fhirtypes.ReferenceType | None
    eventHistory: list[fhirtypes.ReferenceType] | None
    groupIdentifier: fhirtypes.IdentifierType | None
    identifier: list[fhirtypes.IdentifierType] | None
    informationSource: list[fhirtypes.ReferenceType] | None
    insurance: list[fhirtypes.ReferenceType] | None
    intent: fhirtypes.CodeType | None
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    medication: fhirtypes.CodeableReferenceType
    note: list[fhirtypes.AnnotationType] | None
    performer: list[fhirtypes.ReferenceType] | None
    performerType: fhirtypes.CodeableConceptType | None
    priorPrescription: fhirtypes.ReferenceType | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    recorder: fhirtypes.ReferenceType | None
    renderedDosageInstruction: fhirtypes.MarkdownType | None
    renderedDosageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reported: bool | None
    reported__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    requester: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusChanged: fhirtypes.DateTimeType | None
    statusChanged__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.CodeableConceptType | None
    subject: fhirtypes.ReferenceType
    substitution: fhirtypes.MedicationRequestSubstitutionType | None
    supportingInformation: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MedicationRequestDispenseRequest(backboneelement.BackboneElement):
    __resource_type__: str
    dispenseInterval: fhirtypes.DurationType | None
    dispenser: fhirtypes.ReferenceType | None
    dispenserInstruction: list[fhirtypes.AnnotationType] | None
    doseAdministrationAid: fhirtypes.CodeableConceptType | None
    expectedSupplyDuration: fhirtypes.DurationType | None
    initialFill: fhirtypes.MedicationRequestDispenseRequestInitialFillType | None
    numberOfRepeatsAllowed: fhirtypes.UnsignedIntType | None
    numberOfRepeatsAllowed__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
