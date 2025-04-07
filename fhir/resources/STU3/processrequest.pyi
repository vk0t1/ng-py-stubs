from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ProcessRequest(domainresource.DomainResource):
    __resource_type__: str
    action: fhirtypes.CodeType | None
    action__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    exclude: list[fhirtypes.StringType | None] | None
    exclude__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    identifier: list[fhirtypes.IdentifierType] | None
    include: list[fhirtypes.StringType | None] | None
    include__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    item: list[fhirtypes.ProcessRequestItemType] | None
    nullify: bool | None
    nullify__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    organization: fhirtypes.ReferenceType | None
    period: fhirtypes.PeriodType | None
    provider: fhirtypes.ReferenceType | None
    reference: fhirtypes.StringType | None
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    request: fhirtypes.ReferenceType | None
    response: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    target: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class ProcessRequestItem(backboneelement.BackboneElement):
    __resource_type__: str
    sequenceLinkId: fhirtypes.IntegerType | None
    sequenceLinkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
