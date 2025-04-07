from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class List(domainresource.DomainResource):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    emptyReason: fhirtypes.CodeableConceptType | None
    encounter: fhirtypes.ReferenceType | None
    entry: list[fhirtypes.ListEntryType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    mode: fhirtypes.CodeType | None
    mode__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    orderedBy: fhirtypes.CodeableConceptType | None
    source: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class ListEntry(backboneelement.BackboneElement):
    __resource_type__: str
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    deleted: bool | None
    deleted__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    flag: fhirtypes.CodeableConceptType | None
    item: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
