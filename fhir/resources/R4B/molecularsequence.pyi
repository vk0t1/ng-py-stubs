from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class MolecularSequence(domainresource.DomainResource):
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
    quality: list[fhirtypes.MolecularSequenceQualityType] | None
    quantity: fhirtypes.QuantityType | None
    readCoverage: fhirtypes.IntegerType | None
    readCoverage__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    referenceSeq: fhirtypes.MolecularSequenceReferenceSeqType | None
    repository: list[fhirtypes.MolecularSequenceRepositoryType] | None
    specimen: fhirtypes.ReferenceType | None
    structureVariant: list[fhirtypes.MolecularSequenceStructureVariantType] | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    variant: list[fhirtypes.MolecularSequenceVariantType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class MolecularSequenceQuality(backboneelement.BackboneElement):
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
    roc: fhirtypes.MolecularSequenceQualityRocType | None
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

class MolecularSequenceQualityRoc(backboneelement.BackboneElement):
    __resource_type__: str
    fMeasure: list[fhirtypes.DecimalType | None] | None
    fMeasure__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    numFN: list[fhirtypes.IntegerType | None] | None
    numFN__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    numFP: list[fhirtypes.IntegerType | None] | None
    numFP__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    numTP: list[fhirtypes.IntegerType | None] | None
    numTP__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    precision: list[fhirtypes.DecimalType | None] | None
    precision__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    score: list[fhirtypes.IntegerType | None] | None
    score__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    sensitivity: list[fhirtypes.DecimalType | None] | None
    sensitivity__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    @classmethod
    def elements_sequence(cls): ...

class MolecularSequenceReferenceSeq(backboneelement.BackboneElement):
    __resource_type__: str
    chromosome: fhirtypes.CodeableConceptType | None
    genomeBuild: fhirtypes.StringType | None
    genomeBuild__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    orientation: fhirtypes.CodeType | None
    orientation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    referenceSeqId: fhirtypes.CodeableConceptType | None
    referenceSeqPointer: fhirtypes.ReferenceType | None
    referenceSeqString: fhirtypes.StringType | None
    referenceSeqString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    strand: fhirtypes.CodeType | None
    strand__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    windowEnd: fhirtypes.IntegerType | None
    windowEnd__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    windowStart: fhirtypes.IntegerType | None
    windowStart__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MolecularSequenceRepository(backboneelement.BackboneElement):
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

class MolecularSequenceStructureVariant(backboneelement.BackboneElement):
    __resource_type__: str
    exact: bool | None
    exact__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    inner: fhirtypes.MolecularSequenceStructureVariantInnerType | None
    length: fhirtypes.IntegerType | None
    length__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    outer: fhirtypes.MolecularSequenceStructureVariantOuterType | None
    variantType: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class MolecularSequenceStructureVariantInner(backboneelement.BackboneElement):
    __resource_type__: str
    end: fhirtypes.IntegerType | None
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    start: fhirtypes.IntegerType | None
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MolecularSequenceStructureVariantOuter(backboneelement.BackboneElement):
    __resource_type__: str
    end: fhirtypes.IntegerType | None
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    start: fhirtypes.IntegerType | None
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class MolecularSequenceVariant(backboneelement.BackboneElement):
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
