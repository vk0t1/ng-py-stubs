from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class StructureDefinition(domainresource.DomainResource):
    __resource_type__: str
    abstract: bool | None
    abstract__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    baseDefinition: fhirtypes.UriType | None
    baseDefinition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contact: list[fhirtypes.ContactDetailType] | None
    context: list[fhirtypes.StringType | None] | None
    context__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    contextInvariant: list[fhirtypes.StringType | None] | None
    contextInvariant__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    contextType: fhirtypes.CodeType | None
    contextType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    derivation: fhirtypes.CodeType | None
    derivation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    differential: fhirtypes.StructureDefinitionDifferentialType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fhirVersion: fhirtypes.IdType | None
    fhirVersion__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    keyword: list[fhirtypes.CodingType] | None
    kind: fhirtypes.CodeType | None
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    mapping: list[fhirtypes.StructureDefinitionMappingType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    snapshot: fhirtypes.StructureDefinitionSnapshotType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class StructureDefinitionDifferential(backboneelement.BackboneElement):
    __resource_type__: str
    element: list[fhirtypes.ElementDefinitionType]
    @classmethod
    def elements_sequence(cls): ...

class StructureDefinitionMapping(backboneelement.BackboneElement):
    __resource_type__: str
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identity: fhirtypes.IdType | None
    identity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uri: fhirtypes.UriType | None
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    __resource_type__: str
    element: list[fhirtypes.ElementDefinitionType]
    @classmethod
    def elements_sequence(cls): ...
