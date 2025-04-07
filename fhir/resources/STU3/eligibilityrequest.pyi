from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class EligibilityRequest(domainresource.DomainResource):
    __resource_type__: str
    benefitCategory: fhirtypes.CodeableConceptType | None
    benefitSubCategory: fhirtypes.CodeableConceptType | None
    businessArrangement: fhirtypes.StringType | None
    businessArrangement__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    coverage: fhirtypes.ReferenceType | None
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    enterer: fhirtypes.ReferenceType | None
    facility: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    insurer: fhirtypes.ReferenceType | None
    organization: fhirtypes.ReferenceType | None
    patient: fhirtypes.ReferenceType | None
    priority: fhirtypes.CodeableConceptType | None
    provider: fhirtypes.ReferenceType | None
    servicedDate: fhirtypes.DateType | None
    servicedDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    servicedPeriod: fhirtypes.PeriodType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
