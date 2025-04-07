from . import backboneelement as backboneelement
from . import fhirtypes as fhirtypes

class ProdCharacteristic(backboneelement.BackboneElement):
    __resource_type__: str
    color: list[fhirtypes.StringType | None] | None
    color__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    depth: fhirtypes.QuantityType | None
    externalDiameter: fhirtypes.QuantityType | None
    height: fhirtypes.QuantityType | None
    image: list[fhirtypes.AttachmentType] | None
    imprint: list[fhirtypes.StringType | None] | None
    imprint__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    nominalVolume: fhirtypes.QuantityType | None
    scoring: fhirtypes.CodeableConceptType | None
    shape: fhirtypes.StringType | None
    shape__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    weight: fhirtypes.QuantityType | None
    width: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
