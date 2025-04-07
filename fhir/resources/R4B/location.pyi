from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Location(domainresource.DomainResource):
    __resource_type__: str
    address: fhirtypes.AddressType | None
    alias: list[fhirtypes.StringType | None] | None
    alias__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    availabilityExceptions: fhirtypes.StringType | None
    availabilityExceptions__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    endpoint: list[fhirtypes.ReferenceType] | None
    hoursOfOperation: list[fhirtypes.LocationHoursOfOperationType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    managingOrganization: fhirtypes.ReferenceType | None
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    operationalStatus: fhirtypes.CodingType | None
    partOf: fhirtypes.ReferenceType | None
    physicalType: fhirtypes.CodeableConceptType | None
    position: fhirtypes.LocationPositionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    telecom: list[fhirtypes.ContactPointType] | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class LocationHoursOfOperation(backboneelement.BackboneElement):
    __resource_type__: str
    allDay: bool | None
    allDay__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    closingTime: fhirtypes.TimeType | None
    closingTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    daysOfWeek: list[fhirtypes.CodeType | None] | None
    daysOfWeek__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    openingTime: fhirtypes.TimeType | None
    openingTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class LocationPosition(backboneelement.BackboneElement):
    __resource_type__: str
    altitude: fhirtypes.DecimalType | None
    altitude__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    latitude: fhirtypes.DecimalType | None
    latitude__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    longitude: fhirtypes.DecimalType | None
    longitude__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
