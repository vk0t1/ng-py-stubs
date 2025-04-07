from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ExampleScenario(domainresource.DomainResource):
    __resource_type__: str
    actor: list[fhirtypes.ExampleScenarioActorType] | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    workflow: list[fhirtypes.CanonicalType | None] | None
    workflow__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExampleScenarioActor(backboneelement.BackboneElement):
    __resource_type__: str
    actorId: fhirtypes.StringType | None
    actorId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExampleScenarioInstance(backboneelement.BackboneElement):
    __resource_type__: str
    containedInstance: list[fhirtypes.ExampleScenarioInstanceContainedInstanceType] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resourceId: fhirtypes.StringType | None
    resourceId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    resourceType: fhirtypes.CodeType | None
    resourceType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: list[fhirtypes.ExampleScenarioInstanceVersionType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExampleScenarioInstanceContainedInstance(backboneelement.BackboneElement):
    __resource_type__: str
    resourceId: fhirtypes.StringType | None
    resourceId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    versionId: fhirtypes.StringType | None
    versionId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ExampleScenarioInstanceVersion(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    versionId: fhirtypes.StringType | None
    versionId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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
    operation: fhirtypes.ExampleScenarioProcessStepOperationType | None
    pause: bool | None
    pause__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    process: list[fhirtypes.ExampleScenarioProcessType] | None
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
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    number: fhirtypes.StringType | None
    number__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    receiver: fhirtypes.StringType | None
    receiver__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    receiverActive: bool | None
    receiverActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    request: fhirtypes.ExampleScenarioInstanceContainedInstanceType | None
    response: fhirtypes.ExampleScenarioInstanceContainedInstanceType | None
    type: fhirtypes.StringType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
