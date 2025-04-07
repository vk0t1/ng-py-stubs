from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class OperationDefinition(domainresource.DomainResource):
    __resource_type__: str
    affectsState: bool | None
    affectsState__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    base: fhirtypes.CanonicalType | None
    base__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    comment: fhirtypes.MarkdownType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contact: list[fhirtypes.ContactDetailType] | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    inputProfile: fhirtypes.CanonicalType | None
    inputProfile__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    instance: bool | None
    instance__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    kind: fhirtypes.CodeType | None
    kind__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    outputProfile: fhirtypes.CanonicalType | None
    outputProfile__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    overload: list[fhirtypes.OperationDefinitionOverloadType] | None
    parameter: list[fhirtypes.OperationDefinitionParameterType] | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resource: list[fhirtypes.CodeType | None] | None
    resource__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    system: bool | None
    system__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: bool | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class OperationDefinitionOverload(backboneelement.BackboneElement):
    __resource_type__: str
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    parameterName: list[fhirtypes.StringType | None] | None
    parameterName__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...

class OperationDefinitionParameter(backboneelement.BackboneElement):
    __resource_type__: str
    binding: fhirtypes.OperationDefinitionParameterBindingType | None
    documentation: fhirtypes.StringType | None
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    max: fhirtypes.StringType | None
    max__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    min: fhirtypes.IntegerType | None
    min__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.CodeType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    part: list[fhirtypes.OperationDefinitionParameterType] | None
    referencedFrom: list[fhirtypes.OperationDefinitionParameterReferencedFromType] | None
    searchType: fhirtypes.CodeType | None
    searchType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetProfile: list[fhirtypes.CanonicalType | None] | None
    targetProfile__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    use: fhirtypes.CodeType | None
    use__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    __resource_type__: str
    strength: fhirtypes.CodeType | None
    strength__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueSet: fhirtypes.CanonicalType | None
    valueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class OperationDefinitionParameterReferencedFrom(backboneelement.BackboneElement):
    __resource_type__: str
    source: fhirtypes.StringType | None
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sourceId: fhirtypes.StringType | None
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
