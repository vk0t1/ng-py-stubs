from . import element as element
from . import fhirtypes as fhirtypes

class Dosage(element.Element):
    __resource_type__: str
    additionalInstruction: list[fhirtypes.CodeableConceptType] | None
    asNeededBoolean: bool | None
    asNeededBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    asNeededCodeableConcept: fhirtypes.CodeableConceptType | None
    doseQuantity: fhirtypes.QuantityType | None
    doseRange: fhirtypes.RangeType | None
    maxDosePerAdministration: fhirtypes.QuantityType | None
    maxDosePerLifetime: fhirtypes.QuantityType | None
    maxDosePerPeriod: fhirtypes.RatioType | None
    method: fhirtypes.CodeableConceptType | None
    patientInstruction: fhirtypes.StringType | None
    patientInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rateQuantity: fhirtypes.QuantityType | None
    rateRange: fhirtypes.RangeType | None
    rateRatio: fhirtypes.RatioType | None
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
