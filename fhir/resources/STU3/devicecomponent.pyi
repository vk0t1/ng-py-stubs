from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DeviceComponent(domainresource.DomainResource):
    __resource_type__: str
    identifier: fhirtypes.IdentifierType
    languageCode: fhirtypes.CodeableConceptType | None
    lastSystemChange: fhirtypes.InstantType | None
    lastSystemChange__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    measurementPrinciple: fhirtypes.CodeType | None
    measurementPrinciple__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    operationalStatus: list[fhirtypes.CodeableConceptType] | None
    parameterGroup: fhirtypes.CodeableConceptType | None
    parent: fhirtypes.ReferenceType | None
    productionSpecification: list[fhirtypes.DeviceComponentProductionSpecificationType] | None
    source: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class DeviceComponentProductionSpecification(backboneelement.BackboneElement):
    __resource_type__: str
    componentId: fhirtypes.IdentifierType | None
    productionSpec: fhirtypes.StringType | None
    productionSpec__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    specType: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
