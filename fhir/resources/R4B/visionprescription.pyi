from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class VisionPrescription(domainresource.DomainResource):
    __resource_type__: str
    created: fhirtypes.DateTimeType | None
    created__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    dateWritten: fhirtypes.DateTimeType | None
    dateWritten__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    encounter: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    lensSpecification: list[fhirtypes.VisionPrescriptionLensSpecificationType]
    patient: fhirtypes.ReferenceType
    prescriber: fhirtypes.ReferenceType
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class VisionPrescriptionLensSpecification(backboneelement.BackboneElement):
    __resource_type__: str
    add: fhirtypes.DecimalType | None
    add__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    axis: fhirtypes.IntegerType | None
    axis__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    backCurve: fhirtypes.DecimalType | None
    backCurve__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    brand: fhirtypes.StringType | None
    brand__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    color: fhirtypes.StringType | None
    color__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    cylinder: fhirtypes.DecimalType | None
    cylinder__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    diameter: fhirtypes.DecimalType | None
    diameter__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    duration: fhirtypes.QuantityType | None
    eye: fhirtypes.CodeType | None
    eye__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    power: fhirtypes.DecimalType | None
    power__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    prism: list[fhirtypes.VisionPrescriptionLensSpecificationPrismType] | None
    product: fhirtypes.CodeableConceptType
    sphere: fhirtypes.DecimalType | None
    sphere__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class VisionPrescriptionLensSpecificationPrism(backboneelement.BackboneElement):
    __resource_type__: str
    amount: fhirtypes.DecimalType | None
    amount__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    base: fhirtypes.CodeType | None
    base__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
