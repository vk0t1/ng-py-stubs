from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MedicationKnowledge(domainresource.DomainResource):
    __resource_type__: str
    administrationGuidelines: list[fhirtypes.MedicationKnowledgeAdministrationGuidelinesType] | None
    amount: fhirtypes.QuantityType | None
    associatedMedication: list[fhirtypes.ReferenceType] | None
    code: fhirtypes.CodeableConceptType | None
    contraindication: list[fhirtypes.ReferenceType] | None
    cost: list[fhirtypes.MedicationKnowledgeCostType] | None
    doseForm: fhirtypes.CodeableConceptType | None
    drugCharacteristic: list[fhirtypes.MedicationKnowledgeDrugCharacteristicType] | None
    ingredient: list[fhirtypes.MedicationKnowledgeIngredientType] | None
    intendedRoute: list[fhirtypes.CodeableConceptType] | None
    kinetics: list[fhirtypes.MedicationKnowledgeKineticsType] | None
    manufacturer: fhirtypes.ReferenceType | None
    medicineClassification: list[fhirtypes.MedicationKnowledgeMedicineClassificationType] | None
    monitoringProgram: list[fhirtypes.MedicationKnowledgeMonitoringProgramType] | None
    monograph: list[fhirtypes.MedicationKnowledgeMonographType] | None
    packaging: fhirtypes.MedicationKnowledgePackagingType | None
    preparationInstruction: fhirtypes.MarkdownType | None
    preparationInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    productType: list[fhirtypes.CodeableConceptType] | None
    regulatory: list[fhirtypes.MedicationKnowledgeRegulatoryType] | None
    relatedMedicationKnowledge: list[fhirtypes.MedicationKnowledgeRelatedMedicationKnowledgeType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    synonym: list[fhirtypes.StringType | None] | None
    synonym__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeAdministrationGuidelines(backboneelement.BackboneElement):
    __resource_type__: str
    dosage: list[fhirtypes.MedicationKnowledgeAdministrationGuidelinesDosageType] | None
    indicationCodeableConcept: fhirtypes.CodeableConceptType | None
    indicationReference: fhirtypes.ReferenceType | None
    patientCharacteristics: list[fhirtypes.MedicationKnowledgeAdministrationGuidelinesPatientCharacteristicsType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationKnowledgeAdministrationGuidelinesDosage(backboneelement.BackboneElement):
    __resource_type__: str
    dosage: list[fhirtypes.DosageType]
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics(backboneelement.BackboneElement):
    __resource_type__: str
    characteristicCodeableConcept: fhirtypes.CodeableConceptType | None
    characteristicQuantity: fhirtypes.QuantityType | None
    value: list[fhirtypes.StringType | None] | None
    value__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationKnowledgeCost(backboneelement.BackboneElement):
    __resource_type__: str
    cost: fhirtypes.MoneyType
    source: fhirtypes.StringType | None
    source__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeDrugCharacteristic(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType | None
    valueBase64Binary: fhirtypes.Base64BinaryType | None
    valueBase64Binary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationKnowledgeIngredient(backboneelement.BackboneElement):
    __resource_type__: str
    isActive: bool | None
    isActive__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    itemCodeableConcept: fhirtypes.CodeableConceptType | None
    itemReference: fhirtypes.ReferenceType | None
    strength: fhirtypes.RatioType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class MedicationKnowledgeKinetics(backboneelement.BackboneElement):
    __resource_type__: str
    areaUnderCurve: list[fhirtypes.QuantityType] | None
    halfLifePeriod: fhirtypes.DurationType | None
    lethalDose50: list[fhirtypes.QuantityType] | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeMedicineClassification(backboneelement.BackboneElement):
    __resource_type__: str
    classification: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

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
    quantity: fhirtypes.QuantityType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeRegulatory(backboneelement.BackboneElement):
    __resource_type__: str
    maxDispense: fhirtypes.MedicationKnowledgeRegulatoryMaxDispenseType | None
    regulatoryAuthority: fhirtypes.ReferenceType
    schedule: list[fhirtypes.MedicationKnowledgeRegulatoryScheduleType] | None
    substitution: list[fhirtypes.MedicationKnowledgeRegulatorySubstitutionType] | None
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeRegulatoryMaxDispense(backboneelement.BackboneElement):
    __resource_type__: str
    period: fhirtypes.DurationType | None
    quantity: fhirtypes.QuantityType
    @classmethod
    def elements_sequence(cls): ...

class MedicationKnowledgeRegulatorySchedule(backboneelement.BackboneElement):
    __resource_type__: str
    schedule: fhirtypes.CodeableConceptType
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
