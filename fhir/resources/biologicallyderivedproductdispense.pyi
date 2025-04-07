from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class BiologicallyDerivedProductDispense(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    destination: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: fhirtypes.ReferenceType | None
    matchStatus: fhirtypes.CodeableConceptType | None
    note: list[fhirtypes.AnnotationType] | None
    originRelationshipType: fhirtypes.CodeableConceptType | None
    partOf: list[fhirtypes.ReferenceType] | None
    patient: fhirtypes.ReferenceType
    performer: list[fhirtypes.BiologicallyDerivedProductDispensePerformerType] | None
    preparedDate: fhirtypes.DateTimeType | None
    preparedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    product: fhirtypes.ReferenceType
    quantity: fhirtypes.QuantityType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    usageInstruction: fhirtypes.StringType | None
    usageInstruction__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    whenHandedOver: fhirtypes.DateTimeType | None
    whenHandedOver__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class BiologicallyDerivedProductDispensePerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    function: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
