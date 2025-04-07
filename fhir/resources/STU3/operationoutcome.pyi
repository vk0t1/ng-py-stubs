from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class OperationOutcome(domainresource.DomainResource):
    __resource_type__: str
    issue: list[fhirtypes.OperationOutcomeIssueType]
    @classmethod
    def elements_sequence(cls): ...

class OperationOutcomeIssue(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeType | None
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    details: fhirtypes.CodeableConceptType | None
    diagnostics: fhirtypes.StringType | None
    diagnostics__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    expression: list[fhirtypes.StringType | None] | None
    expression__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    location: list[fhirtypes.StringType | None] | None
    location__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    severity: fhirtypes.CodeType | None
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
