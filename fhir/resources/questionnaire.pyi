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
    copyrightLabel: fhirtypes.StringType | None
    copyrightLabel__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    derivedFrom: list[fhirtypes.CanonicalType | None] | None
    derivedFrom__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
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
    versionAlgorithmCoding: fhirtypes.CodingType | None
    versionAlgorithmString: fhirtypes.StringType | None
    versionAlgorithmString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class QuestionnaireItem(backboneelement.BackboneElement):
    __resource_type__: str
    answerConstraint: fhirtypes.CodeType | None
    answerConstraint__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    answerOption: list[fhirtypes.QuestionnaireItemAnswerOptionType] | None
    answerValueSet: fhirtypes.CanonicalType | None
    answerValueSet__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    code: list[fhirtypes.CodingType] | None
    definition: fhirtypes.UriType | None
    definition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    disabledDisplay: fhirtypes.CodeType | None
    disabledDisplay__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    enableBehavior: fhirtypes.CodeType | None
    enableBehavior__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    enableWhen: list[fhirtypes.QuestionnaireItemEnableWhenType] | None
    initial: list[fhirtypes.QuestionnaireItemInitialType] | None
    item: list[fhirtypes.QuestionnaireItemType] | None
    linkId: fhirtypes.StringType | None
    linkId__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    maxLength: fhirtypes.IntegerType | None
    maxLength__ext: fhirtypes.FHIRPrimitiveExtensionType | None
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

class QuestionnaireItemAnswerOption(backboneelement.BackboneElement):
    __resource_type__: str
    initialSelected: bool | None
    initialSelected__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueCoding: fhirtypes.CodingType | None
    valueDate: fhirtypes.DateType | None
    valueDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueInteger: fhirtypes.IntegerType | None
    valueInteger__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueReference: fhirtypes.ReferenceType | None
    valueString: fhirtypes.StringType | None
    valueString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    valueTime: fhirtypes.TimeType | None
    valueTime__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class QuestionnaireItemEnableWhen(backboneelement.BackboneElement):
    __resource_type__: str
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
    operator: fhirtypes.CodeType | None
    operator__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    question: fhirtypes.StringType | None
    question__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class QuestionnaireItemInitial(backboneelement.BackboneElement):
    __resource_type__: str
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
