from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class QuestionnaireResponse(domainresource.DomainResource):
    __resource_type__: str
    author: fhirtypes.ReferenceType | None
    authored: fhirtypes.DateTimeType | None
    authored__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    basedOn: list[fhirtypes.ReferenceType] | None
    encounter: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    item: list[fhirtypes.QuestionnaireResponseItemType] | None
    partOf: list[fhirtypes.ReferenceType] | None
    questionnaire: fhirtypes.CanonicalType | None
    questionnaire__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    source: fhirtypes.ReferenceType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subject: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class QuestionnaireResponseItem(backboneelement.BackboneElement):
    __resource_type__: str
    answer: list[fhirtypes.QuestionnaireResponseItemAnswerType] | None
    definition: fhirtypes.UriType | None
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    item: list[fhirtypes.QuestionnaireResponseItemType] | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class QuestionnaireResponseItemAnswer(backboneelement.BackboneElement):
    __resource_type__: str
    item: list[fhirtypes.QuestionnaireResponseItemType] | None
    valueAttachment: fhirtypes.AttachmentType | None
    valueBoolean: bool | None
    valueBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCoding: fhirtypes.CodingType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDateTime: fhirtypes.DateTimeType | None
    valueDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueDecimal: fhirtypes.DecimalType | None
    valueDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueQuantity: fhirtypes.QuantityType | None
    valueReference: fhirtypes.ReferenceType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTime: fhirtypes.TimeType | None
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueUri: fhirtypes.UriType | None
    valueUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
