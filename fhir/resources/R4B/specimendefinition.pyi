from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class SpecimenDefinition(domainresource.DomainResource):
    __resource_type__: str
    collection: list[fhirtypes.CodeableConceptType] | None
    identifier: fhirtypes.IdentifierType | None
    patientPreparation: list[fhirtypes.CodeableConceptType] | None
    timeAspect: fhirtypes.StringType | None
    timeAspect__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    typeCollected: fhirtypes.CodeableConceptType | None
    typeTested: list[fhirtypes.SpecimenDefinitionTypeTestedType] | None
    @classmethod
    def elements_sequence(cls): ...

class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    __resource_type__: str
    container: fhirtypes.SpecimenDefinitionTypeTestedContainerType | None
    handling: list[fhirtypes.SpecimenDefinitionTypeTestedHandlingType] | None
    isDerived: bool | None
    isDerived__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    preference: fhirtypes.CodeType | None
    preference__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    rejectionCriterion: list[fhirtypes.CodeableConceptType] | None
    requirement: fhirtypes.StringType | None
    requirement__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    retentionTime: fhirtypes.DurationType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    __resource_type__: str
    additive: list[fhirtypes.SpecimenDefinitionTypeTestedContainerAdditiveType] | None
    cap: fhirtypes.CodeableConceptType | None
    capacity: fhirtypes.QuantityType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    material: fhirtypes.CodeableConceptType | None
    minimumVolumeQuantity: fhirtypes.QuantityType | None
    minimumVolumeString: fhirtypes.StringType | None
    minimumVolumeString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    preparation: fhirtypes.StringType | None
    preparation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    __resource_type__: str
    additiveCodeableConcept: fhirtypes.CodeableConceptType | None
    additiveReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    __resource_type__: str
    instruction: fhirtypes.StringType | None
    instruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxDuration: fhirtypes.DurationType | None
    temperatureQualifier: fhirtypes.CodeableConceptType | None
    temperatureRange: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...
