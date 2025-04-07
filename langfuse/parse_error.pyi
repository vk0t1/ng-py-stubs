from _typeshed import Incomplete
from langfuse.api.core import ApiError as ApiError
from langfuse.api.resources.commons.errors import AccessDeniedError as AccessDeniedError, Error as Error, MethodNotAllowedError as MethodNotAllowedError, NotFoundError as NotFoundError, UnauthorizedError as UnauthorizedError
from langfuse.api.resources.health.errors import ServiceUnavailableError as ServiceUnavailableError
from langfuse.request import APIError as APIError, APIErrors as APIErrors

SUPPORT_URL: str
API_DOCS_URL: str
RBAC_DOCS_URL: str
INSTALLATION_DOCS_URL: str
RATE_LIMITS_URL: str
PYPI_PACKAGE_URL: str
updatePromptResponse: Incomplete
defaultServerErrorPrompt: Incomplete
defaultErrorResponse: Incomplete
errorResponseByCode: Incomplete

def generate_error_message_fern(error: Error) -> str: ...
def handle_fern_exception(exception: Error) -> None: ...
def generate_error_message(exception: APIError | APIErrors | Exception) -> str: ...
def handle_exception(exception: APIError | APIErrors | Exception) -> None: ...
