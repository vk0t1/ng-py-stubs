from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ClinicalUseDefinition(domainresource.DomainResource):
    __resource_type__: str
    category: list[fhirtypes.CodeableConceptType] | None
    contraindication: fhirtypes.ClinicalUseDefinitionContraindicationType | None
    identifier: list[fhirtypes.IdentifierType] | None
    indication: fhirtypes.ClinicalUseDefinitionIndicationType | None
    interaction: fhirtypes.ClinicalUseDefinitionInteractionType | None
    library: list[fhirtypes.CanonicalType | None] | None
    library__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    population: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeableConceptType | None
    subject: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    undesirableEffect: fhirtypes.ClinicalUseDefinitionUndesirableEffectType | None
    warning: fhirtypes.ClinicalUseDefinitionWarningType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ClinicalUseDefinitionContraindication(backboneelement.BackboneElement):
    __resource_type__: str
    applicability: fhirtypes.ExpressionType | None
    comorbidity: list[fhirtypes.CodeableReferenceType] | None
    diseaseStatus: fhirtypes.CodeableReferenceType | None
    diseaseSymptomProcedure: fhirtypes.CodeableReferenceType | None
    indication: list[fhirtypes.ReferenceType] | None
    otherTherapy: list[fhirtypes.ClinicalUseDefinitionContraindicationOtherTherapyType] | None
    @classmethod
    def elements_sequence(cls): ...

class ClinicalUseDefinitionContraindicationOtherTherapy(backboneelement.BackboneElement):
    __resource_type__: str
    relationshipType: fhirtypes.CodeableConceptType
    treatment: fhirtypes.CodeableReferenceType
    @classmethod
    def elements_sequence(cls): ...

class ClinicalUseDefinitionIndication(backboneelement.BackboneElement):
    __resource_type__: str
    applicability: fhirtypes.ExpressionType | None
    comorbidity: list[fhirtypes.CodeableReferenceType] | None
    diseaseStatus: fhirtypes.CodeableReferenceType | None
    diseaseSymptomProcedure: fhirtypes.CodeableReferenceType | None
    durationRange: fhirtypes.RangeType | None
    durationString: fhirtypes.StringType | None
    durationString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    intendedEffect: fhirtypes.CodeableReferenceType | None
    otherTherapy: list[fhirtypes.ClinicalUseDefinitionContraindicationOtherTherapyType] | None
    undesirableEffect: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ClinicalUseDefinitionInteraction(backboneelement.BackboneElement):
    __resource_type__: str
    effect: fhirtypes.CodeableReferenceType | None
    incidence: fhirtypes.CodeableConceptType | None
    interactant: list[fhirtypes.ClinicalUseDefinitionInteractionInteractantType] | None
    management: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ClinicalUseDefinitionInteractionInteractant(backboneelement.BackboneElement):
    __resource_type__: str
    itemCodeableConcept: fhirtypes.CodeableConceptType | None
    itemReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ClinicalUseDefinitionUndesirableEffect(backboneelement.BackboneElement):
    __resource_type__: str
    classification: fhirtypes.CodeableConceptType | None
    frequencyOfOccurrence: fhirtypes.CodeableConceptType | None
    symptomConditionEffect: fhirtypes.CodeableReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class ClinicalUseDefinitionWarning(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
