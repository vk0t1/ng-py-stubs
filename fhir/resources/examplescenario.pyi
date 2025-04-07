from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ExampleScenario(domainresource.DomainResource):
    __resource_type__: str
    actor: list[fhirtypes.ExampleScenarioActorType] | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyrightLabel: fhirtypes.StringType | None
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    instance: list[fhirtypes.ExampleScenarioInstanceType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    process: list[fhirtypes.ExampleScenarioProcessType] | None
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

class ExampleScenarioActor(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    key: fhirtypes.StringType | None
    key__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExampleScenarioInstance(backboneelement.BackboneElement):
    __resource_type__: str
    containedInstance: list[fhirtypes.ExampleScenarioInstanceContainedInstanceType] | None
    content: fhirtypes.ReferenceType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    key: fhirtypes.StringType | None
    key__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    structureProfileCanonical: fhirtypes.CanonicalType | None
    structureProfileCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    structureProfileUri: fhirtypes.UriType | None
    structureProfileUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    structureType: fhirtypes.CodingType
    structureVersion: fhirtypes.StringType | None
    structureVersion__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: list[fhirtypes.ExampleScenarioInstanceVersionType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ExampleScenarioInstanceContainedInstance(backboneelement.BackboneElement):
    __resource_type__: str
    instanceReference: fhirtypes.StringType | None
    instanceReference__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    versionReference: fhirtypes.StringType | None
    versionReference__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExampleScenarioInstanceVersion(backboneelement.BackboneElement):
    __resource_type__: str
    content: fhirtypes.ReferenceType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    key: fhirtypes.StringType | None
    key__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExampleScenarioProcess(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    postConditions: fhirtypes.MarkdownType | None
    postConditions__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    preConditions: fhirtypes.MarkdownType | None
    preConditions__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    step: list[fhirtypes.ExampleScenarioProcessStepType] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExampleScenarioProcessStep(backboneelement.BackboneElement):
    __resource_type__: str
    alternative: list[fhirtypes.ExampleScenarioProcessStepAlternativeType] | None
    number: fhirtypes.StringType | None
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    operation: fhirtypes.ExampleScenarioProcessStepOperationType | None
    pause: bool | None
    pause__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    process: fhirtypes.ExampleScenarioProcessType | None
    workflow: fhirtypes.CanonicalType | None
    workflow__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ExampleScenarioProcessStepAlternative(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    step: list[fhirtypes.ExampleScenarioProcessStepType] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExampleScenarioProcessStepOperation(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    initiator: fhirtypes.StringType | None
    initiator__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    initiatorActive: bool | None
    initiatorActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    receiver: fhirtypes.StringType | None
    receiver__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    receiverActive: bool | None
    receiverActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    request: fhirtypes.ExampleScenarioInstanceContainedInstanceType | None
    response: fhirtypes.ExampleScenarioInstanceContainedInstanceType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodingType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
