from _typeshed import Incomplete
from typing import Any

db_dtypes_import_exception: Incomplete
db_dtypes_import_exception = exc

def pyarrow_datetime(): ...
def pyarrow_numeric(): ...
def pyarrow_bignumeric(): ...
def pyarrow_time(): ...
def pyarrow_timestamp(): ...
def bq_to_arrow_scalars(bq_scalar: str): ...
def arrow_scalar_ids_to_bq(arrow_scalar: Any): ...
