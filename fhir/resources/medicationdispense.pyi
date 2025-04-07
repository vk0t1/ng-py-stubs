from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MedicationDispense(domainresource.DomainResource):
    __resource_type__: str
    authorizingPrescription: list[fhirtypes.ReferenceType] | None
    basedOn: list[fhirtypes.ReferenceType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    daysSupply: fhirtypes.QuantityType | None
    destination: fhirtypes.ReferenceType | None
    dosageInstruction: list[fhirtypes.DosageType] | None
    encounter: fhirtypes.ReferenceType | None
    eventHistory: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: fhirtypes.ReferenceType | None
    medication: fhirtypes.CodeableReferenceType
    notPerformedReason: fhirtypes.CodeableReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    performer: list[fhirtypes.MedicationDispensePerformerType] | None
    quantity: fhirtypes.QuantityType | None
    receiver: list[fhirtypes.ReferenceType] | None
    recorded: fhirtypes.DateTimeType | None
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    renderedDosageInstruction: fhirtypes.MarkdownType | None
    renderedDosageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusChanged: fhirtypes.DateTimeType | None
    statusChanged__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
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

class MedicationDispensePerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    __resource_type__: str
    reason: list[fhirtypes.CodeableConceptType] | None
    responsibleParty: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    wasSubstituted: bool | None
    wasSubstituted__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
