from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Procedure(domainresource.DomainResource):
    __resource_type__: str
    basedOn: list[fhirtypes.ReferenceType] | None
    bodySite: list[fhirtypes.CodeableConceptType] | None
    category: fhirtypes.CodeableConceptType | None
    code: fhirtypes.CodeableConceptType | None
    complication: list[fhirtypes.CodeableConceptType] | None
    complicationDetail: list[fhirtypes.ReferenceType] | None
    context: fhirtypes.ReferenceType | None
    definition: list[fhirtypes.ReferenceType] | None
    focalDevice: list[fhirtypes.ProcedureFocalDeviceType] | None
    followUp: list[fhirtypes.CodeableConceptType] | None
    identifier: list[fhirtypes.IdentifierType] | None
    location: fhirtypes.ReferenceType | None
    notDone: bool | None
    notDone__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    notDoneReason: fhirtypes.CodeableConceptType | None
    note: list[fhirtypes.AnnotationType] | None
    outcome: fhirtypes.CodeableConceptType | None
    partOf: list[fhirtypes.ReferenceType] | None
    performedDateTime: fhirtypes.DateTimeType | None
    performedDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    performedPeriod: fhirtypes.PeriodType | None
    performer: list[fhirtypes.ProcedurePerformerType] | None
    reasonCode: list[fhirtypes.CodeableConceptType] | None
    reasonReference: list[fhirtypes.ReferenceType] | None
    report: list[fhirtypes.ReferenceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType
    usedCode: list[fhirtypes.CodeableConceptType] | None
    usedReference: list[fhirtypes.ReferenceType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class ProcedureFocalDevice(backboneelement.BackboneElement):
    __resource_type__: str
    action: fhirtypes.CodeableConceptType | None
    manipulated: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...

class ProcedurePerformer(backboneelement.BackboneElement):
    __resource_type__: str
    actor: fhirtypes.ReferenceType
    onBehalfOf: fhirtypes.ReferenceType | None
    role: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
