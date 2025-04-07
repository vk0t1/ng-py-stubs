from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class AllergyIntolerance(domainresource.DomainResource):
    __resource_type__: str
    asserter: fhirtypes.ReferenceType | None
    category: list[fhirtypes.CodeType | None] | None
    category__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    clinicalStatus: fhirtypes.CodeableConceptType | None
    code: fhirtypes.CodeableConceptType | None
    criticality: fhirtypes.CodeType | None
    criticality__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    lastOccurrence: fhirtypes.DateTimeType | None
    lastOccurrence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    onsetAge: fhirtypes.AgeType | None
    onsetDateTime: fhirtypes.DateTimeType | None
    onsetDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    onsetPeriod: fhirtypes.PeriodType | None
    onsetRange: fhirtypes.RangeType | None
    onsetString: fhirtypes.StringType | None
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patient: fhirtypes.ReferenceType
    reaction: list[fhirtypes.AllergyIntoleranceReactionType] | None
    recordedDate: fhirtypes.DateTimeType | None
    recordedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    recorder: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    verificationStatus: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class AllergyIntoleranceReaction(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    exposureRoute: fhirtypes.CodeableConceptType | None
    manifestation: list[fhirtypes.CodeableConceptType]
    note: list[fhirtypes.AnnotationType] | None
    onset: fhirtypes.DateTimeType | None
    onset__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    severity: fhirtypes.CodeType | None
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    substance: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
