from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ProcessResponse(domainresource.DomainResource):
    __resource_type__: str
    communicationRequest: list[fhirtypes.ReferenceType] | None
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    disposition: fhirtypes.StringType | None
    disposition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    error: list[fhirtypes.CodeableConceptType] | None
    form: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    organization: fhirtypes.ReferenceType | None
    outcome: fhirtypes.CodeableConceptType | None
    processNote: list[fhirtypes.ProcessResponseProcessNoteType] | None
    request: fhirtypes.ReferenceType | None
    requestOrganization: fhirtypes.ReferenceType | None
    requestProvider: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class ProcessResponseProcessNote(backboneelement.BackboneElement):
    __resource_type__: str
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
