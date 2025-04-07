from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class StructureMap(domainresource.DomainResource):
    __resource_type__: str
    const: list[fhirtypes.StructureMapConstType] | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyrightLabel: fhirtypes.StringType | None
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    group: list[fhirtypes.StructureMapGroupType]
    identifier: list[fhirtypes.IdentifierType] | None
    import_fhir: list[fhirtypes.CanonicalType | None] | None
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
    versionAlgorithmCoding: fhirtypes.CodingType | None
    versionAlgorithmString: fhirtypes.StringType | None
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class StructureMapConst(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.IdType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class StructureMapGroup(backboneelement.BackboneElement):
    __resource_type__: str
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    extends: fhirtypes.IdType | None
    extends__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    input: list[fhirtypes.StructureMapGroupInputType]
    name: fhirtypes.IdType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rule: list[fhirtypes.StructureMapGroupRuleType] | None
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

class StructureMapGroupRuleDependent(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.IdType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    parameter: list[fhirtypes.StructureMapGroupRuleTargetParameterType]
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
    defaultValue: fhirtypes.StringType | None
    defaultValue__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    element: fhirtypes.StringType | None
    element__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    listMode: fhirtypes.CodeType | None
    listMode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    logMessage: fhirtypes.StringType | None
    logMessage__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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

class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    __resource_type__: str
    context: fhirtypes.StringType | None
    context__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueId: fhirtypes.IdType | None
    valueId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTime: fhirtypes.TimeType | None
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    url: fhirtypes.CanonicalType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
