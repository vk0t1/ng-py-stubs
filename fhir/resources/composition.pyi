from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Composition(domainresource.DomainResource):
    __resource_type__: str
    attester: list[fhirtypes.CompositionAttesterType] | None
    author: list[fhirtypes.ReferenceType]
    category: list[fhirtypes.CodeableConceptType] | None
    custodian: fhirtypes.ReferenceType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    event: list[fhirtypes.CompositionEventType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    relatesTo: list[fhirtypes.RelatedArtifactType] | None
    section: list[fhirtypes.CompositionSectionType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: list[fhirtypes.ReferenceType] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CompositionAttester(backboneelement.BackboneElement):
    __resource_type__: str
    mode: fhirtypes.CodeableConceptType
    party: fhirtypes.ReferenceType | None
    time: fhirtypes.DateTimeType | None
    time__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class CompositionEvent(backboneelement.BackboneElement):
    __resource_type__: str
    detail: list[fhirtypes.CodeableReferenceType] | None
    period: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...

class CompositionSection(backboneelement.BackboneElement):
    __resource_type__: str
    author: list[fhirtypes.ReferenceType] | None
    code: fhirtypes.CodeableConceptType | None
    emptyReason: fhirtypes.CodeableConceptType | None
    entry: list[fhirtypes.ReferenceType] | None
    focus: fhirtypes.ReferenceType | None
    orderedBy: fhirtypes.CodeableConceptType | None
    section: list[fhirtypes.CompositionSectionType] | None
    text: fhirtypes.NarrativeType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
