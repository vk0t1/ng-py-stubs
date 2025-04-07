from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Task(domainresource.DomainResource):
    __resource_type__: str
    authoredOn: fhirtypes.DateTimeType | None
    authoredOn__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    businessStatus: fhirtypes.CodeableConceptType | None
    code: fhirtypes.CodeableConceptType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    doNotPerform: bool | None
    doNotPerform__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    executionPeriod: fhirtypes.PeriodType | None
    focus: fhirtypes.ReferenceType | None
    for_fhir: fhirtypes.ReferenceType | None
    groupIdentifier: fhirtypes.IdentifierType | None
    identifier: list[fhirtypes.IdentifierType] | None
    input: list[fhirtypes.TaskInputType] | None
    instantiatesCanonical: fhirtypes.CanonicalType | None
    instantiatesCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    instantiatesUri: fhirtypes.UriType | None
    instantiatesUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    insurance: list[fhirtypes.ReferenceType] | None
    intent: fhirtypes.CodeType | None
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    lastModified: fhirtypes.DateTimeType | None
    lastModified__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    location: fhirtypes.ReferenceType | None
    note: list[fhirtypes.AnnotationType] | None
    output: list[fhirtypes.TaskOutputType] | None
    owner: fhirtypes.ReferenceType | None
    partOf: list[fhirtypes.ReferenceType] | None
    performer: list[fhirtypes.TaskPerformerType] | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    relevantHistory: list[fhirtypes.ReferenceType] | None
    requestedPerformer: list[fhirtypes.CodeableReferenceType] | None
    requestedPeriod: fhirtypes.PeriodType | None
    requester: fhirtypes.ReferenceType | None
    restriction: fhirtypes.TaskRestrictionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.CodeableReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TaskInput(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueAddress: fhirtypes.AddressType | None
    valueAge: fhirtypes.AgeType | None
    valueAnnotation: fhirtypes.AnnotationType | None
    valueAttachment: fhirtypes.AttachmentType | None
    valueAvailability: fhirtypes.AvailabilityType | None
    valueBase64Binary: fhirtypes.Base64BinaryType | None
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCanonical: fhirtypes.CanonicalType | None
    valueCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCode: fhirtypes.CodeType | None
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueCodeableReference: fhirtypes.CodeableReferenceType | None
    valueCoding: fhirtypes.CodingType | None
    valueContactDetail: fhirtypes.ContactDetailType | None
    valueContactPoint: fhirtypes.ContactPointType | None
    valueCount: fhirtypes.CountType | None
    valueDataRequirement: fhirtypes.DataRequirementType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDistance: fhirtypes.DistanceType | None
    valueDosage: fhirtypes.DosageType | None
    valueDuration: fhirtypes.DurationType | None
    valueExpression: fhirtypes.ExpressionType | None
    valueExtendedContactDetail: fhirtypes.ExtendedContactDetailType | None
    valueHumanName: fhirtypes.HumanNameType | None
    valueId: fhirtypes.IdType | None
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueIdentifier: fhirtypes.IdentifierType | None
    valueInstant: fhirtypes.InstantType | None
    valueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger64: fhirtypes.Integer64Type | None
    valueInteger64__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueMarkdown: fhirtypes.MarkdownType | None
    valueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueMeta: fhirtypes.MetaType | None
    valueMoney: fhirtypes.MoneyType | None
    valueOid: fhirtypes.OidType | None
    valueOid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueParameterDefinition: fhirtypes.ParameterDefinitionType | None
    valuePeriod: fhirtypes.PeriodType | None
    valuePositiveInt: fhirtypes.PositiveIntType | None
    valuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueRatio: fhirtypes.RatioType | None
    valueRatioRange: fhirtypes.RatioRangeType | None
    valueReference: fhirtypes.ReferenceType | None
    valueRelatedArtifact: fhirtypes.RelatedArtifactType | None
    valueSampledData: fhirtypes.SampledDataType | None
    valueSignature: fhirtypes.SignatureType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTime: fhirtypes.TimeType | None
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTiming: fhirtypes.TimingType | None
    valueTriggerDefinition: fhirtypes.TriggerDefinitionType | None
    valueUnsignedInt: fhirtypes.UnsignedIntType | None
    valueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueUri: fhirtypes.UriType | None
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueUrl: fhirtypes.UrlType | None
    valueUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueUsageContext: fhirtypes.UsageContextType | None
    valueUuid: fhirtypes.UuidType | None
    valueUuid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class TaskOutput(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueAddress: fhirtypes.AddressType | None
    valueAge: fhirtypes.AgeType | None
    valueAnnotation: fhirtypes.AnnotationType | None
    valueAttachment: fhirtypes.AttachmentType | None
    valueAvailability: fhirtypes.AvailabilityType | None
    valueBase64Binary: fhirtypes.Base64BinaryType | None
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCanonical: fhirtypes.CanonicalType | None
    valueCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCode: fhirtypes.CodeType | None
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueCodeableReference: fhirtypes.CodeableReferenceType | None
    valueCoding: fhirtypes.CodingType | None
    valueContactDetail: fhirtypes.ContactDetailType | None
    valueContactPoint: fhirtypes.ContactPointType | None
    valueCount: fhirtypes.CountType | None
    valueDataRequirement: fhirtypes.DataRequirementType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDistance: fhirtypes.DistanceType | None
    valueDosage: fhirtypes.DosageType | None
    valueDuration: fhirtypes.DurationType | None
    valueExpression: fhirtypes.ExpressionType | None
    valueExtendedContactDetail: fhirtypes.ExtendedContactDetailType | None
    valueHumanName: fhirtypes.HumanNameType | None
    valueId: fhirtypes.IdType | None
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueIdentifier: fhirtypes.IdentifierType | None
    valueInstant: fhirtypes.InstantType | None
    valueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger64: fhirtypes.Integer64Type | None
    valueInteger64__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueMarkdown: fhirtypes.MarkdownType | None
    valueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueMeta: fhirtypes.MetaType | None
    valueMoney: fhirtypes.MoneyType | None
    valueOid: fhirtypes.OidType | None
    valueOid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueParameterDefinition: fhirtypes.ParameterDefinitionType | None
    valuePeriod: fhirtypes.PeriodType | None
    valuePositiveInt: fhirtypes.PositiveIntType | None
    valuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueRatio: fhirtypes.RatioType | None
    valueRatioRange: fhirtypes.RatioRangeType | None
    valueReference: fhirtypes.ReferenceType | None
    valueRelatedArtifact: fhirtypes.RelatedArtifactType | None
    valueSampledData: fhirtypes.SampledDataType | None
    valueSignature: fhirtypes.SignatureType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTime: fhirtypes.TimeType | None
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTiming: fhirtypes.TimingType | None
    valueTriggerDefinition: fhirtypes.TriggerDefinitionType | None
    valueUnsignedInt: fhirtypes.UnsignedIntType | None
    valueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueUri: fhirtypes.UriType | None
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueUrl: fhirtypes.UrlType | None
    valueUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueUsageContext: fhirtypes.UsageContextType | None
    valueUuid: fhirtypes.UuidType | None
    valueUuid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class TaskPerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class TaskRestriction(backboneelement.BackboneElement):
    __resource_type__: str
    period: fhirtypes.PeriodType | None
    recipient: list[fhirtypes.ReferenceType] | None
    repetitions: fhirtypes.PositiveIntType | None
    repetitions__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
