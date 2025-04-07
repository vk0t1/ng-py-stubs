from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class Citation(domainresource.DomainResource):
    __resource_type__: str
    approvalDate: fhirtypes.DateType | None
    approvalDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    author: list[fhirtypes.ContactDetailType] | None
    citedArtifact: fhirtypes.CitationCitedArtifactType | None
    classification: list[fhirtypes.CitationClassificationType] | None
    contact: list[fhirtypes.ContactDetailType] | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    currentState: list[fhirtypes.CodeableConceptType] | None
    date: fhirtypes.DateTimeType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    description: fhirtypes.MarkdownType | None
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    editor: list[fhirtypes.ContactDetailType] | None
    effectivePeriod: fhirtypes.PeriodType | None
    endorser: list[fhirtypes.ContactDetailType] | None
    experimental: bool | None
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    jurisdiction: list[fhirtypes.CodeableConceptType] | None
    lastReviewDate: fhirtypes.DateType | None
    lastReviewDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.StringType | None
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    note: list[fhirtypes.AnnotationType] | None
    publisher: fhirtypes.StringType | None
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    purpose: fhirtypes.MarkdownType | None
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    relatesTo: list[fhirtypes.CitationRelatesToType] | None
    reviewer: list[fhirtypes.ContactDetailType] | None
    status: fhirtypes.CodeType | None
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    statusDate: list[fhirtypes.CitationStatusDateType] | None
    summary: list[fhirtypes.CitationSummaryType] | None
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

class CitationCitedArtifact(backboneelement.BackboneElement):
    __resource_type__: str
    abstract: list[fhirtypes.CitationCitedArtifactAbstractType] | None
    classification: list[fhirtypes.CitationCitedArtifactClassificationType] | None
    contributorship: fhirtypes.CitationCitedArtifactContributorshipType | None
    currentState: list[fhirtypes.CodeableConceptType] | None
    dateAccessed: fhirtypes.DateTimeType | None
    dateAccessed__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    note: list[fhirtypes.AnnotationType] | None
    part: fhirtypes.CitationCitedArtifactPartType | None
    publicationForm: list[fhirtypes.CitationCitedArtifactPublicationFormType] | None
    relatedIdentifier: list[fhirtypes.IdentifierType] | None
    relatesTo: list[fhirtypes.CitationCitedArtifactRelatesToType] | None
    statusDate: list[fhirtypes.CitationCitedArtifactStatusDateType] | None
    title: list[fhirtypes.CitationCitedArtifactTitleType] | None
    version: fhirtypes.CitationCitedArtifactVersionType | None
    webLocation: list[fhirtypes.CitationCitedArtifactWebLocationType] | None
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactAbstract(backboneelement.BackboneElement):
    __resource_type__: str
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    language: fhirtypes.CodeableConceptType | None
    text: fhirtypes.MarkdownType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CitationCitedArtifactClassification(backboneelement.BackboneElement):
    __resource_type__: str
    classifier: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType | None
    whoClassified: fhirtypes.CitationCitedArtifactClassificationWhoClassifiedType | None
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactClassificationWhoClassified(backboneelement.BackboneElement):
    __resource_type__: str
    classifierCopyright: fhirtypes.StringType | None
    classifierCopyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    freeToShare: bool | None
    freeToShare__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    organization: fhirtypes.ReferenceType | None
    person: fhirtypes.ReferenceType | None
    publisher: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactContributorship(backboneelement.BackboneElement):
    __resource_type__: str
    complete: bool | None
    complete__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    entry: list[fhirtypes.CitationCitedArtifactContributorshipEntryType] | None
    summary: list[fhirtypes.CitationCitedArtifactContributorshipSummaryType] | None
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactContributorshipEntry(backboneelement.BackboneElement):
    __resource_type__: str
    address: list[fhirtypes.AddressType] | None
    affiliationInfo: list[fhirtypes.CitationCitedArtifactContributorshipEntryAffiliationInfoType] | None
    collectiveName: fhirtypes.StringType | None
    collectiveName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    contributionInstance: list[fhirtypes.CitationCitedArtifactContributorshipEntryContributionInstanceType] | None
    contributionType: list[fhirtypes.CodeableConceptType] | None
    correspondingContact: bool | None
    correspondingContact__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    initials: fhirtypes.StringType | None
    initials__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    listOrder: fhirtypes.PositiveIntType | None
    listOrder__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    name: fhirtypes.HumanNameType | None
    role: fhirtypes.CodeableConceptType | None
    telecom: list[fhirtypes.ContactPointType] | None
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactContributorshipEntryAffiliationInfo(backboneelement.BackboneElement):
    __resource_type__: str
    affiliation: fhirtypes.StringType | None
    affiliation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    identifier: list[fhirtypes.IdentifierType] | None
    role: fhirtypes.StringType | None
    role__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactContributorshipEntryContributionInstance(backboneelement.BackboneElement):
    __resource_type__: str
    time: fhirtypes.DateTimeType | None
    time__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactContributorshipSummary(backboneelement.BackboneElement):
    __resource_type__: str
    source: fhirtypes.CodeableConceptType | None
    style: fhirtypes.CodeableConceptType | None
    type: fhirtypes.CodeableConceptType | None
    value: fhirtypes.MarkdownType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CitationCitedArtifactPart(backboneelement.BackboneElement):
    __resource_type__: str
    baseCitation: fhirtypes.ReferenceType | None
    type: fhirtypes.CodeableConceptType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactPublicationForm(backboneelement.BackboneElement):
    __resource_type__: str
    accessionNumber: fhirtypes.StringType | None
    accessionNumber__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    articleDate: fhirtypes.DateTimeType | None
    articleDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    copyright: fhirtypes.MarkdownType | None
    copyright__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    firstPage: fhirtypes.StringType | None
    firstPage__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    language: list[fhirtypes.CodeableConceptType] | None
    lastPage: fhirtypes.StringType | None
    lastPage__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    lastRevisionDate: fhirtypes.DateTimeType | None
    lastRevisionDate__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    pageCount: fhirtypes.StringType | None
    pageCount__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    pageString: fhirtypes.StringType | None
    pageString__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    periodicRelease: fhirtypes.CitationCitedArtifactPublicationFormPeriodicReleaseType | None
    publishedIn: fhirtypes.CitationCitedArtifactPublicationFormPublishedInType | None
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactPublicationFormPeriodicRelease(backboneelement.BackboneElement):
    __resource_type__: str
    citedMedium: fhirtypes.CodeableConceptType | None
    dateOfPublication: fhirtypes.CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublicationType | None
    issue: fhirtypes.StringType | None
    issue__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    volume: fhirtypes.StringType | None
    volume__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactPublicationFormPeriodicReleaseDateOfPublication(backboneelement.BackboneElement):
    __resource_type__: str
    date: fhirtypes.DateType | None
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    day: fhirtypes.StringType | None
    day__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    month: fhirtypes.StringType | None
    month__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    season: fhirtypes.StringType | None
    season__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    text: fhirtypes.StringType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    year: fhirtypes.StringType | None
    year__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactPublicationFormPublishedIn(backboneelement.BackboneElement):
    __resource_type__: str
    identifier: list[fhirtypes.IdentifierType] | None
    publisher: fhirtypes.ReferenceType | None
    publisherLocation: fhirtypes.StringType | None
    publisherLocation__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    title: fhirtypes.StringType | None
    title__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactRelatesTo(backboneelement.BackboneElement):
    __resource_type__: str
    relationshipType: fhirtypes.CodeableConceptType
    targetAttachment: fhirtypes.AttachmentType | None
    targetClassifier: list[fhirtypes.CodeableConceptType] | None
    targetIdentifier: fhirtypes.IdentifierType | None
    targetReference: fhirtypes.ReferenceType | None
    targetUri: fhirtypes.UriType | None
    targetUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class CitationCitedArtifactStatusDate(backboneelement.BackboneElement):
    __resource_type__: str
    activity: fhirtypes.CodeableConceptType
    actual: bool | None
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    period: fhirtypes.PeriodType
    @classmethod
    def elements_sequence(cls): ...

