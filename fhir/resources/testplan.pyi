from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class TestPlan(domainresource.DomainResource):
    __resource_type__: str
    category: list[fhirtypes.CodeableConceptType] | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyrightLabel: fhirtypes.StringType | None
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dependency: list[fhirtypes.TestPlanDependencyType] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    exitCriteria: fhirtypes.MarkdownType | None
    exitCriteria__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    scope: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    testCase: list[fhirtypes.TestPlanTestCaseType] | None
    testTools: fhirtypes.MarkdownType | None
    testTools__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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

class TestPlanDependency(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    predecessor: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class TestPlanTestCase(backboneelement.BackboneElement):
    __resource_type__: str
    assertion: list[fhirtypes.TestPlanTestCaseAssertionType] | None
    dependency: list[fhirtypes.TestPlanTestCaseDependencyType] | None
    scope: list[fhirtypes.ReferenceType] | None
    sequence: fhirtypes.IntegerType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    testData: list[fhirtypes.TestPlanTestCaseTestDataType] | None
    testRun: list[fhirtypes.TestPlanTestCaseTestRunType] | None
    @classmethod
    def elements_sequence(cls): ...

class TestPlanTestCaseAssertion(backboneelement.BackboneElement):
    __resource_type__: str
    object: list[fhirtypes.CodeableReferenceType] | None
    result: list[fhirtypes.CodeableReferenceType] | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class TestPlanTestCaseDependency(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    predecessor: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class TestPlanTestCaseTestData(backboneelement.BackboneElement):
    __resource_type__: str
    content: fhirtypes.ReferenceType | None
    sourceReference: fhirtypes.ReferenceType | None
    sourceString: fhirtypes.StringType | None
    sourceString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodingType
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class TestPlanTestCaseTestRun(backboneelement.BackboneElement):
    __resource_type__: str
    narrative: fhirtypes.MarkdownType | None
    narrative__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    script: fhirtypes.TestPlanTestCaseTestRunScriptType | None
    @classmethod
    def elements_sequence(cls): ...

class TestPlanTestCaseTestRunScript(backboneelement.BackboneElement):
    __resource_type__: str
    language: fhirtypes.CodeableConceptType | None
    sourceReference: fhirtypes.ReferenceType | None
    sourceString: fhirtypes.StringType | None
    sourceString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
