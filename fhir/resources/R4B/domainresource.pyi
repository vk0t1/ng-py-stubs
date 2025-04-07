from . import fhirtypes as fhirtypes
from . import resource as resource

class DomainResource(resource.Resource):
    __resource_type__: str = "DomainResource"
    contained: list[fhirtypes.ResourceType] | None = None
    extension: list[fhirtypes.ExtensionType] | None = None
    modifierExtension: list[fhirtypes.ExtensionType] | None = None
    text: fhirtypes.NarrativeType | None = None
    @classmethod
    def elements_sequence(cls) -> list[str]: ...
