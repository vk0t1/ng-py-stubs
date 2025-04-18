from . import datatype as datatype
from . import fhirtypes as fhirtypes

class Extension(datatype.DataType):
    __resource_type__: str
    url: fhirtypes.UriType | None
    valueAddress: fhirtypes.AddressType | None
    valueAge: fhirtypes.AgeType | None
    valueAnnotation: fhirtypes.AnnotationType | None
    valueAttachment: fhirtypes.AttachmentType | None
    valueAvailability: fhirtypes.AvailabilityType | None
    valueBase64Binary: fhirtypes.Base64BinaryType | None
    valueBoolean: bool | None
    valueCanonical: fhirtypes.CanonicalType | None
    valueCode: fhirtypes.CodeType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueCodeableReference: fhirtypes.CodeableReferenceType | None
    valueCoding: fhirtypes.CodingType | None
    valueContactDetail: fhirtypes.ContactDetailType | None
    valueContactPoint: fhirtypes.ContactPointType | None
    valueCount: fhirtypes.CountType | None
    valueDataRequirement: fhirtypes.DataRequirementType | None
    valueDate: fhirtypes.DateType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDistance: fhirtypes.DistanceType | None
    valueDosage: fhirtypes.DosageType | None
    valueDuration: fhirtypes.DurationType | None
    valueExpression: fhirtypes.ExpressionType | None
    valueExtendedContactDetail: fhirtypes.ExtendedContactDetailType | None
    valueHumanName: fhirtypes.HumanNameType | None
    valueId: fhirtypes.IdType | None
    valueIdentifier: fhirtypes.IdentifierType | None
    valueInstant: fhirtypes.InstantType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger64: fhirtypes.Integer64Type | None
    valueMarkdown: fhirtypes.MarkdownType | None
    valueMeta: fhirtypes.MetaType | None
    valueMoney: fhirtypes.MoneyType | None
    valueOid: fhirtypes.OidType | None
    valueParameterDefinition: fhirtypes.ParameterDefinitionType | None
    valuePeriod: fhirtypes.PeriodType | None
    valuePositiveInt: fhirtypes.PositiveIntType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueRatio: fhirtypes.RatioType | None
    valueRatioRange: fhirtypes.RatioRangeType | None
    valueReference: fhirtypes.ReferenceType | None
    valueRelatedArtifact: fhirtypes.RelatedArtifactType | None
    valueSampledData: fhirtypes.SampledDataType | None
    valueSignature: fhirtypes.SignatureType | None
    valueString: fhirtypes.StringType | None
    valueTime: fhirtypes.TimeType | None
    valueTiming: fhirtypes.TimingType | None
    valueTriggerDefinition: fhirtypes.TriggerDefinitionType | None
    valueUnsignedInt: fhirtypes.UnsignedIntType | None
    valueUri: fhirtypes.UriType | None
    valueUrl: fhirtypes.UrlType | None
    valueUsageContext: fhirtypes.UsageContextType | None
    valueUuid: fhirtypes.UuidType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
