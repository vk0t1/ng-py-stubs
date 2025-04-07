from _typeshed import Incomplete
from collections.abc import Generator
from google.api_core.exceptions import GoogleAPICallError as GoogleAPICallError

logger: Incomplete
HAS_OPENTELEMETRY: bool

def create_span(name, attributes: Incomplete | None = None, client: Incomplete | None = None, job_ref: Incomplete | None = None) -> Generator[Incomplete]: ...
