from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ResearchStudy(domainresource.DomainResource):
    __resource_type__: str
    arm: list[fhirtypes.ResearchStudyArmType] | None
    category: list[fhirtypes.CodeableConceptType] | None
    contact: list[fhirtypes.ContactDetailType] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    enrollment: list[fhirtypes.ReferenceType] | None
    focus: list[fhirtypes.CodeableConceptType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    keyword: list[fhirtypes.CodeableConceptType] | None
    note: list[fhirtypes.AnnotationType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    period: fhirtypes.PeriodType | None
    principalInvestigator: fhirtypes.ReferenceType | None
    protocol: list[fhirtypes.ReferenceType] | None
    reasonStopped: fhirtypes.CodeableConceptType | None
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    site: list[fhirtypes.ReferenceType] | None
    sponsor: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ResearchStudyArm(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    description: fhirtypes.StringType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
