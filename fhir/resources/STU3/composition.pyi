from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Composition(domainresource.DomainResource):
    __resource_type__: str
    attester: list[fhirtypes.CompositionAttesterType] | None
    author: list[fhirtypes.ReferenceType]
    class_fhir: fhirtypes.CodeableConceptType | None
    confidentiality: fhirtypes.CodeType | None
    confidentiality__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    custodian: fhirtypes.ReferenceType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    event: list[fhirtypes.CompositionEventType] | None
    identifier: fhirtypes.IdentifierType | None
    relatesTo: list[fhirtypes.CompositionRelatesToType] | None
    section: list[fhirtypes.CompositionSectionType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CompositionAttester(backboneelement.BackboneElement):
    __resource_type__: str
    mode: list[fhirtypes.CodeType | None] | None
    mode__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    party: fhirtypes.ReferenceType | None
    time: fhirtypes.DateTimeType | None
    time__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CompositionEvent(backboneelement.BackboneElement):
    __resource_type__: str
    code: list[fhirtypes.CodeableConceptType] | None
    detail: list[fhirtypes.ReferenceType] | None
    period: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...

class CompositionRelatesTo(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    targetIdentifier: fhirtypes.IdentifierType | None
    targetReference: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class CompositionSection(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    emptyReason: fhirtypes.CodeableConceptType | None
    entry: list[fhirtypes.ReferenceType] | None
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    orderedBy: fhirtypes.CodeableConceptType | None
    section: list[fhirtypes.CompositionSectionType] | None
    text: fhirtypes.NarrativeType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
