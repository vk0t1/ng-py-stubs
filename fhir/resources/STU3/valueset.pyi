from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ValueSet(domainresource.DomainResource):
    __resource_type__: str
    compose: fhirtypes.ValueSetComposeType | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    expansion: fhirtypes.ValueSetExpansionType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    extensible: bool | None
    extensible__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    immutable: bool | None
    immutable__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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

class ValueSetCompose(backboneelement.BackboneElement):
    __resource_type__: str
    exclude: list[fhirtypes.ValueSetComposeIncludeType] | None
    inactive: bool | None
    inactive__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    include: list[fhirtypes.ValueSetComposeIncludeType]
    lockedDate: fhirtypes.DateType | None
    lockedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ValueSetComposeInclude(backboneelement.BackboneElement):
    __resource_type__: str
    concept: list[fhirtypes.ValueSetComposeIncludeConceptType] | None
    filter: list[fhirtypes.ValueSetComposeIncludeFilterType] | None
    system: fhirtypes.UriType | None
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueSet: list[fhirtypes.UriType | None] | None
    valueSet__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ValueSetComposeIncludeConcept(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    designation: list[fhirtypes.ValueSetComposeIncludeConceptDesignationType] | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ValueSetComposeIncludeConceptDesignation(backboneelement.BackboneElement):
    __resource_type__: str
    language: fhirtypes.CodeType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    use: fhirtypes.CodingType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ValueSetComposeIncludeFilter(backboneelement.BackboneElement):
    __resource_type__: str
    op: fhirtypes.CodeType | None
    op__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    property: fhirtypes.CodeType | None
    property__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    value: fhirtypes.CodeType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ValueSetExpansion(backboneelement.BackboneElement):
    __resource_type__: str
    contains: list[fhirtypes.ValueSetExpansionContainsType] | None
    identifier: fhirtypes.UriType | None
    identifier__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    offset: fhirtypes.IntegerType | None
    offset__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    parameter: list[fhirtypes.ValueSetExpansionParameterType] | None
    timestamp: fhirtypes.DateTimeType | None
    timestamp__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    total: fhirtypes.IntegerType | None
    total__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ValueSetExpansionContains(backboneelement.BackboneElement):
    __resource_type__: str
    abstract: bool | None
    abstract__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contains: list[fhirtypes.ValueSetExpansionContainsType] | None
    designation: list[fhirtypes.ValueSetComposeIncludeConceptDesignationType] | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    inactive: bool | None
    inactive__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    system: fhirtypes.UriType | None
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ValueSetExpansionParameter(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCode: fhirtypes.CodeType | None
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueUri: fhirtypes.UriType | None
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
