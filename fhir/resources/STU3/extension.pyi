from . import element as element
from . import fhirtypes as fhirtypes

class Extension(element.Element):
    __resource_type__: str
    url: fhirtypes.UriType | None
    valueAddress: fhirtypes.AddressType | None
    valueAge: fhirtypes.AgeType | None
    valueAnnotation: fhirtypes.AnnotationType | None
    valueAttachment: fhirtypes.AttachmentType | None
    valueBase64Binary: fhirtypes.Base64BinaryType | None
    valueBoolean: bool | None
    valueCode: fhirtypes.CodeType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueCoding: fhirtypes.CodingType | None
    valueContactPoint: fhirtypes.ContactPointType | None
    valueCount: fhirtypes.CountType | None
    valueDate: fhirtypes.DateType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDistance: fhirtypes.DistanceType | None
    valueDuration: fhirtypes.DurationType | None
    valueHumanName: fhirtypes.HumanNameType | None
    valueId: fhirtypes.IdType | None
    valueIdentifier: fhirtypes.IdentifierType | None
    valueInstant: fhirtypes.InstantType | None
    valueInteger: fhirtypes.IntegerType | None
    valueMarkdown: fhirtypes.MarkdownType | None
    valueMeta: fhirtypes.MetaType | None
    valueMoney: fhirtypes.MoneyType | None
    valueOid: fhirtypes.OidType | None
    valuePeriod: fhirtypes.PeriodType | None
    valuePositiveInt: fhirtypes.PositiveIntType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueRatio: fhirtypes.RatioType | None
    valueReference: fhirtypes.ReferenceType | None
    valueSampledData: fhirtypes.SampledDataType | None
    valueSignature: fhirtypes.SignatureType | None
    valueString: fhirtypes.StringType | None
    valueTime: fhirtypes.TimeType | None
    valueTiming: fhirtypes.TimingType | None
    valueUnsignedInt: fhirtypes.UnsignedIntType | None
    valueUri: fhirtypes.UriType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
