from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ConceptMap(domainresource.DomainResource):
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
    group: list[fhirtypes.ConceptMapGroupType] | None
    identifier: fhirtypes.IdentifierType | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sourceReference: fhirtypes.ReferenceType | None
    sourceUri: fhirtypes.UriType | None
    sourceUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetReference: fhirtypes.ReferenceType | None
    targetUri: fhirtypes.UriType | None
    targetUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ConceptMapGroup(backboneelement.BackboneElement):
    __resource_type__: str
    element: list[fhirtypes.ConceptMapGroupElementType]
    source: fhirtypes.UriType | None
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sourceVersion: fhirtypes.StringType | None
    sourceVersion__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    target: fhirtypes.UriType | None
    target__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetVersion: fhirtypes.StringType | None
    targetVersion__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    unmapped: fhirtypes.ConceptMapGroupUnmappedType | None
    @classmethod
    def elements_sequence(cls): ...

class ConceptMapGroupElement(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    target: list[fhirtypes.ConceptMapGroupElementTargetType] | None
    @classmethod
    def elements_sequence(cls): ...

class ConceptMapGroupElementTarget(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dependsOn: list[fhirtypes.ConceptMapGroupElementTargetDependsOnType] | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    equivalence: fhirtypes.CodeType | None
    equivalence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    product: list[fhirtypes.ConceptMapGroupElementTargetDependsOnType] | None
    @classmethod
    def elements_sequence(cls): ...

class ConceptMapGroupElementTargetDependsOn(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.StringType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    property: fhirtypes.UriType | None
    property__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    system: fhirtypes.UriType | None
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ConceptMapGroupUnmapped(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
