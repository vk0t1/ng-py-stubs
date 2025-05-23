from . import backboneelement as backboneelement
from . import element as element
from . import fhirtypes as fhirtypes

class Dosage(backboneelement.BackboneElement):
    __resource_type__: str
    additionalInstruction: list[fhirtypes.CodeableConceptType] | None
    asNeededBoolean: bool | None
    asNeededBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    asNeededCodeableConcept: fhirtypes.CodeableConceptType | None
    doseAndRate: list[fhirtypes.DosageDoseAndRateType] | None
    maxDosePerAdministration: fhirtypes.QuantityType | None
    maxDosePerLifetime: fhirtypes.QuantityType | None
    maxDosePerPeriod: fhirtypes.RatioType | None
    method: fhirtypes.CodeableConceptType | None
    patientInstruction: fhirtypes.StringType | None
    patientInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    route: fhirtypes.CodeableConceptType | None
    sequence: fhirtypes.IntegerType | None
    sequence__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    site: fhirtypes.CodeableConceptType | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    timing: fhirtypes.TimingType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class DosageDoseAndRate(element.Element):
    __resource_type__: str
    doseQuantity: fhirtypes.QuantityType | None
    doseRange: fhirtypes.RangeType | None
    rateQuantity: fhirtypes.QuantityType | None
    rateRange: fhirtypes.RangeType | None
    rateRatio: fhirtypes.RatioType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
