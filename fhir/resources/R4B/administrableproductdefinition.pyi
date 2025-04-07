from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class AdministrableProductDefinition(domainresource.DomainResource):
    __resource_type__: str
    administrableDoseForm: fhirtypes.CodeableConceptType | None
    device: fhirtypes.ReferenceType | None
    formOf: list[fhirtypes.ReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    ingredient: list[fhirtypes.CodeableConceptType] | None
    producedFrom: list[fhirtypes.ReferenceType] | None
    property: list[fhirtypes.AdministrableProductDefinitionPropertyType] | None
    routeOfAdministration: list[fhirtypes.AdministrableProductDefinitionRouteOfAdministrationType]
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    unitOfPresentation: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class AdministrableProductDefinitionProperty(backboneelement.BackboneElement):
    __resource_type__: str
    status: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeableConceptType
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class AdministrableProductDefinitionRouteOfAdministration(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    firstDose: fhirtypes.QuantityType | None
    maxDosePerDay: fhirtypes.QuantityType | None
    maxDosePerTreatmentPeriod: fhirtypes.RatioType | None
    maxSingleDose: fhirtypes.QuantityType | None
    maxTreatmentPeriod: fhirtypes.DurationType | None
    targetSpecies: list[fhirtypes.AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesType] | None
    @classmethod
    def elements_sequence(cls): ...

class AdministrableProductDefinitionRouteOfAdministrationTargetSpecies(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    withdrawalPeriod: (
        list[fhirtypes.AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriodType] | None
    )
    @classmethod
    def elements_sequence(cls): ...

class AdministrableProductDefinitionRouteOfAdministrationTargetSpeciesWithdrawalPeriod(backboneelement.BackboneElement):
    __resource_type__: str
    supportingInformation: fhirtypes.StringType | None
    supportingInformation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    tissue: fhirtypes.CodeableConceptType
    value: fhirtypes.QuantityType
    @classmethod
    def elements_sequence(cls): ...
