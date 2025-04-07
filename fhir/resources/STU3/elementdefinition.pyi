from . import element as element
from . import fhirtypes as fhirtypes

class ElementDefinition(element.Element):
    __resource_type__: str
    alias: list[fhirtypes.StringType | None] | None
    alias__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    base: fhirtypes.ElementDefinitionBaseType | None
    binding: fhirtypes.ElementDefinitionBindingType | None
    code: list[fhirtypes.CodingType] | None
    comment: fhirtypes.MarkdownType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    condition: list[fhirtypes.IdType | None] | None
    condition__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    constraint: list[fhirtypes.ElementDefinitionConstraintType] | None
    contentReference: fhirtypes.UriType | None
    contentReference__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueAddress: fhirtypes.AddressType | None
    defaultValueAge: fhirtypes.AgeType | None
    defaultValueAnnotation: fhirtypes.AnnotationType | None
    defaultValueAttachment: fhirtypes.AttachmentType | None
    defaultValueBase64Binary: fhirtypes.Base64BinaryType | None
    defaultValueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueBoolean: bool | None
    defaultValueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueCode: fhirtypes.CodeType | None
    defaultValueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueCodeableConcept: fhirtypes.CodeableConceptType | None
    defaultValueCoding: fhirtypes.CodingType | None
    defaultValueContactPoint: fhirtypes.ContactPointType | None
    defaultValueCount: fhirtypes.CountType | None
    defaultValueDate: fhirtypes.DateType | None
    defaultValueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueDateTime: fhirtypes.DateTimeType | None
    defaultValueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueDecimal: fhirtypes.DecimalType | None
    defaultValueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueDistance: fhirtypes.DistanceType | None
    defaultValueDuration: fhirtypes.DurationType | None
    defaultValueHumanName: fhirtypes.HumanNameType | None
    defaultValueId: fhirtypes.IdType | None
    defaultValueId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueIdentifier: fhirtypes.IdentifierType | None
    defaultValueInstant: fhirtypes.InstantType | None
    defaultValueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueInteger: fhirtypes.IntegerType | None
    defaultValueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueMarkdown: fhirtypes.MarkdownType | None
    defaultValueMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueMeta: fhirtypes.MetaType | None
    defaultValueMoney: fhirtypes.MoneyType | None
    defaultValueOid: fhirtypes.OidType | None
    defaultValueOid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValuePeriod: fhirtypes.PeriodType | None
    defaultValuePositiveInt: fhirtypes.PositiveIntType | None
    defaultValuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueQuantity: fhirtypes.QuantityType | None
    defaultValueRange: fhirtypes.RangeType | None
    defaultValueRatio: fhirtypes.RatioType | None
    defaultValueReference: fhirtypes.ReferenceType | None
    defaultValueSampledData: fhirtypes.SampledDataType | None
    defaultValueSignature: fhirtypes.SignatureType | None
    defaultValueString: fhirtypes.StringType | None
    defaultValueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueTime: fhirtypes.TimeType | None
    defaultValueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueTiming: fhirtypes.TimingType | None
    defaultValueUnsignedInt: fhirtypes.UnsignedIntType | None
    defaultValueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    defaultValueUri: fhirtypes.UriType | None
    defaultValueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    definition: fhirtypes.MarkdownType | None
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    example: list[fhirtypes.ElementDefinitionExampleType] | None
    fixedAddress: fhirtypes.AddressType | None
    fixedAge: fhirtypes.AgeType | None
    fixedAnnotation: fhirtypes.AnnotationType | None
    fixedAttachment: fhirtypes.AttachmentType | None
    fixedBase64Binary: fhirtypes.Base64BinaryType | None
    fixedBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedBoolean: bool | None
    fixedBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedCode: fhirtypes.CodeType | None
    fixedCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedCodeableConcept: fhirtypes.CodeableConceptType | None
    fixedCoding: fhirtypes.CodingType | None
    fixedContactPoint: fhirtypes.ContactPointType | None
    fixedCount: fhirtypes.CountType | None
    fixedDate: fhirtypes.DateType | None
    fixedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedDateTime: fhirtypes.DateTimeType | None
    fixedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedDecimal: fhirtypes.DecimalType | None
    fixedDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedDistance: fhirtypes.DistanceType | None
    fixedDuration: fhirtypes.DurationType | None
    fixedHumanName: fhirtypes.HumanNameType | None
    fixedId: fhirtypes.IdType | None
    fixedId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedIdentifier: fhirtypes.IdentifierType | None
    fixedInstant: fhirtypes.InstantType | None
    fixedInstant__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedInteger: fhirtypes.IntegerType | None
    fixedInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedMarkdown: fhirtypes.MarkdownType | None
    fixedMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedMeta: fhirtypes.MetaType | None
    fixedMoney: fhirtypes.MoneyType | None
    fixedOid: fhirtypes.OidType | None
    fixedOid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedPeriod: fhirtypes.PeriodType | None
    fixedPositiveInt: fhirtypes.PositiveIntType | None
    fixedPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedQuantity: fhirtypes.QuantityType | None
    fixedRange: fhirtypes.RangeType | None
    fixedRatio: fhirtypes.RatioType | None
    fixedReference: fhirtypes.ReferenceType | None
    fixedSampledData: fhirtypes.SampledDataType | None
    fixedSignature: fhirtypes.SignatureType | None
    fixedString: fhirtypes.StringType | None
    fixedString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedTime: fhirtypes.TimeType | None
    fixedTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedTiming: fhirtypes.TimingType | None
    fixedUnsignedInt: fhirtypes.UnsignedIntType | None
    fixedUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedUri: fhirtypes.UriType | None
    fixedUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    isModifier: bool | None
    isModifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    isSummary: bool | None
    isSummary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    label: fhirtypes.StringType | None
    label__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    mapping: list[fhirtypes.ElementDefinitionMappingType] | None
    max: fhirtypes.StringType | None
    max__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxLength: fhirtypes.IntegerType | None
    maxLength__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxValueDate: fhirtypes.DateType | None
    maxValueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxValueDateTime: fhirtypes.DateTimeType | None
    maxValueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxValueDecimal: fhirtypes.DecimalType | None
    maxValueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxValueInstant: fhirtypes.InstantType | None
    maxValueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxValueInteger: fhirtypes.IntegerType | None
    maxValueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxValuePositiveInt: fhirtypes.PositiveIntType | None
    maxValuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxValueQuantity: fhirtypes.QuantityType | None
    maxValueTime: fhirtypes.TimeType | None
    maxValueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxValueUnsignedInt: fhirtypes.UnsignedIntType | None
    maxValueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    meaningWhenMissing: fhirtypes.MarkdownType | None
    meaningWhenMissing__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    min: fhirtypes.UnsignedIntType | None
    min__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    minValueDate: fhirtypes.DateType | None
    minValueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    minValueDateTime: fhirtypes.DateTimeType | None
    minValueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    minValueDecimal: fhirtypes.DecimalType | None
    minValueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    minValueInstant: fhirtypes.InstantType | None
    minValueInstant__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    minValueInteger: fhirtypes.IntegerType | None
    minValueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    minValuePositiveInt: fhirtypes.PositiveIntType | None
    minValuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    minValueQuantity: fhirtypes.QuantityType | None
    minValueTime: fhirtypes.TimeType | None
    minValueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    minValueUnsignedInt: fhirtypes.UnsignedIntType | None
    minValueUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    mustSupport: bool | None
    mustSupport__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    orderMeaning: fhirtypes.StringType | None
    orderMeaning__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternAddress: fhirtypes.AddressType | None
    patternAge: fhirtypes.AgeType | None
    patternAnnotation: fhirtypes.AnnotationType | None
    patternAttachment: fhirtypes.AttachmentType | None
    patternBase64Binary: fhirtypes.Base64BinaryType | None
    patternBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternBoolean: bool | None
    patternBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternCode: fhirtypes.CodeType | None
    patternCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternCodeableConcept: fhirtypes.CodeableConceptType | None
    patternCoding: fhirtypes.CodingType | None
    patternContactPoint: fhirtypes.ContactPointType | None
    patternCount: fhirtypes.CountType | None
    patternDate: fhirtypes.DateType | None
    patternDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternDateTime: fhirtypes.DateTimeType | None
    patternDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternDecimal: fhirtypes.DecimalType | None
    patternDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternDistance: fhirtypes.DistanceType | None
    patternDuration: fhirtypes.DurationType | None
    patternHumanName: fhirtypes.HumanNameType | None
    patternId: fhirtypes.IdType | None
    patternId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternIdentifier: fhirtypes.IdentifierType | None
    patternInstant: fhirtypes.InstantType | None
    patternInstant__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternInteger: fhirtypes.IntegerType | None
    patternInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternMarkdown: fhirtypes.MarkdownType | None
    patternMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternMeta: fhirtypes.MetaType | None
    patternMoney: fhirtypes.MoneyType | None
    patternOid: fhirtypes.OidType | None
    patternOid__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternPeriod: fhirtypes.PeriodType | None
    patternPositiveInt: fhirtypes.PositiveIntType | None
    patternPositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternQuantity: fhirtypes.QuantityType | None
    patternRange: fhirtypes.RangeType | None
    patternRatio: fhirtypes.RatioType | None
    patternReference: fhirtypes.ReferenceType | None
    patternSampledData: fhirtypes.SampledDataType | None
    patternSignature: fhirtypes.SignatureType | None
    patternString: fhirtypes.StringType | None
    patternString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternTime: fhirtypes.TimeType | None
    patternTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternTiming: fhirtypes.TimingType | None
    patternUnsignedInt: fhirtypes.UnsignedIntType | None
    patternUnsignedInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patternUri: fhirtypes.UriType | None
    patternUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    representation: list[fhirtypes.CodeType | None] | None
    representation__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    requirements: fhirtypes.MarkdownType | None
    requirements__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    short: fhirtypes.StringType | None
    short__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sliceName: fhirtypes.StringType | None
    sliceName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    slicing: fhirtypes.ElementDefinitionSlicingType | None
    type: list[fhirtypes.ElementDefinitionTypeType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ElementDefinitionBase(element.Element):
    __resource_type__: str
    max: fhirtypes.StringType | None
    max__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    min: fhirtypes.UnsignedIntType | None
    min__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ElementDefinitionBinding(element.Element):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    strength: fhirtypes.CodeType | None
    strength__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueSetReference: fhirtypes.ReferenceType | None
    valueSetUri: fhirtypes.UriType | None
    valueSetUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ElementDefinitionConstraint(element.Element):
    __resource_type__: str
    expression: fhirtypes.StringType | None
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    human: fhirtypes.StringType | None
    human__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    key: fhirtypes.IdType | None
    key__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    requirements: fhirtypes.StringType | None
    requirements__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    severity: fhirtypes.CodeType | None
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    source: fhirtypes.UriType | None
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    xpath: fhirtypes.StringType | None
    xpath__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ElementDefinitionExample(element.Element):
    __resource_type__: str
    label: fhirtypes.StringType | None
    label__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ElementDefinitionMapping(element.Element):
    __resource_type__: str
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identity: fhirtypes.IdType | None
    identity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    language: fhirtypes.CodeType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    map: fhirtypes.StringType | None
    map__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ElementDefinitionSlicing(element.Element):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    discriminator: list[fhirtypes.ElementDefinitionSlicingDiscriminatorType] | None
    ordered: bool | None
    ordered__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rules: fhirtypes.CodeType | None
    rules__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ElementDefinitionSlicingDiscriminator(element.Element):
    __resource_type__: str
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ElementDefinitionType(element.Element):
    __resource_type__: str
    aggregation: list[fhirtypes.CodeType | None] | None
    aggregation__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    code: fhirtypes.UriType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    profile: fhirtypes.UriType | None
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetProfile: fhirtypes.UriType | None
    targetProfile__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    versioning: fhirtypes.CodeType | None
    versioning__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
