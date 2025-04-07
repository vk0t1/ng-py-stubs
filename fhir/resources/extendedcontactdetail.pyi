from . import datatype as datatype
from . import fhirtypes as fhirtypes

class ExtendedContactDetail(datatype.DataType):
    __resource_type__: str
    address: fhirtypes.AddressType | None
    name: list[fhirtypes.HumanNameType] | None
    organization: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    purpose: fhirtypes.CodeableConceptType | None
    telecom: list[fhirtypes.ContactPointType] | None
    @classmethod
    def elements_sequence(cls): ...
