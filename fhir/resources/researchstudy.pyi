from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ResearchStudy(domainresource.DomainResource):
    __resource_type__: str
    associatedParty: list[fhirtypes.ResearchStudyAssociatedPartyType] | None
    classifier: list[fhirtypes.CodeableConceptType] | None
    comparisonGroup: list[fhirtypes.ResearchStudyComparisonGroupType] | None
    condition: list[fhirtypes.CodeableConceptType] | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    descriptionSummary: fhirtypes.MarkdownType | None
    descriptionSummary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    focus: list[fhirtypes.CodeableReferenceType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    keyword: list[fhirtypes.CodeableConceptType] | None
    label: list[fhirtypes.ResearchStudyLabelType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    objective: list[fhirtypes.ResearchStudyObjectiveType] | None
    outcomeMeasure: list[fhirtypes.ResearchStudyOutcomeMeasureType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    period: fhirtypes.PeriodType | None
    phase: fhirtypes.CodeableConceptType | None
    primaryPurposeType: fhirtypes.CodeableConceptType | None
    progressStatus: list[fhirtypes.ResearchStudyProgressStatusType] | None
    protocol: list[fhirtypes.ReferenceType] | None
    recruitment: fhirtypes.ResearchStudyRecruitmentType | None
    region: list[fhirtypes.CodeableConceptType] | None
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    result: list[fhirtypes.ReferenceType] | None
    site: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    studyDesign: list[fhirtypes.CodeableConceptType] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    whyStopped: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ResearchStudyAssociatedParty(backboneelement.BackboneElement):
    __resource_type__: str
    classifier: list[fhirtypes.CodeableConceptType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    party: fhirtypes.ReferenceType | None
    period: list[fhirtypes.PeriodType] | None
    role: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class ResearchStudyComparisonGroup(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    intendedExposure: list[fhirtypes.ReferenceType] | None
    linkId: fhirtypes.IdType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    observedGroup: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ResearchStudyLabel(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ResearchStudyObjective(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class ResearchStudyOutcomeMeasure(backboneelement.BackboneElement):
    __resource_type__: str
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reference: fhirtypes.ReferenceType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class ResearchStudyProgressStatus(backboneelement.BackboneElement):
    __resource_type__: str
    actual: bool | None
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    period: fhirtypes.PeriodType | None
    state: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class ResearchStudyRecruitment(backboneelement.BackboneElement):
    __resource_type__: str
    actualGroup: fhirtypes.ReferenceType | None
    actualNumber: fhirtypes.UnsignedIntType | None
    actualNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    eligibility: fhirtypes.ReferenceType | None
    targetNumber: fhirtypes.UnsignedIntType | None
    targetNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
