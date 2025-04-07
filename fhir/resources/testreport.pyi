from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class TestReport(domainresource.DomainResource):
    __resource_type__: str
    identifier: fhirtypes.IdentifierType | None
    issued: fhirtypes.DateTimeType | None
    issued__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    participant: list[fhirtypes.TestReportParticipantType] | None
    result: fhirtypes.CodeType | None
    result__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    score: fhirtypes.DecimalType | None
    score__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    setup: fhirtypes.TestReportSetupType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    teardown: fhirtypes.TestReportTeardownType | None
    test: list[fhirtypes.TestReportTestType] | None
    testScript: fhirtypes.CanonicalType | None
    testScript__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    tester: fhirtypes.StringType | None
    tester__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestReportParticipant(backboneelement.BackboneElement):
    __resource_type__: str
    display: fhirtypes.StringType | None
    display__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    uri: fhirtypes.UriType | None
    uri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestReportSetup(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.TestReportSetupActionType]
    @classmethod
    def elements_sequence(cls): ...

class TestReportSetupAction(backboneelement.BackboneElement):
    __resource_type__: str
    assert_fhir: fhirtypes.TestReportSetupActionAssertType | None
    operation: fhirtypes.TestReportSetupActionOperationType | None
    @classmethod
    def elements_sequence(cls): ...

class TestReportSetupActionAssert(backboneelement.BackboneElement):
    __resource_type__: str
    detail: fhirtypes.StringType | None
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    message: fhirtypes.MarkdownType | None
    message__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    requirement: list[fhirtypes.TestReportSetupActionAssertRequirementType] | None
    result: fhirtypes.CodeType | None
    result__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestReportSetupActionAssertRequirement(backboneelement.BackboneElement):
    __resource_type__: str
    linkCanonical: fhirtypes.CanonicalType | None
    linkCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    linkUri: fhirtypes.UriType | None
    linkUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class TestReportSetupActionOperation(backboneelement.BackboneElement):
    __resource_type__: str
    detail: fhirtypes.UriType | None
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    message: fhirtypes.MarkdownType | None
    message__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    result: fhirtypes.CodeType | None
    result__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class TestReportTeardown(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.TestReportTeardownActionType]
    @classmethod
    def elements_sequence(cls): ...

class TestReportTeardownAction(backboneelement.BackboneElement):
    __resource_type__: str
    operation: fhirtypes.TestReportSetupActionOperationType
    @classmethod
    def elements_sequence(cls): ...

class TestReportTest(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.TestReportTestActionType]
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class TestReportTestAction(backboneelement.BackboneElement):
    __resource_type__: str
    assert_fhir: fhirtypes.TestReportSetupActionAssertType | None
    operation: fhirtypes.TestReportSetupActionOperationType | None
    @classmethod
    def elements_sequence(cls): ...
