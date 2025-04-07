import requests
from _typeshed import Incomplete
from email.mime.application import MIMEApplication
from google.cloud import exceptions as exceptions
from google.cloud.storage._http import Connection as Connection

class MIMEApplicationHTTP(MIMEApplication):
    def __init__(self, method, uri, headers, body) -> None: ...

class _FutureDict:
    @staticmethod
    def get(key, default: Incomplete | None = None) -> None: ...
    def __getitem__(self, key) -> None: ...
    def __setitem__(self, key, value) -> None: ...

class _FutureResponse(requests.Response):
    status_code: int
    def __init__(self, future_dict) -> None: ...
    def json(self): ...
    @property
    def content(self): ...

class Batch(Connection):
    def __init__(self, client, raise_exception: bool = True) -> None: ...
    def finish(self, raise_exception: bool = True): ...
    def current(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
