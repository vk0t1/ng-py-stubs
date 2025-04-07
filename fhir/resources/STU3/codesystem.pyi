from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class CodeSystem(domainresource.DomainResource):
    __resource_type__: str
    caseSensitive: bool | None
    caseSensitive__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    compositional: bool | None
    compositional__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    concept: list[fhirtypes.CodeSystemConceptType] | None
    contact: list[fhirtypes.ContactDetailType] | None
    content: fhirtypes.CodeType | None
    content__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    count: fhirtypes.UnsignedIntType | None
    count__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    filter: list[fhirtypes.CodeSystemFilterType] | None
    hierarchyMeaning: fhirtypes.CodeType | None
    hierarchyMeaning__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    property: list[fhirtypes.CodeSystemPropertyType] | None
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
    valueSet: fhirtypes.UriType | None
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    versionNeeded: bool | None
    versionNeeded__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CodeSystemConcept(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    concept: list[fhirtypes.CodeSystemConceptType] | None
    definition: fhirtypes.StringType | None
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    designation: list[fhirtypes.CodeSystemConceptDesignationType] | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    property: list[fhirtypes.CodeSystemConceptPropertyType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CodeSystemConceptDesignation(backboneelement.BackboneElement):
    __resource_type__: str
    language: fhirtypes.CodeType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    use: fhirtypes.CodingType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CodeSystemConceptProperty(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCode: fhirtypes.CodeType | None
    valueCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCoding: fhirtypes.CodingType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class CodeSystemFilter(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    operator: list[fhirtypes.CodeType | None] | None
    operator__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CodeSystemProperty(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uri: fhirtypes.UriType | None
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
