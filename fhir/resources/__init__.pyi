from fhir_core.fhirabstractmodel import FHIRAbstractModel as FHIRAbstractModel

__version__: str
__fhir_version__: str

def get_fhir_model_class(model_name: str) -> type[FHIRAbstractModel]: ...
