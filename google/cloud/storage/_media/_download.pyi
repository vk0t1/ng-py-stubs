from _typeshed import Incomplete
from google.cloud.storage.exceptions import InvalidResponse as InvalidResponse
from google.cloud.storage.retry import DEFAULT_RETRY as DEFAULT_RETRY

class DownloadBase:
    media_url: Incomplete
    start: Incomplete
    end: Incomplete
    def __init__(
        self,
        media_url,
        stream: Incomplete | None = None,
        start: Incomplete | None = None,
        end: Incomplete | None = None,
        headers: Incomplete | None = None,
        retry=...,
    ) -> None: ...
    @property
    def finished(self): ...

class Download(DownloadBase):
    checksum: Incomplete
    def __init__(
        self,
        media_url,
        stream: Incomplete | None = None,
        start: Incomplete | None = None,
        end: Incomplete | None = None,
        headers: Incomplete | None = None,
        checksum: str = "auto",
        retry=...,
    ) -> None: ...
    def consume(self, transport, timeout: Incomplete | None = None) -> None: ...

class ChunkedDownload(DownloadBase):
    chunk_size: Incomplete
    def __init__(
        self,
        media_url,
        chunk_size,
        stream,
        start: int = 0,
        end: Incomplete | None = None,
        headers: Incomplete | None = None,
        retry=...,
    ) -> None: ...
    @property
    def bytes_downloaded(self): ...
    @property
    def total_bytes(self): ...
    @property
    def invalid(self): ...
    def consume_next_chunk(self, transport, timeout: Incomplete | None = None) -> None: ...

def add_bytes_range(start, end, headers) -> None: ...
def get_range_info(response, get_headers, callback=...): ...
