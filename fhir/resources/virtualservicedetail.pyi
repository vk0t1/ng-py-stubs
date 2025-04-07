from . import datatype as datatype
from . import fhirtypes as fhirtypes

class VirtualServiceDetail(datatype.DataType):
    __resource_type__: str
    additionalInfo: list[fhirtypes.UrlType | None] | None
    additionalInfo__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    addressContactPoint: fhirtypes.ContactPointType | None
    addressExtendedContactDetail: fhirtypes.ExtendedContactDetailType | None
    addressString: fhirtypes.StringType | None
    addressString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    addressUrl: fhirtypes.UrlType | None
    addressUrl__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    channelType: fhirtypes.CodingType | None
    maxParticipants: fhirtypes.PositiveIntType | None
    maxParticipants__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sessionKey: fhirtypes.StringType | None
    sessionKey__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
