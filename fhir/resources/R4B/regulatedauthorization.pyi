from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class RegulatedAuthorization(domainresource.DomainResource):
    __resource_type__: str
    basis: list[fhirtypes.CodeableConceptType] | None
    case: fhirtypes.RegulatedAuthorizationCaseType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    holder: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    indication: fhirtypes.CodeableReferenceType | None
    intendedUse: fhirtypes.CodeableConceptType | None
    region: list[fhirtypes.CodeableConceptType] | None
    regulator: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeableConceptType | None
    statusDate: fhirtypes.DateTimeType | None
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: list[fhirtypes.ReferenceType] | None
    type: fhirtypes.CodeableConceptType | None
    validityPeriod: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...

class RegulatedAuthorizationCase(backboneelement.BackboneElement):
    __resource_type__: str
    application: list[fhirtypes.RegulatedAuthorizationCaseType] | None
    dateDateTime: fhirtypes.DateTimeType | None
    dateDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    datePeriod: fhirtypes.PeriodType | None
    identifier: fhirtypes.IdentifierType | None
    status: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
