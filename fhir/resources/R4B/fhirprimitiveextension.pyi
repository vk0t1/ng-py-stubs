import typing

from fhir_core import fhirabstractmodel

from . import fhirtypes as fhirtypes

class FHIRPrimitiveExtension(fhirabstractmodel.FHIRAbstractModel):
    __resource_type__: str
    id: fhirtypes.StringType | None
    extension: list[fhirtypes.ExtensionType] | None
    def validate_extension_or_fhir_comment_required(cls, values: dict[str, typing.Any]) -> dict[str, typing.Any]: ...
    @classmethod
    def elements_sequence(cls): ...
