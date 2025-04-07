from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class DetectedIssue(domainresource.DomainResource):
    __resource_type__: str
    author: fhirtypes.ReferenceType | None
    category: fhirtypes.CodeableConceptType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    detail: fhirtypes.StringType | None
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: fhirtypes.IdentifierType | None
    implicated: list[fhirtypes.ReferenceType] | None
    mitigation: list[fhirtypes.DetectedIssueMitigationType] | None
    patient: fhirtypes.ReferenceType | None
    reference: fhirtypes.UriType | None
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    severity: fhirtypes.CodeType | None
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class DetectedIssueMitigation(backboneelement.BackboneElement):
    __resource_type__: str
    action: fhirtypes.CodeableConceptType
    author: fhirtypes.ReferenceType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
