from _typeshed import Incomplete
from google.cloud import _http
from google.cloud.bigquery import __version__ as __version__

class Connection(_http.JSONConnection):
    DEFAULT_API_ENDPOINT: str
    DEFAULT_API_MTLS_ENDPOINT: str
    API_BASE_URL: Incomplete
    API_BASE_MTLS_URL: Incomplete
    ALLOW_AUTO_SWITCH_TO_MTLS_URL: Incomplete
    def __init__(self, client, client_info: Incomplete | None = None, api_endpoint: Incomplete | None = None) -> None: ...
    API_VERSION: str
    API_URL_TEMPLATE: str
