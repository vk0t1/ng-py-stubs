from . import backboneelement as backboneelement
from . import fhirtypes as fhirtypes
from . import resource as resource

class Parameters(resource.Resource):
    __resource_type__: str
    parameter: list[fhirtypes.ParametersParameterType] | None
    @classmethod
    def elements_sequence(cls): ...

class ParametersParameter(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    part: list[fhirtypes.ParametersParameterType] | None
    resource: fhirtypes.ResourceType | None
    valueAddress: fhirtypes.AddressType | None
    valueAge: fhirtypes.AgeType | None
    valueAnnotation: fhirtypes.AnnotationType | None
    valueAttachment: fhirtypes.AttachmentType | None
    valueBase64Binary: fhirtypes.Base64BinaryType | None
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCanonical: fhirtypes.CanonicalType | None
    valueCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCode: fhirtypes.CodeType | None
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueCoding: fhirtypes.CodingType | None
    valueContactDetail: fhirtypes.ContactDetailType | None
    valueContactPoint: fhirtypes.ContactPointType | None
    valueContributor: fhirtypes.ContributorType | None
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
    valueParameterDefinition: fhirtypes.ParameterDefinitionType | None
    valuePeriod: fhirtypes.PeriodType | None
    valuePositiveInt: fhirtypes.PositiveIntType | None
    valuePositiveInt__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    valueRatio: fhirtypes.RatioType | None
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
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
