from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ResearchSubject(domainresource.DomainResource):
    __resource_type__: str
    actualArm: fhirtypes.StringType | None
    actualArm__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    assignedArm: fhirtypes.StringType | None
    assignedArm__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    consent: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    individual: fhirtypes.ReferenceType
    period: fhirtypes.PeriodType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    study: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
