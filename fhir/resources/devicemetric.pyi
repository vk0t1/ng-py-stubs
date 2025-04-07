from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DeviceMetric(domainresource.DomainResource):
    __resource_type__: str
    calibration: list[fhirtypes.DeviceMetricCalibrationType] | None
    category: fhirtypes.CodeType | None
    category__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    color: fhirtypes.CodeType | None
    color__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    device: fhirtypes.ReferenceType
    identifier: list[fhirtypes.IdentifierType] | None
    measurementFrequency: fhirtypes.QuantityType | None
    operationalStatus: fhirtypes.CodeType | None
    operationalStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    unit: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DeviceMetricCalibration(backboneelement.BackboneElement):
    __resource_type__: str
    state: fhirtypes.CodeType | None
    state__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    time: fhirtypes.InstantType | None
    time__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
