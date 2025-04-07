from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Immunization(domainresource.DomainResource):
    __resource_type__: str
    doseQuantity: fhirtypes.QuantityType | None
    education: list[fhirtypes.ImmunizationEducationType] | None
    encounter: fhirtypes.ReferenceType | None
    expirationDate: fhirtypes.DateType | None
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fundingSource: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    isSubpotent: bool | None
    isSubpotent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    location: fhirtypes.ReferenceType | None
    lotNumber: fhirtypes.StringType | None
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    manufacturer: fhirtypes.ReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    occurrenceDateTime: fhirtypes.DateTimeType | None
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    occurrenceString: fhirtypes.StringType | None
    occurrenceString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patient: fhirtypes.ReferenceType
    performer: list[fhirtypes.ImmunizationPerformerType] | None
    primarySource: bool | None
    primarySource__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    programEligibility: list[fhirtypes.CodeableConceptType] | None
    protocolApplied: list[fhirtypes.ImmunizationProtocolAppliedType] | None
    reaction: list[fhirtypes.ImmunizationReactionType] | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    recorded: fhirtypes.DateTimeType | None
    recorded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reportOrigin: fhirtypes.CodeableConceptType | None
    route: fhirtypes.CodeableConceptType | None
    site: fhirtypes.CodeableConceptType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.CodeableConceptType | None
    subpotentReason: list[fhirtypes.CodeableConceptType] | None
    vaccineCode: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ImmunizationEducation(backboneelement.BackboneElement):
    __resource_type__: str
    documentType: fhirtypes.StringType | None
    documentType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    presentationDate: fhirtypes.DateTimeType | None
    presentationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publicationDate: fhirtypes.DateTimeType | None
    publicationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reference: fhirtypes.UriType | None
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ImmunizationPerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ImmunizationProtocolApplied(backboneelement.BackboneElement):
    __resource_type__: str
    authority: fhirtypes.ReferenceType | None
    doseNumberPositiveInt: fhirtypes.PositiveIntType | None
    doseNumberPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    doseNumberString: fhirtypes.StringType | None
    doseNumberString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    series: fhirtypes.StringType | None
    series__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    seriesDosesPositiveInt: fhirtypes.PositiveIntType | None
    seriesDosesPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    seriesDosesString: fhirtypes.StringType | None
    seriesDosesString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetDisease: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ImmunizationReaction(backboneelement.BackboneElement):
    __resource_type__: str
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    detail: fhirtypes.ReferenceType | None
    reported: bool | None
    reported__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
