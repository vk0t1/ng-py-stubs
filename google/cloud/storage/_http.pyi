from _typeshed import Incomplete
from google.cloud import _http
from google.cloud.storage import __version__ as __version__
from google.cloud.storage._opentelemetry_tracing import create_trace_span as create_trace_span

class Connection(_http.JSONConnection):
    DEFAULT_API_ENDPOINT: Incomplete
    DEFAULT_API_MTLS_ENDPOINT: str
    API_BASE_URL: Incomplete
    API_BASE_MTLS_URL: Incomplete
    ALLOW_AUTO_SWITCH_TO_MTLS_URL: Incomplete
    def __init__(self, client, client_info: Incomplete | None = None, api_endpoint: Incomplete | None = None) -> None: ...
    API_VERSION: Incomplete
    API_URL_TEMPLATE: str
    def api_request(self, *args, **kwargs): ...
