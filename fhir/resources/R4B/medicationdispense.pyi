from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MedicationDispense(domainresource.DomainResource):
    __resource_type__: str
    authorizingPrescription: list[fhirtypes.ReferenceType] | None
    category: fhirtypes.CodeableConceptType | None
    context: fhirtypes.ReferenceType | None
    daysSupply: fhirtypes.QuantityType | None
    destination: fhirtypes.ReferenceType | None
    detectedIssue: list[fhirtypes.ReferenceType] | None
    dosageInstruction: list[fhirtypes.DosageType] | None
    eventHistory: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: fhirtypes.ReferenceType | None
    medicationCodeableConcept: fhirtypes.CodeableConceptType | None
    medicationReference: fhirtypes.ReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    performer: list[fhirtypes.MedicationDispensePerformerType] | None
    quantity: fhirtypes.QuantityType | None
    receiver: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReasonCodeableConcept: fhirtypes.CodeableConceptType | None
    statusReasonReference: fhirtypes.ReferenceType | None
    subject: fhirtypes.ReferenceType | None
    substitution: fhirtypes.MedicationDispenseSubstitutionType | None
    supportingInformation: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeableConceptType | None
    whenHandedOver: fhirtypes.DateTimeType | None
    whenHandedOver__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    whenPrepared: fhirtypes.DateTimeType | None
    whenPrepared__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationDispensePerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    __resource_type__: str
    reason: list[fhirtypes.CodeableConceptType] | None
    responsibleParty: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeableConceptType | None
    wasSubstituted: bool | None
    wasSubstituted__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
