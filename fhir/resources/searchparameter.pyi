from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class SearchParameter(domainresource.DomainResource):
    __resource_type__: str
    base: list[fhirtypes.CodeType | None] | None
    base__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    chain: list[fhirtypes.StringType | None] | None
    chain__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    comparator: list[fhirtypes.CodeType | None] | None
    comparator__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    component: list[fhirtypes.SearchParameterComponentType] | None
    constraint: fhirtypes.StringType | None
    constraint__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyrightLabel: fhirtypes.StringType | None
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    derivedFrom: fhirtypes.CanonicalType | None
    derivedFrom__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    expression: fhirtypes.StringType | None
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    modifier: list[fhirtypes.CodeType | None] | None
    modifier__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    multipleAnd: bool | None
    multipleAnd__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    multipleOr: bool | None
    multipleOr__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    processingMode: fhirtypes.CodeType | None
    processingMode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    target: list[fhirtypes.CodeType | None] | None
    target__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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

class SearchParameterComponent(backboneelement.BackboneElement):
    __resource_type__: str
    definition: fhirtypes.CanonicalType | None
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    expression: fhirtypes.StringType | None
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
