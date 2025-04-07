from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ExpansionProfile(domainresource.DomainResource):
    __resource_type__: str
    activeOnly: bool | None
    activeOnly__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contact: list[fhirtypes.ContactDetailType] | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    designation: fhirtypes.ExpansionProfileDesignationType | None
    displayLanguage: fhirtypes.CodeType | None
    displayLanguage__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    excludeNested: bool | None
    excludeNested__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    excludeNotForUI: bool | None
    excludeNotForUI__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    excludePostCoordinated: bool | None
    excludePostCoordinated__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    excludedSystem: fhirtypes.ExpansionProfileExcludedSystemType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixedVersion: list[fhirtypes.ExpansionProfileFixedVersionType] | None
    identifier: fhirtypes.IdentifierType | None
    includeDefinition: bool | None
    includeDefinition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    includeDesignations: bool | None
    includeDesignations__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    limitedExpansion: bool | None
    limitedExpansion__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExpansionProfileDesignation(backboneelement.BackboneElement):
    __resource_type__: str
    exclude: fhirtypes.ExpansionProfileDesignationExcludeType | None
    include: fhirtypes.ExpansionProfileDesignationIncludeType | None
    @classmethod
    def elements_sequence(cls): ...

class ExpansionProfileDesignationExclude(backboneelement.BackboneElement):
    __resource_type__: str
    designation: list[fhirtypes.ExpansionProfileDesignationExcludeDesignationType] | None
    @classmethod
    def elements_sequence(cls): ...

class ExpansionProfileDesignationExcludeDesignation(backboneelement.BackboneElement):
    __resource_type__: str
    language: fhirtypes.CodeType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    use: fhirtypes.CodingType | None
    @classmethod
    def elements_sequence(cls): ...

class ExpansionProfileDesignationInclude(backboneelement.BackboneElement):
    __resource_type__: str
    designation: list[fhirtypes.ExpansionProfileDesignationIncludeDesignationType] | None
    @classmethod
    def elements_sequence(cls): ...

class ExpansionProfileDesignationIncludeDesignation(backboneelement.BackboneElement):
    __resource_type__: str
    language: fhirtypes.CodeType | None
    language__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    use: fhirtypes.CodingType | None
    @classmethod
    def elements_sequence(cls): ...

class ExpansionProfileExcludedSystem(backboneelement.BackboneElement):
    __resource_type__: str
    system: fhirtypes.UriType | None
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExpansionProfileFixedVersion(backboneelement.BackboneElement):
    __resource_type__: str
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    system: fhirtypes.UriType | None
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
