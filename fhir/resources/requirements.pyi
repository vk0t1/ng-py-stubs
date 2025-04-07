from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Requirements(domainresource.DomainResource):
    __resource_type__: str
    actor: list[fhirtypes.CanonicalType | None] | None
    actor__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyrightLabel: fhirtypes.StringType | None
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    derivedFrom: list[fhirtypes.CanonicalType | None] | None
    derivedFrom__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reference: list[fhirtypes.UrlType | None] | None
    reference__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    statement: list[fhirtypes.RequirementsStatementType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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

class RequirementsStatement(backboneelement.BackboneElement):
    __resource_type__: str
    conditionality: bool | None
    conditionality__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    conformance: list[fhirtypes.CodeType | None] | None
    conformance__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    derivedFrom: fhirtypes.StringType | None
    derivedFrom__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    key: fhirtypes.IdType | None
    key__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    label: fhirtypes.StringType | None
    label__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    parent: fhirtypes.StringType | None
    parent__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reference: list[fhirtypes.UrlType | None] | None
    reference__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    requirement: fhirtypes.MarkdownType | None
    requirement__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    satisfiedBy: list[fhirtypes.UrlType | None] | None
    satisfiedBy__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    source: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
