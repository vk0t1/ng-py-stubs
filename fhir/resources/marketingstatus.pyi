from . import backbonetype as backbonetype
from . import fhirtypes as fhirtypes

class MarketingStatus(backbonetype.BackboneType):
    __resource_type__: str
    country: fhirtypes.CodeableConceptType | None
    dateRange: fhirtypes.PeriodType | None
    jurisdiction: fhirtypes.CodeableConceptType | None
    restoreDate: fhirtypes.DateTimeType | None
    restoreDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
