from . import fhirtypes as fhirtypes
from . import resource as resource

class DomainResource(resource.Resource):
    __resource_type__: str
    contained: list[fhirtypes.ResourceType] | None
    extension: list[fhirtypes.ExtensionType] | None
    modifierExtension: list[fhirtypes.ExtensionType] | None
    text: fhirtypes.NarrativeType | None
    @classmethod
    def elements_sequence(cls): ...
