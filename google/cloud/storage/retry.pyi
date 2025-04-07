from _typeshed import Incomplete
from google.api_core import retry as retry
from google.cloud.storage.exceptions import InvalidResponse as InvalidResponse

DEFAULT_RETRY: Incomplete

class ConditionalRetryPolicy:
    retry_policy: Incomplete
    conditional_predicate: Incomplete
    required_kwargs: Incomplete
    def __init__(self, retry_policy, conditional_predicate, required_kwargs) -> None: ...
    def get_retry_policy_if_conditions_met(self, **kwargs): ...

def is_generation_specified(query_params): ...
def is_metageneration_specified(query_params): ...
def is_etag_in_data(data): ...
def is_etag_in_json(data): ...

DEFAULT_RETRY_IF_GENERATION_SPECIFIED: Incomplete
DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED: Incomplete
DEFAULT_RETRY_IF_ETAG_IN_JSON: Incomplete
