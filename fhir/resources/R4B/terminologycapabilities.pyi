from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class TerminologyCapabilities(domainresource.DomainResource):
    __resource_type__: str
    closure: fhirtypes.TerminologyCapabilitiesClosureType | None
    codeSearch: fhirtypes.CodeType | None
    codeSearch__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    codeSystem: list[fhirtypes.TerminologyCapabilitiesCodeSystemType] | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    expansion: fhirtypes.TerminologyCapabilitiesExpansionType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    implementation: fhirtypes.TerminologyCapabilitiesImplementationType | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    kind: fhirtypes.CodeType | None
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    lockedDate: bool | None
    lockedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    software: fhirtypes.TerminologyCapabilitiesSoftwareType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    translation: fhirtypes.TerminologyCapabilitiesTranslationType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    validateCode: fhirtypes.TerminologyCapabilitiesValidateCodeType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TerminologyCapabilitiesClosure(backboneelement.BackboneElement):
    __resource_type__: str
    translation: bool | None
    translation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class TerminologyCapabilitiesCodeSystem(backboneelement.BackboneElement):
    __resource_type__: str
    subsumption: bool | None
    subsumption__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uri: fhirtypes.CanonicalType | None
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: list[fhirtypes.TerminologyCapabilitiesCodeSystemVersionType] | None
    @classmethod
    def elements_sequence(cls): ...

class TerminologyCapabilitiesCodeSystemVersion(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.StringType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    compositional: bool | None
    compositional__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    filter: list[fhirtypes.TerminologyCapabilitiesCodeSystemVersionFilterType] | None
    isDefault: bool | None
    isDefault__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    language: list[fhirtypes.CodeType | None] | None
    language__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    property: list[fhirtypes.CodeType | None] | None
    property__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...

class TerminologyCapabilitiesCodeSystemVersionFilter(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    op: list[fhirtypes.CodeType | None] | None
    op__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TerminologyCapabilitiesExpansion(backboneelement.BackboneElement):
    __resource_type__: str
    hierarchical: bool | None
    hierarchical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    incomplete: bool | None
    incomplete__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    paging: bool | None
    paging__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    parameter: list[fhirtypes.TerminologyCapabilitiesExpansionParameterType] | None
    textFilter: fhirtypes.MarkdownType | None
    textFilter__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class TerminologyCapabilitiesExpansionParameter(backboneelement.BackboneElement):
    __resource_type__: str
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.CodeType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TerminologyCapabilitiesImplementation(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UrlType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TerminologyCapabilitiesSoftware(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TerminologyCapabilitiesTranslation(backboneelement.BackboneElement):
    __resource_type__: str
    needsMap: bool | None
    needsMap__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TerminologyCapabilitiesValidateCode(backboneelement.BackboneElement):
    __resource_type__: str
    translations: bool | None
    translations__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
