from _typeshed import Incomplete
from google.api_core import exceptions as exceptions
from google.cloud.storage import Blob as Blob
from google.cloud.storage import Client as Client
from google.cloud.storage._media.requests.upload import XMLMPUContainer as XMLMPUContainer
from google.cloud.storage._media.requests.upload import XMLMPUPart as XMLMPUPart
from google.cloud.storage.exceptions import DataCorruption as DataCorruption
from google.cloud.storage.retry import DEFAULT_RETRY as DEFAULT_RETRY

TM_DEFAULT_CHUNK_SIZE: Incomplete
DEFAULT_MAX_WORKERS: int
MAX_CRC32C_ZERO_ARRAY_SIZE: Incomplete
METADATA_HEADER_TRANSLATION: Incomplete
PROCESS: str
THREAD: str
DOWNLOAD_CRC32C_MISMATCH_TEMPLATE: str

def upload_many(
    file_blob_pairs,
    skip_if_exists: bool = False,
    upload_kwargs: Incomplete | None = None,
    threads: Incomplete | None = None,
    deadline: Incomplete | None = None,
    raise_exception: bool = False,
    worker_type=...,
    max_workers=...,
): ...
def download_many(
    blob_file_pairs,
    download_kwargs: Incomplete | None = None,
    threads: Incomplete | None = None,
    deadline: Incomplete | None = None,
    raise_exception: bool = False,
    worker_type=...,
    max_workers=...,
    *,
    skip_if_exists: bool = False,
): ...
def upload_many_from_filenames(
    bucket,
    filenames,
    source_directory: str = "",
    blob_name_prefix: str = "",
    skip_if_exists: bool = False,
    blob_constructor_kwargs: Incomplete | None = None,
    upload_kwargs: Incomplete | None = None,
    threads: Incomplete | None = None,
    deadline: Incomplete | None = None,
    raise_exception: bool = False,
    worker_type=...,
    max_workers=...,
    *,
    additional_blob_attributes: Incomplete | None = None,
): ...
def download_many_to_path(
    bucket,
    blob_names,
    destination_directory: str = "",
    blob_name_prefix: str = "",
    download_kwargs: Incomplete | None = None,
    threads: Incomplete | None = None,
    deadline: Incomplete | None = None,
    create_directories: bool = True,
    raise_exception: bool = False,
    worker_type=...,
    max_workers=...,
    *,
    skip_if_exists: bool = False,
): ...
def download_chunks_concurrently(
    blob,
    filename,
    chunk_size=...,
    download_kwargs: Incomplete | None = None,
    deadline: Incomplete | None = None,
    worker_type=...,
    max_workers=...,
    *,
    crc32c_checksum: bool = True,
) -> None: ...
def upload_chunks_concurrently(
    filename,
    blob,
    content_type: Incomplete | None = None,
    chunk_size=...,
    deadline: Incomplete | None = None,
    worker_type=...,
    max_workers=...,
    *,
    checksum: str = "auto",
    timeout=...,
    retry=...,
) -> None: ...

class _ChecksummingSparseFileWrapper:
    f: Incomplete
    def __init__(self, filename, start_position, crc32c_enabled) -> None: ...
    def write(self, chunk) -> None: ...
    @property
    def crc(self): ...
    def __enter__(self): ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_value: BaseException | None, tb: types.TracebackType | None
    ) -> None: ...

class _LazyClient:
    def __new__(cls, id, *args, **kwargs): ...
