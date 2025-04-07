from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class FamilyMemberHistory(domainresource.DomainResource):
    __resource_type__: str
    ageAge: fhirtypes.AgeType | None
    ageRange: fhirtypes.RangeType | None
    ageString: fhirtypes.StringType | None
    ageString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    bornDate: fhirtypes.DateType | None
    bornDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    bornPeriod: fhirtypes.PeriodType | None
    bornString: fhirtypes.StringType | None
    bornString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    condition: list[fhirtypes.FamilyMemberHistoryConditionType] | None
    dataAbsentReason: fhirtypes.CodeableConceptType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    deceasedAge: fhirtypes.AgeType | None
    deceasedBoolean: bool | None
    deceasedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    deceasedDate: fhirtypes.DateType | None
    deceasedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    deceasedRange: fhirtypes.RangeType | None
    deceasedString: fhirtypes.StringType | None
    deceasedString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    estimatedAge: bool | None
    estimatedAge__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    instantiatesCanonical: list[fhirtypes.CanonicalType | None] | None
    instantiatesCanonical__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    instantiatesUri: list[fhirtypes.UriType | None] | None
    instantiatesUri__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    participant: list[fhirtypes.FamilyMemberHistoryParticipantType] | None
    patient: fhirtypes.ReferenceType
    procedure: list[fhirtypes.FamilyMemberHistoryProcedureType] | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    relationship: fhirtypes.CodeableConceptType
    sex: fhirtypes.CodeableConceptType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class FamilyMemberHistoryCondition(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    contributedToDeath: bool | None
    contributedToDeath__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    onsetAge: fhirtypes.AgeType | None
    onsetPeriod: fhirtypes.PeriodType | None
    onsetRange: fhirtypes.RangeType | None
    onsetString: fhirtypes.StringType | None
    onsetString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    outcome: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class FamilyMemberHistoryParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class FamilyMemberHistoryProcedure(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    contributedToDeath: bool | None
    contributedToDeath__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    outcome: fhirtypes.CodeableConceptType | None
    performedAge: fhirtypes.AgeType | None
    performedDateTime: fhirtypes.DateTimeType | None
    performedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    performedPeriod: fhirtypes.PeriodType | None
    performedRange: fhirtypes.RangeType | None
    performedString: fhirtypes.StringType | None
    performedString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
