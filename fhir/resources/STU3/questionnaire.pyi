from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Questionnaire(domainresource.DomainResource):
    __resource_type__: str
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    code: list[fhirtypes.CodingType] | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    effectivePeriod: fhirtypes.PeriodType | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    item: list[fhirtypes.QuestionnaireItemType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    subjectType: list[fhirtypes.CodeType | None] | None
    subjectType__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    useContext: list[fhirtypes.UsageContextType] | None
    version: fhirtypes.StringType | None
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class QuestionnaireItem(backboneelement.BackboneElement):
    __resource_type__: str
    code: list[fhirtypes.CodingType] | None
    definition: fhirtypes.UriType | None
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    enableWhen: list[fhirtypes.QuestionnaireItemEnableWhenType] | None
    initialAttachment: fhirtypes.AttachmentType | None
    initialBoolean: bool | None
    initialBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    initialCoding: fhirtypes.CodingType | None
    initialDate: fhirtypes.DateType | None
    initialDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    initialDateTime: fhirtypes.DateTimeType | None
    initialDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    initialDecimal: fhirtypes.DecimalType | None
    initialDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    initialInteger: fhirtypes.IntegerType | None
    initialInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    initialQuantity: fhirtypes.QuantityType | None
    initialReference: fhirtypes.ReferenceType | None
    initialString: fhirtypes.StringType | None
    initialString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    initialTime: fhirtypes.TimeType | None
    initialTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    initialUri: fhirtypes.UriType | None
    initialUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    item: list[fhirtypes.QuestionnaireItemType] | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxLength: fhirtypes.IntegerType | None
    maxLength__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    option: list[fhirtypes.QuestionnaireItemOptionType] | None
    options: fhirtypes.ReferenceType | None
    prefix: fhirtypes.StringType | None
    prefix__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    readOnly: bool | None
    readOnly__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    repeats: bool | None
    repeats__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    required: bool | None
    required__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeType | None
    type__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    __resource_type__: str
    answerAttachment: fhirtypes.AttachmentType | None
    answerBoolean: bool | None
    answerBoolean__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    answerCoding: fhirtypes.CodingType | None
    answerDate: fhirtypes.DateType | None
    answerDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    answerDateTime: fhirtypes.DateTimeType | None
    answerDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    answerDecimal: fhirtypes.DecimalType | None
    answerDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    answerInteger: fhirtypes.IntegerType | None
    answerInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    answerQuantity: fhirtypes.QuantityType | None
    answerReference: fhirtypes.ReferenceType | None
    answerString: fhirtypes.StringType | None
    answerString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    answerTime: fhirtypes.TimeType | None
    answerTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    answerUri: fhirtypes.UriType | None
    answerUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    hasAnswer: bool | None
    hasAnswer__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    question: fhirtypes.StringType | None
    question__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class QuestionnaireItemOption(backboneelement.BackboneElement):
    __resource_type__: str
    valueCoding: fhirtypes.CodingType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTime: fhirtypes.TimeType | None
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...
