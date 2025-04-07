from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Immunization(domainresource.DomainResource):
    __resource_type__: str
    administeredProduct: fhirtypes.CodeableReferenceType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    doseQuantity: fhirtypes.QuantityType | None
    encounter: fhirtypes.ReferenceType | None
    expirationDate: fhirtypes.DateType | None
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fundingSource: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    informationSource: fhirtypes.CodeableReferenceType | None
    isSubpotent: bool | None
    isSubpotent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    location: fhirtypes.ReferenceType | None
    lotNumber: fhirtypes.StringType | None
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    manufacturer: fhirtypes.CodeableReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrenceString: fhirtypes.StringType | None
    occurrenceString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patient: fhirtypes.ReferenceType
    performer: list[fhirtypes.ImmunizationPerformerType] | None
    primarySource: bool | None
    primarySource__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    programEligibility: list[fhirtypes.ImmunizationProgramEligibilityType] | None
    protocolApplied: list[fhirtypes.ImmunizationProtocolAppliedType] | None
    reaction: list[fhirtypes.ImmunizationReactionType] | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    route: fhirtypes.CodeableConceptType | None
    site: fhirtypes.CodeableConceptType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.CodeableConceptType | None
    subpotentReason: list[fhirtypes.CodeableConceptType] | None
    supportingInformation: list[fhirtypes.ReferenceType] | None
    vaccineCode: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ImmunizationPerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ImmunizationProgramEligibility(backboneelement.BackboneElement):
    __resource_type__: str
    program: fhirtypes.CodeableConceptType
    programStatus: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class ImmunizationProtocolApplied(backboneelement.BackboneElement):
    __resource_type__: str
    authority: fhirtypes.ReferenceType | None
    doseNumber: fhirtypes.StringType | None
    doseNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    series: fhirtypes.StringType | None
    series__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    seriesDoses: fhirtypes.StringType | None
    seriesDoses__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetDisease: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImmunizationReaction(backboneelement.BackboneElement):
    __resource_type__: str
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    manifestation: fhirtypes.CodeableReferenceType | None
    reported: bool | None
    reported__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
