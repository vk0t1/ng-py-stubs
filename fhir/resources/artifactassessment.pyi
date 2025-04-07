from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ArtifactAssessment(domainresource.DomainResource):
    __resource_type__: str
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    artifactCanonical: fhirtypes.CanonicalType | None
    artifactCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    artifactReference: fhirtypes.ReferenceType | None
    artifactUri: fhirtypes.UriType | None
    artifactUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    citeAsMarkdown: fhirtypes.MarkdownType | None
    citeAsMarkdown__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    citeAsReference: fhirtypes.ReferenceType | None
    content: list[fhirtypes.ArtifactAssessmentContentType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    disposition: fhirtypes.CodeType | None
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    workflowStatus: fhirtypes.CodeType | None
    workflowStatus__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ArtifactAssessmentContent(backboneelement.BackboneElement):
    __resource_type__: str
    author: fhirtypes.ReferenceType | None
    classifier: list[fhirtypes.CodeableConceptType] | None
    component: list[fhirtypes.ArtifactAssessmentContentType] | None
    freeToShare: bool | None
    freeToShare__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    informationType: fhirtypes.CodeType | None
    informationType__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    path: list[fhirtypes.UriType | None] | None
    path__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    quantity: fhirtypes.QuantityType | None
    relatedArtifact: list[fhirtypes.RelatedArtifactType] | None
    summary: fhirtypes.MarkdownType | None
    summary__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
