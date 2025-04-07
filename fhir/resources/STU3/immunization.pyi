from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Immunization(domainresource.DomainResource):
    __resource_type__: str
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    doseQuantity: fhirtypes.QuantityType | None
    encounter: fhirtypes.ReferenceType | None
    expirationDate: fhirtypes.DateType | None
    expirationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    explanation: fhirtypes.ImmunizationExplanationType | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: fhirtypes.ReferenceType | None
    lotNumber: fhirtypes.StringType | None
    lotNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    manufacturer: fhirtypes.ReferenceType | None
    notGiven: bool | None
    notGiven__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    patient: fhirtypes.ReferenceType
    practitioner: list[fhirtypes.ImmunizationPractitionerType] | None
    primarySource: bool | None
    primarySource__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reaction: list[fhirtypes.ImmunizationReactionType] | None
    reportOrigin: fhirtypes.CodeableConceptType | None
    route: fhirtypes.CodeableConceptType | None
    site: fhirtypes.CodeableConceptType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    vaccinationProtocol: list[fhirtypes.ImmunizationVaccinationProtocolType] | None
    vaccineCode: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImmunizationExplanation(backboneelement.BackboneElement):
    __resource_type__: str
    reason: list[fhirtypes.CodeableConceptType] | None
    reasonNotGiven: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class ImmunizationPractitioner(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    role: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ImmunizationReaction(backboneelement.BackboneElement):
    __resource_type__: str
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    detail: fhirtypes.ReferenceType | None
    reported: bool | None
    reported__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ImmunizationVaccinationProtocol(backboneelement.BackboneElement):
    __resource_type__: str
    authority: fhirtypes.ReferenceType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    doseSequence: fhirtypes.PositiveIntType | None
    doseSequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    doseStatus: fhirtypes.CodeableConceptType
    doseStatusReason: fhirtypes.CodeableConceptType | None
    series: fhirtypes.StringType | None
    series__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    seriesDoses: fhirtypes.PositiveIntType | None
    seriesDoses__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetDisease: list[fhirtypes.CodeableConceptType]
    @classmethod
    def elements_sequence(cls): ...
