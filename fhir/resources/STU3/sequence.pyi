from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Sequence(domainresource.DomainResource):
    __resource_type__: str
    coordinateSystem: fhirtypes.IntegerType | None
    coordinateSystem__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    device: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    observedSeq: fhirtypes.StringType | None
    observedSeq__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    patient: fhirtypes.ReferenceType | None
    performer: fhirtypes.ReferenceType | None
    pointer: list[fhirtypes.ReferenceType] | None
    quality: list[fhirtypes.SequenceQualityType] | None
    quantity: fhirtypes.QuantityType | None
    readCoverage: fhirtypes.IntegerType | None
    readCoverage__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    referenceSeq: fhirtypes.SequenceReferenceSeqType | None
    repository: list[fhirtypes.SequenceRepositoryType] | None
    specimen: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    variant: list[fhirtypes.SequenceVariantType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SequenceQuality(backboneelement.BackboneElement):
    __resource_type__: str
    end: fhirtypes.IntegerType | None
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    fScore: fhirtypes.DecimalType | None
    fScore__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    gtFP: fhirtypes.DecimalType | None
    gtFP__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    method: fhirtypes.CodeableConceptType | None
    precision: fhirtypes.DecimalType | None
    precision__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    queryFP: fhirtypes.DecimalType | None
    queryFP__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    queryTP: fhirtypes.DecimalType | None
    queryTP__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    recall: fhirtypes.DecimalType | None
    recall__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    score: fhirtypes.QuantityType | None
    standardSequence: fhirtypes.CodeableConceptType | None
    start: fhirtypes.IntegerType | None
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    truthFN: fhirtypes.DecimalType | None
    truthFN__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    truthTP: fhirtypes.DecimalType | None
    truthTP__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SequenceReferenceSeq(backboneelement.BackboneElement):
    __resource_type__: str
    chromosome: fhirtypes.CodeableConceptType | None
    genomeBuild: fhirtypes.StringType | None
    genomeBuild__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    referenceSeqId: fhirtypes.CodeableConceptType | None
    referenceSeqPointer: fhirtypes.ReferenceType | None
    referenceSeqString: fhirtypes.StringType | None
    referenceSeqString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    strand: fhirtypes.IntegerType | None
    strand__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    windowEnd: fhirtypes.IntegerType | None
    windowEnd__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    windowStart: fhirtypes.IntegerType | None
    windowStart__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SequenceRepository(backboneelement.BackboneElement):
    __resource_type__: str
    datasetId: fhirtypes.StringType | None
    datasetId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    readsetId: fhirtypes.StringType | None
    readsetId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    variantsetId: fhirtypes.StringType | None
    variantsetId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class SequenceVariant(backboneelement.BackboneElement):
    __resource_type__: str
    cigar: fhirtypes.StringType | None
    cigar__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    end: fhirtypes.IntegerType | None
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    observedAllele: fhirtypes.StringType | None
    observedAllele__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    referenceAllele: fhirtypes.StringType | None
    referenceAllele__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    start: fhirtypes.IntegerType | None
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    variantPointer: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
