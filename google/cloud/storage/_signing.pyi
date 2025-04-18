# mypy: ignore-errors

from typing import NamedTuple

from _typeshed import Incomplete
from google.auth import exceptions as exceptions
from google.auth.transport import requests as requests
from google.cloud.storage.retry import DEFAULT_RETRY as DEFAULT_RETRY

NOW: Incomplete
SERVICE_ACCOUNT_URL: str

def ensure_signed_credentials(credentials) -> None: ...
def get_signed_query_params_v2(credentials, expiration, string_to_sign): ...
def get_expiration_seconds_v2(expiration): ...
def get_expiration_seconds_v4(expiration): ...
def get_canonical_headers(headers): ...

class _Canonical(NamedTuple):
    method: Incomplete
    resource: Incomplete
    query_parameters: Incomplete
    headers: Incomplete

def canonicalize_v2(method, resource, query_parameters, headers): ...
def generate_signed_url_v2(
    credentials,
    resource,
    expiration,
    api_access_endpoint: str = "",
    method: str = "GET",
    content_md5: Incomplete | None = None,
    content_type: Incomplete | None = None,
    response_type: Incomplete | None = None,
    response_disposition: Incomplete | None = None,
    generation: Incomplete | None = None,
    headers: Incomplete | None = None,
    query_parameters: Incomplete | None = None,
    service_account_email: Incomplete | None = None,
    access_token: Incomplete | None = None,
    universe_domain: Incomplete | None = None,
): ...

SEVEN_DAYS: Incomplete
DEFAULT_ENDPOINT: str

def generate_signed_url_v4(
    credentials,
    resource,
    expiration,
    api_access_endpoint=...,
    method: str = "GET",
    content_md5: Incomplete | None = None,
    content_type: Incomplete | None = None,
    response_type: Incomplete | None = None,
    response_disposition: Incomplete | None = None,
    generation: Incomplete | None = None,
    headers: Incomplete | None = None,
    query_parameters: Incomplete | None = None,
    service_account_email: Incomplete | None = None,
    access_token: Incomplete | None = None,
    universe_domain: Incomplete | None = None,
    _request_timestamp: Incomplete | None = None,
): ...
def get_v4_now_dtstamps(): ...
