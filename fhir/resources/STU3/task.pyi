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
    context: fhirtypes.ReferenceType | None
    definitionReference: fhirtypes.ReferenceType | None
    definitionUri: fhirtypes.UriType | None
    definitionUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    executionPeriod: fhirtypes.PeriodType | None
    focus: fhirtypes.ReferenceType | None
    for_fhir: fhirtypes.ReferenceType | None
    groupIdentifier: fhirtypes.IdentifierType | None
    identifier: list[fhirtypes.IdentifierType] | None
    input: list[fhirtypes.TaskInputType] | None
    intent: fhirtypes.CodeType | None
    intent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    lastModified: fhirtypes.DateTimeType | None
    lastModified__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    output: list[fhirtypes.TaskOutputType] | None
    owner: fhirtypes.ReferenceType | None
    partOf: list[fhirtypes.ReferenceType] | None
    performerType: list[fhirtypes.CodeableConceptType] | None
    priority: fhirtypes.CodeType | None
    priority__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reason: fhirtypes.CodeableConceptType | None
    relevantHistory: list[fhirtypes.ReferenceType] | None
    requester: fhirtypes.TaskRequesterType | None
    restriction: fhirtypes.TaskRestrictionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusReason: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class TaskInput(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueAddress: fhirtypes.AddressType | None
    valueAge: fhirtypes.AgeType | None
    valueAnnotation: fhirtypes.AnnotationType | None
    valueAttachment: fhirtypes.AttachmentType | None
    valueBase64Binary: fhirtypes.Base64BinaryType | None
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCode: fhirtypes.CodeType | None
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueCoding: fhirtypes.CodingType | None
    valueContactPoint: fhirtypes.ContactPointType | None
    valueCount: fhirtypes.CountType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDistance: fhirtypes.DistanceType | None
    valueDuration: fhirtypes.DurationType | None
    valueHumanName: fhirtypes.HumanNameType | None
    valueId: fhirtypes.IdType | None
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueIdentifier: fhirtypes.IdentifierType | None
    valueInstant: fhirtypes.InstantType | None
    valueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueMarkdown: fhirtypes.MarkdownType | None
    valueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueMeta: fhirtypes.MetaType | None
    valueMoney: fhirtypes.MoneyType | None
    valueOid: fhirtypes.OidType | None
    valueOid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valuePeriod: fhirtypes.PeriodType | None
    valuePositiveInt: fhirtypes.PositiveIntType | None
    valuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueRatio: fhirtypes.RatioType | None
    valueReference: fhirtypes.ReferenceType | None
    valueSampledData: fhirtypes.SampledDataType | None
    valueSignature: fhirtypes.SignatureType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTime: fhirtypes.TimeType | None
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTiming: fhirtypes.TimingType | None
    valueUnsignedInt: fhirtypes.UnsignedIntType | None
    valueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueUri: fhirtypes.UriType | None
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    valueBase64Binary: fhirtypes.Base64BinaryType | None
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCode: fhirtypes.CodeType | None
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueCoding: fhirtypes.CodingType | None
    valueContactPoint: fhirtypes.ContactPointType | None
    valueCount: fhirtypes.CountType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDistance: fhirtypes.DistanceType | None
    valueDuration: fhirtypes.DurationType | None
    valueHumanName: fhirtypes.HumanNameType | None
    valueId: fhirtypes.IdType | None
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueIdentifier: fhirtypes.IdentifierType | None
    valueInstant: fhirtypes.InstantType | None
    valueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueMarkdown: fhirtypes.MarkdownType | None
    valueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueMeta: fhirtypes.MetaType | None
    valueMoney: fhirtypes.MoneyType | None
    valueOid: fhirtypes.OidType | None
    valueOid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valuePeriod: fhirtypes.PeriodType | None
    valuePositiveInt: fhirtypes.PositiveIntType | None
    valuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueRatio: fhirtypes.RatioType | None
    valueReference: fhirtypes.ReferenceType | None
    valueSampledData: fhirtypes.SampledDataType | None
    valueSignature: fhirtypes.SignatureType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTime: fhirtypes.TimeType | None
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTiming: fhirtypes.TimingType | None
    valueUnsignedInt: fhirtypes.UnsignedIntType | None
    valueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueUri: fhirtypes.UriType | None
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class TaskRequester(backboneelement.BackboneElement):
    __resource_type__: str
    agent: fhirtypes.ReferenceType
    onBehalfOf: fhirtypes.ReferenceType | None
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
