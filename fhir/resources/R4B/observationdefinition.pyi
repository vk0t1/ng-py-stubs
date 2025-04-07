from . import backboneelement as backboneelement
from . import domainresource as domainresource
from . import fhirtypes as fhirtypes

class ObservationDefinition(domainresource.DomainResource):
    __resource_type__: str
    abnormalCodedValueSet: fhirtypes.ReferenceType | None
    category: list[fhirtypes.CodeableConceptType] | None
    code: fhirtypes.CodeableConceptType
    criticalCodedValueSet: fhirtypes.ReferenceType | None
    identifier: list[fhirtypes.IdentifierType] | None
    method: fhirtypes.CodeableConceptType | None
    multipleResultsAllowed: bool | None
    multipleResultsAllowed__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    normalCodedValueSet: fhirtypes.ReferenceType | None
    permittedDataType: list[fhirtypes.CodeType | None] | None
    permittedDataType__ext: list[fhirtypes.FHIRPrimitiveExtensionType | None] | None
    preferredReportName: fhirtypes.StringType | None
    preferredReportName__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    qualifiedInterval: list[fhirtypes.ObservationDefinitionQualifiedIntervalType] | None
    quantitativeDetails: fhirtypes.ObservationDefinitionQuantitativeDetailsType | None
    validCodedValueSet: fhirtypes.ReferenceType | None
    @classmethod
    def elements_sequence(cls): ...

class ObservationDefinitionQualifiedInterval(backboneelement.BackboneElement):
    __resource_type__: str
    age: fhirtypes.RangeType | None
    appliesTo: list[fhirtypes.CodeableConceptType] | None
    category: fhirtypes.CodeType | None
    category__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    condition: fhirtypes.StringType | None
    condition__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    context: fhirtypes.CodeableConceptType | None
    gender: fhirtypes.CodeType | None
    gender__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    gestationalAge: fhirtypes.RangeType | None
    range: fhirtypes.RangeType | None
    @classmethod
    def elements_sequence(cls): ...

class ObservationDefinitionQuantitativeDetails(backboneelement.BackboneElement):
    __resource_type__: str
    conversionFactor: fhirtypes.DecimalType | None
    conversionFactor__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    customaryUnit: fhirtypes.CodeableConceptType | None
    decimalPrecision: fhirtypes.IntegerType | None
    decimalPrecision__ext: fhirtypes.FHIRPrimitiveExtensionType | None
    unit: fhirtypes.CodeableConceptType | None
    @classmethod
    def elements_sequence(cls): ...
