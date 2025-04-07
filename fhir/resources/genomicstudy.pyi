from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class GenomicStudy(domainresource.DomainResource):
    __resource_type__: str
    analysis: list[fhirtypes.GenomicStudyAnalysisType] | None
    basedOn: list[fhirtypes.ReferenceType] | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    instantiatesCanonical: fhirtypes.CanonicalType | None
    instantiatesCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    instantiatesUri: fhirtypes.UriType | None
    instantiatesUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    interpreter: list[fhirtypes.ReferenceType] | None
    note: list[fhirtypes.AnnotationType] | None
    reason: list[fhirtypes.CodeableReferenceType] | None
    referrer: fhirtypes.ReferenceType | None
    startDate: fhirtypes.DateTimeType | None
    startDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class GenomicStudyAnalysis(backboneelement.BackboneElement):
    __resource_type__: str
    changeType: list[fhirtypes.CodeableConceptType] | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    device: list[fhirtypes.GenomicStudyAnalysisDeviceType] | None
    focus: list[fhirtypes.ReferenceType] | None
    genomeBuild: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    input: list[fhirtypes.GenomicStudyAnalysisInputType] | None
    instantiatesCanonical: fhirtypes.CanonicalType | None
    instantiatesCanonical__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    instantiatesUri: fhirtypes.UriType | None
    instantiatesUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    methodType: list[fhirtypes.CodeableConceptType] | None
    note: list[fhirtypes.AnnotationType] | None
    output: list[fhirtypes.GenomicStudyAnalysisOutputType] | None
    performer: list[fhirtypes.GenomicStudyAnalysisPerformerType] | None
    protocolPerformed: fhirtypes.ReferenceType | None
    regionsCalled: list[fhirtypes.ReferenceType] | None
    regionsStudied: list[fhirtypes.ReferenceType] | None
    specimen: list[fhirtypes.ReferenceType] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class GenomicStudyAnalysisDevice(backboneelement.BackboneElement):
    __resource_type__: str
    device: fhirtypes.ReferenceType | None
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class GenomicStudyAnalysisInput(backboneelement.BackboneElement):
    __resource_type__: str
    file: fhirtypes.ReferenceType | None
    generatedByIdentifier: fhirtypes.IdentifierType | None
    generatedByReference: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class GenomicStudyAnalysisOutput(backboneelement.BackboneElement):
    __resource_type__: str
    file: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class GenomicStudyAnalysisPerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType | None
    role: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