class CitationCitedArtifactTitle(backboneelement.BackboneElement):
    __resource_type__: str
    language: fhirtypes.CodeableConceptType | None
    text: fhirtypes.MarkdownType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    type: list[fhirtypes.CodeableConceptType] | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CitationCitedArtifactVersion(backboneelement.BackboneElement):
    __resource_type__: str
    baseCitation: fhirtypes.ReferenceType | None
    value: fhirtypes.StringType | None
    value__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...

class CitationCitedArtifactWebLocation(backboneelement.BackboneElement):
    __resource_type__: str
    type: fhirtypes.CodeableConceptType | None
    url: fhirtypes.UriType | None
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...

class CitationClassification(backboneelement.BackboneElement):
    __resource_type__: str
    classifier: list[fhirtypes.CodeableConceptType] | None
    type: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...

class CitationRelatesTo(backboneelement.BackboneElement):
    __resource_type__: str
    relationshipType: fhirtypes.CodeableConceptType
    targetAttachment: fhirtypes.AttachmentType | None
    targetClassifier: list[fhirtypes.CodeableConceptType] | None
    targetIdentifier: fhirtypes.IdentifierType | None
    targetReference: fhirtypes.ReferenceType | None
    targetUri: fhirtypes.UriType | None
    targetUri__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_one_of_many_fields(self) -> dict[str, list[str]]: ...

class CitationStatusDate(backboneelement.BackboneElement):
    __resource_type__: str
    activity: fhirtypes.CodeableConceptType
    actual: bool | None
    actual__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    period: fhirtypes.PeriodType
    @classmethod
    def elements_sequence(cls): ...

class CitationSummary(backboneelement.BackboneElement):
    __resource_type__: str
    style: fhirtypes.CodeableConceptType | None
    text: fhirtypes.MarkdownType | None
    text__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    @classmethod
    def elements_sequence(cls): ...
    def get_required_fields(self) -> list[tuple[str, str]]: ...
