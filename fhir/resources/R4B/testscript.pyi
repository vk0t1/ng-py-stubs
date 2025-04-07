from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class TestScript(domainresource.DomainResource):
    __resource_type__: str
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    destination: list[fhirtypes.TestScriptDestinationType] | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fixture: list[fhirtypes.TestScriptFixtureType] | None
    identifier: fhirtypes.IdentifierType | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    metadata: fhirtypes.TestScriptMetadataType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    origin: list[fhirtypes.TestScriptOriginType] | None
    profile: list[fhirtypes.ReferenceType] | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    setup: fhirtypes.TestScriptSetupType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    teardown: fhirtypes.TestScriptTeardownType | None
    test: list[fhirtypes.TestScriptTestType] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    variable: list[fhirtypes.TestScriptVariableType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestScriptDestination(backboneelement.BackboneElement):
    __resource_type__: str
    index: fhirtypes.IntegerType | None
    index__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    profile: fhirtypes.CodingType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestScriptFixture(backboneelement.BackboneElement):
    __resource_type__: str
    autocreate: bool | None
    autocreate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    autodelete: bool | None
    autodelete__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resource: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestScriptMetadata(backboneelement.BackboneElement):
    __resource_type__: str
    capability: list[fhirtypes.TestScriptMetadataCapabilityType]
    link: list[fhirtypes.TestScriptMetadataLinkType] | None
    @classmethod
    def elements_sequence(cls): ...

class TestScriptMetadataCapability(backboneelement.BackboneElement):
    __resource_type__: str
    capabilities: fhirtypes.CanonicalType | None
    capabilities__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    destination: fhirtypes.IntegerType | None
    destination__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    link: list[fhirtypes.UriType | None] | None
    link__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    origin: list[fhirtypes.IntegerType | None] | None
    origin__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    required: bool | None
    required__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    validated: bool | None
    validated__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestScriptMetadataLink(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestScriptOrigin(backboneelement.BackboneElement):
    __resource_type__: str
    index: fhirtypes.IntegerType | None
    index__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    profile: fhirtypes.CodingType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestScriptSetup(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.TestScriptSetupActionType]
    @classmethod
    def elements_sequence(cls): ...

class TestScriptSetupAction(backboneelement.BackboneElement):
    __resource_type__: str
    assert_fhir: fhirtypes.TestScriptSetupActionAssertType | None
    operation: fhirtypes.TestScriptSetupActionOperationType | None
    @classmethod
    def elements_sequence(cls): ...

class TestScriptSetupActionAssert(backboneelement.BackboneElement):
    __resource_type__: str
    compareToSourceExpression: fhirtypes.StringType | None
    compareToSourceExpression__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    compareToSourceId: fhirtypes.StringType | None
    compareToSourceId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    compareToSourcePath: fhirtypes.StringType | None
    compareToSourcePath__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contentType: fhirtypes.CodeType | None
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    direction: fhirtypes.CodeType | None
    direction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    expression: fhirtypes.StringType | None
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    headerField: fhirtypes.StringType | None
    headerField__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    label: fhirtypes.StringType | None
    label__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    minimumId: fhirtypes.StringType | None
    minimumId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    navigationLinks: bool | None
    navigationLinks__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    operator: fhirtypes.CodeType | None
    operator__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    requestMethod: fhirtypes.CodeType | None
    requestMethod__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    requestURL: fhirtypes.StringType | None
    requestURL__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resource: fhirtypes.CodeType | None
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    response: fhirtypes.CodeType | None
    response__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    responseCode: fhirtypes.StringType | None
    responseCode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sourceId: fhirtypes.IdType | None
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    validateProfileId: fhirtypes.IdType | None
    validateProfileId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    warningOnly: bool | None
    warningOnly__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestScriptSetupActionOperation(backboneelement.BackboneElement):
    __resource_type__: str
    accept: fhirtypes.CodeType | None
    accept__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contentType: fhirtypes.CodeType | None
    contentType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    destination: fhirtypes.IntegerType | None
    destination__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encodeRequestUrl: bool | None
    encodeRequestUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    label: fhirtypes.StringType | None
    label__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    method: fhirtypes.CodeType | None
    method__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    origin: fhirtypes.IntegerType | None
    origin__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    params: fhirtypes.StringType | None
    params__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    requestHeader: list[fhirtypes.TestScriptSetupActionOperationRequestHeaderType] | None
    requestId: fhirtypes.IdType | None
    requestId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resource: fhirtypes.CodeType | None
    resource__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    responseId: fhirtypes.IdType | None
    responseId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sourceId: fhirtypes.IdType | None
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetId: fhirtypes.IdType | None
    targetId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodingType | None
    url: fhirtypes.StringType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestScriptSetupActionOperationRequestHeader(backboneelement.BackboneElement):
    __resource_type__: str
    field: fhirtypes.StringType | None
    field__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestScriptTeardown(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.TestScriptTeardownActionType]
    @classmethod
    def elements_sequence(cls): ...

class TestScriptTeardownAction(backboneelement.BackboneElement):
    __resource_type__: str
    operation: fhirtypes.TestScriptSetupActionOperationType
    @classmethod
    def elements_sequence(cls): ...

class TestScriptTest(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.TestScriptTestActionType]
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class TestScriptTestAction(backboneelement.BackboneElement):
    __resource_type__: str
    assert_fhir: fhirtypes.TestScriptSetupActionAssertType | None
    operation: fhirtypes.TestScriptSetupActionOperationType | None
    @classmethod
    def elements_sequence(cls): ...

class TestScriptVariable(backboneelement.BackboneElement):
    __resource_type__: str
    defaultValue: fhirtypes.StringType | None
    defaultValue__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    expression: fhirtypes.StringType | None
    expression__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    headerField: fhirtypes.StringType | None
    headerField__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    hint: fhirtypes.StringType | None
    hint__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    path: fhirtypes.StringType | None
    path__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sourceId: fhirtypes.IdType | None
    sourceId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
