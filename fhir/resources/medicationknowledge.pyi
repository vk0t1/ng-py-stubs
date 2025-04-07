from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MedicationKnowledge(domainresource.DomainResource):
    __resource_type__: str
    associatedMedication: list[fhirtypes.ReferenceType] | None
    author: fhirtypes.ReferenceType | None
    clinicalUseIssue: list[fhirtypes.ReferenceType] | None
    code: fhirtypes.CodeableConceptType | None
    cost: list[fhirtypes.MedicationKnowledgeCostType] | None
    definitional: fhirtypes.MedicationKnowledgeDefinitionalType | None
    identifier: list[fhirtypes.IdentifierType] | None
    indicationGuideline: list[fhirtypes.MedicationKnowledgeIndicationGuidelineType] | None
    intendedJurisdiction: list[fhirtypes.CodeableConceptType] | None
    medicineClassification: list[fhirtypes.MedicationKnowledgeMedicineClassificationType] | None
    monitoringProgram: list[fhirtypes.MedicationKnowledgeMonitoringProgramType] | None
    monograph: list[fhirtypes.MedicationKnowledgeMonographType] | None
    name: list[fhirtypes.StringType | None] | None
    name__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    packaging: list[fhirtypes.MedicationKnowledgePackagingType] | None
    preparationInstruction: fhirtypes.MarkdownType | None
    preparationInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    productType: list[fhirtypes.CodeableConceptType] | None
    regulatory: list[fhirtypes.MedicationKnowledgeRegulatoryType] | None
    relatedMedicationKnowledge: list[fhirtypes.MedicationKnowledgeRelatedMedicationKnowledgeType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    storageGuideline: list[fhirtypes.MedicationKnowledgeStorageGuidelineType] | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeCost(backboneelement.BackboneElement):
    __resource_type__: str
    costCodeableConcept: fhirtypes.CodeableConceptType | None
    costMoney: fhirtypes.MoneyType | None
    effectiveDate: list[fhirtypes.PeriodType] | None
    source: fhirtypes.StringType | None
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationKnowledgeDefinitional(backboneelement.BackboneElement):
    __resource_type__: str
    definition: list[fhirtypes.ReferenceType] | None
    doseForm: fhirtypes.CodeableConceptType | None
    drugCharacteristic: list[fhirtypes.MedicationKnowledgeDefinitionalDrugCharacteristicType] | None
    ingredient: list[fhirtypes.MedicationKnowledgeDefinitionalIngredientType] | None
    intendedRoute: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeDefinitionalDrugCharacteristic(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType | None
    valueAttachment: fhirtypes.AttachmentType | None
    valueBase64Binary: fhirtypes.Base64BinaryType | None
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationKnowledgeDefinitionalIngredient(backboneelement.BackboneElement):
    __resource_type__: str
    item: fhirtypes.CodeableReferenceType
    strengthCodeableConcept: fhirtypes.CodeableConceptType | None
    strengthQuantity: fhirtypes.QuantityType | None
    strengthRatio: fhirtypes.RatioType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationKnowledgeIndicationGuideline(backboneelement.BackboneElement):
    __resource_type__: str
    dosingGuideline: list[fhirtypes.MedicationKnowledgeIndicationGuidelineDosingGuidelineType] | None
    indication: list[fhirtypes.CodeableReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeIndicationGuidelineDosingGuideline(backboneelement.BackboneElement):
    __resource_type__: str
    administrationTreatment: fhirtypes.CodeableConceptType | None
    dosage: list[fhirtypes.MedicationKnowledgeIndicationGuidelineDosingGuidelineDosageType] | None
    patientCharacteristic: (
        list[fhirtypes.MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristicType] | None
    )
    treatmentIntent: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeIndicationGuidelineDosingGuidelineDosage(backboneelement.BackboneElement):
    __resource_type__: str
    dosage: list[fhirtypes.DosageType]
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeIndicationGuidelineDosingGuidelinePatientCharacteristic(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationKnowledgeMedicineClassification(backboneelement.BackboneElement):
    __resource_type__: str
    classification: list[fhirtypes.CodeableConceptType] | None
    sourceString: fhirtypes.StringType | None
    sourceString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sourceUri: fhirtypes.UriType | None
    sourceUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationKnowledgeMonitoringProgram(backboneelement.BackboneElement):
    __resource_type__: str
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeMonograph(backboneelement.BackboneElement):
    __resource_type__: str
    source: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgePackaging(backboneelement.BackboneElement):
    __resource_type__: str
    cost: list[fhirtypes.MedicationKnowledgeCostType] | None
    packagedProduct: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeRegulatory(backboneelement.BackboneElement):
    __resource_type__: str
    maxDispense: fhirtypes.MedicationKnowledgeRegulatoryMaxDispenseType | None
    regulatoryAuthority: fhirtypes.ReferenceType
    schedule: list[fhirtypes.CodeableConceptType] | None
    substitution: list[fhirtypes.MedicationKnowledgeRegulatorySubstitutionType] | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeRegulatoryMaxDispense(backboneelement.BackboneElement):
    __resource_type__: str
    period: fhirtypes.DurationType | None
    quantity: fhirtypes.QuantityType
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeRegulatorySubstitution(backboneelement.BackboneElement):
    __resource_type__: str
    allowed: bool | None
    allowed__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MedicationKnowledgeRelatedMedicationKnowledge(backboneelement.BackboneElement):
    __resource_type__: str
    reference: list[fhirtypes.ReferenceType]
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeStorageGuideline(backboneelement.BackboneElement):
    __resource_type__: str
    environmentalSetting: list[fhirtypes.MedicationKnowledgeStorageGuidelineEnvironmentalSettingType] | None
    note: list[fhirtypes.AnnotationType] | None
    reference: fhirtypes.UriType | None
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    stabilityDuration: fhirtypes.DurationType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeStorageGuidelineEnvironmentalSetting(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
