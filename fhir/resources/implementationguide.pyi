from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ImplementationGuide(domainresource.DomainResource):
    __resource_type__: str
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyrightLabel: fhirtypes.StringType | None
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    definition: fhirtypes.ImplementationGuideDefinitionType | None
    dependsOn: list[fhirtypes.ImplementationGuideDependsOnType] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fhirVersion: list[fhirtypes.CodeType | None] | None
    fhirVersion__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    global_fhir: list[fhirtypes.ImplementationGuideGlobalType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    license: fhirtypes.CodeType | None
    license__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    manifest: fhirtypes.ImplementationGuideManifestType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    packageId: fhirtypes.IdType | None
    packageId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    versionAlgorithmCoding: fhirtypes.CodingType | None
    versionAlgorithmString: fhirtypes.StringType | None
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ImplementationGuideDefinition(backboneelement.BackboneElement):
    __resource_type__: str
    grouping: list[fhirtypes.ImplementationGuideDefinitionGroupingType] | None
    page: fhirtypes.ImplementationGuideDefinitionPageType | None
    parameter: list[fhirtypes.ImplementationGuideDefinitionParameterType] | None
    resource: list[fhirtypes.ImplementationGuideDefinitionResourceType] | None
    template: list[fhirtypes.ImplementationGuideDefinitionTemplateType] | None
    @classmethod
    def elements_sequence(cls): ...

class ImplementationGuideDefinitionGrouping(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImplementationGuideDefinitionPage(backboneelement.BackboneElement):
    __resource_type__: str
    generation: fhirtypes.CodeType | None
    generation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.UrlType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    page: list[fhirtypes.ImplementationGuideDefinitionPageType] | None
    sourceMarkdown: fhirtypes.MarkdownType | None
    sourceMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sourceString: fhirtypes.StringType | None
    sourceString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sourceUrl: fhirtypes.UrlType | None
    sourceUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ImplementationGuideDefinitionParameter(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodingType
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImplementationGuideDefinitionResource(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fhirVersion: list[fhirtypes.CodeType | None] | None
    fhirVersion__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    groupingId: fhirtypes.IdType | None
    groupingId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    isExample: bool | None
    isExample__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    profile: list[fhirtypes.CanonicalType | None] | None
    profile__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    reference: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...

class ImplementationGuideDefinitionTemplate(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    scope: fhirtypes.StringType | None
    scope__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    source: fhirtypes.StringType | None
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImplementationGuideDependsOn(backboneelement.BackboneElement):
    __resource_type__: str
    packageId: fhirtypes.IdType | None
    packageId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reason: fhirtypes.MarkdownType | None
    reason__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uri: fhirtypes.CanonicalType | None
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImplementationGuideGlobal(backboneelement.BackboneElement):
    __resource_type__: str
    profile: fhirtypes.CanonicalType | None
    profile__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImplementationGuideManifest(backboneelement.BackboneElement):
    __resource_type__: str
    image: list[fhirtypes.StringType | None] | None
    image__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    other: list[fhirtypes.StringType | None] | None
    other__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    page: list[fhirtypes.ImplementationGuideManifestPageType] | None
    rendering: fhirtypes.UrlType | None
    rendering__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resource: list[fhirtypes.ImplementationGuideManifestResourceType]
    @classmethod
    def elements_sequence(cls): ...

class ImplementationGuideManifestPage(backboneelement.BackboneElement):
    __resource_type__: str
    anchor: list[fhirtypes.StringType | None] | None
    anchor__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ImplementationGuideManifestResource(backboneelement.BackboneElement):
    __resource_type__: str
    isExample: bool | None
    isExample__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    profile: list[fhirtypes.CanonicalType | None] | None
    profile__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    reference: fhirtypes.ReferenceType
    relativePath: fhirtypes.UrlType | None
    relativePath__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
