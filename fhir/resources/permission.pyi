from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Permission(domainresource.DomainResource):
    __resource_type__: str
    asserter: fhirtypes.ReferenceType | None
    combining: fhirtypes.CodeType | None
    combining__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: list[fhirtypes.DateTimeType | None] | None
    date__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    justification: fhirtypes.PermissionJustificationType | None
    rule: list[fhirtypes.PermissionRuleType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    validity: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class PermissionJustification(backboneelement.BackboneElement):
    __resource_type__: str
    basis: list[fhirtypes.CodeableConceptType] | None
    evidence: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...

class PermissionRule(backboneelement.BackboneElement):
    __resource_type__: str
    activity: list[fhirtypes.PermissionRuleActivityType] | None
    data: list[fhirtypes.PermissionRuleDataType] | None
    limit: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class PermissionRuleActivity(backboneelement.BackboneElement):
    __resource_type__: str
    action: list[fhirtypes.CodeableConceptType] | None
    actor: list[fhirtypes.ReferenceType] | None
    purpose: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...

class PermissionRuleData(backboneelement.BackboneElement):
    __resource_type__: str
    expression: fhirtypes.ExpressionType | None
    period: list[fhirtypes.PeriodType] | None
    resource: list[fhirtypes.PermissionRuleDataResourceType] | None
    security: list[fhirtypes.CodingType] | None
    @classmethod
    def elements_sequence(cls): ...

class PermissionRuleDataResource(backboneelement.BackboneElement):
    __resource_type__: str
    meaning: fhirtypes.CodeType | None
    meaning__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    reference: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
