from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class StructureMap(domainresource.DomainResource):
    __resource_type__: str
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    group: list[fhirtypes.StructureMapGroupType]
    identifier: list[fhirtypes.IdentifierType] | None
    import_fhir: list[fhirtypes.UriType | None] | None
    import__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    structure: list[fhirtypes.StructureMapStructureType] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class StructureMapGroup(backboneelement.BackboneElement):
    __resource_type__: str
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    extends: fhirtypes.IdType | None
    extends__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    input: list[fhirtypes.StructureMapGroupInputType]
    name: fhirtypes.IdType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rule: list[fhirtypes.StructureMapGroupRuleType]
    typeMode: fhirtypes.CodeType | None
    typeMode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class StructureMapGroupInput(backboneelement.BackboneElement):
    __resource_type__: str
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.IdType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.StringType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class StructureMapGroupRule(backboneelement.BackboneElement):
    __resource_type__: str
    dependent: list[fhirtypes.StructureMapGroupRuleDependentType] | None
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.IdType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rule: list[fhirtypes.StructureMapGroupRuleType] | None
    source: list[fhirtypes.StructureMapGroupRuleSourceType]
    target: list[fhirtypes.StructureMapGroupRuleTargetType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class StructureMapGroupRuleDependent(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.IdType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    variable: list[fhirtypes.StringType | None] | None
    variable__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class StructureMapGroupRuleSource(backboneelement.BackboneElement):
    __resource_type__: str
    check: fhirtypes.StringType | None
    check__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    condition: fhirtypes.StringType | None
    condition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    context: fhirtypes.IdType | None
    context__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    element: fhirtypes.StringType | None
    element__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    listMode: fhirtypes.CodeType | None
    listMode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    max: fhirtypes.StringType | None
    max__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    min: fhirtypes.IntegerType | None
    min__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.StringType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    variable: fhirtypes.IdType | None
    variable__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    __resource_type__: str
    context: fhirtypes.IdType | None
    context__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contextType: fhirtypes.CodeType | None
    contextType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    element: fhirtypes.StringType | None
    element__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    listMode: list[fhirtypes.CodeType | None] | None
    listMode__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    listRuleId: fhirtypes.IdType | None
    listRuleId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    parameter: list[fhirtypes.StructureMapGroupRuleTargetParameterType] | None
    transform: fhirtypes.CodeType | None
    transform__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    variable: fhirtypes.IdType | None
    variable__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class StructureMapGroupRuleTargetParameter(backboneelement.BackboneElement):
    __resource_type__: str
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueId: fhirtypes.IdType | None
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class StructureMapStructure(backboneelement.BackboneElement):
    __resource_type__: str
    alias: fhirtypes.StringType | None
    alias__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
