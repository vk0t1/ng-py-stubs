from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class VerificationResult(domainresource.DomainResource):
    __resource_type__: str
    attestation: fhirtypes.VerificationResultAttestationType | None
    failureAction: fhirtypes.CodeableConceptType | None
    frequency: fhirtypes.TimingType | None
    lastPerformed: fhirtypes.DateTimeType | None
    lastPerformed__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    need: fhirtypes.CodeableConceptType | None
    nextScheduled: fhirtypes.DateType | None
    nextScheduled__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    primarySource: list[fhirtypes.VerificationResultPrimarySourceType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusDate: fhirtypes.DateTimeType | None
    statusDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    target: list[fhirtypes.ReferenceType] | None
    targetLocation: list[fhirtypes.StringType | None] | None
    targetLocation__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    validationProcess: list[fhirtypes.CodeableConceptType] | None
    validationType: fhirtypes.CodeableConceptType | None
    validator: list[fhirtypes.VerificationResultValidatorType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class VerificationResultAttestation(backboneelement.BackboneElement):
    __resource_type__: str
    communicationMethod: fhirtypes.CodeableConceptType | None
    date: fhirtypes.DateType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    onBehalfOf: fhirtypes.ReferenceType | None
    proxyIdentityCertificate: fhirtypes.StringType | None
    proxyIdentityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    proxySignature: fhirtypes.SignatureType | None
    sourceIdentityCertificate: fhirtypes.StringType | None
    sourceIdentityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    sourceSignature: fhirtypes.SignatureType | None
    who: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class VerificationResultPrimarySource(backboneelement.BackboneElement):
    __resource_type__: str
    canPushUpdates: fhirtypes.CodeableConceptType | None
    communicationMethod: list[fhirtypes.CodeableConceptType] | None
    pushTypeAvailable: list[fhirtypes.CodeableConceptType] | None
    type: list[fhirtypes.CodeableConceptType] | None
    validationDate: fhirtypes.DateTimeType | None
    validationDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    validationStatus: fhirtypes.CodeableConceptType | None
    who: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class VerificationResultValidator(backboneelement.BackboneElement):
    __resource_type__: str
    attestationSignature: fhirtypes.SignatureType | None
    identityCertificate: fhirtypes.StringType | None
    identityCertificate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    organization: fhirtypes.ReferenceType
    @classmethod
    def elements_sequence(cls): ...
