from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class SubstanceReferenceInformation(domainresource.DomainResource):
    __resource_type__: str
    comment: fhirtypes.StringType | None
    comment__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    gene: list[fhirtypes.SubstanceReferenceInformationGeneType] | None
    geneElement: list[fhirtypes.SubstanceReferenceInformationGeneElementType] | None
    target: list[fhirtypes.SubstanceReferenceInformationTargetType] | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceReferenceInformationGene(backboneelement.BackboneElement):
    __resource_type__: str
    gene: fhirtypes.CodeableConceptType | None
    geneSequenceOrigin: fhirtypes.CodeableConceptType | None
    source: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceReferenceInformationGeneElement(backboneelement.BackboneElement):
    __resource_type__: str
    element: fhirtypes.IdentifierType | None
    source: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class SubstanceReferenceInformationTarget(backboneelement.BackboneElement):
    __resource_type__: str
    amountQuantity: fhirtypes.QuantityType | None
    amountRange: fhirtypes.RangeType | None
    amountString: fhirtypes.StringType | None
    amountString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    amountType: fhirtypes.CodeableConceptType | None
    interaction: fhirtypes.CodeableConceptType | None
    organism: fhirtypes.CodeableConceptType | None
    organismType: fhirtypes.CodeableConceptType | None
    source: list[fhirtypes.ReferenceType] | None
    target: fhirtypes.IdentifierType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
