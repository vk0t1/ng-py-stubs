from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Group(domainresource.DomainResource):
    __resource_type__: str
    active: bool | None
    active__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    actual: bool | None
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    characteristic: list[fhirtypes.GroupCharacteristicType] | None
    code: fhirtypes.CodeableConceptType | None
    identifier: list[fhirtypes.IdentifierType] | None
    member: list[fhirtypes.GroupMemberType] | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    quantity: fhirtypes.UnsignedIntType | None
    quantity__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class GroupCharacteristic(backboneelement.BackboneElement):
    __resource_type__: str
    code: fhirtypes.CodeableConceptType
    exclude: bool | None
    exclude__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    period: fhirtypes.PeriodType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCodeableConcept: fhirtypes.CodeableConceptType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueRange: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class GroupMember(backboneelement.BackboneElement):
    __resource_type__: str
    entity: fhirtypes.ReferenceType
    inactive: bool | None
    inactive__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    period: fhirtypes.PeriodType | None
    @classmethod
    def elements_sequence(cls): ...
