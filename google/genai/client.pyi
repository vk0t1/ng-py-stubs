import google.auth
import pydantic

from ._api_client import BaseApiClient as BaseApiClient
from ._api_client import HttpOptions as HttpOptions
from ._api_client import HttpOptionsDict as HttpOptionsDict
from ._replay_api_client import ReplayApiClient as ReplayApiClient
from .batches import AsyncBatches as AsyncBatches
from .batches import Batches as Batches
from .caches import AsyncCaches as AsyncCaches
from .caches import Caches as Caches
from .chats import AsyncChats as AsyncChats
from .chats import Chats as Chats
from .files import AsyncFiles as AsyncFiles
from .files import Files as Files
from .live import AsyncLive as AsyncLive
from .models import AsyncModels as AsyncModels
from .models import Models as Models
from .operations import AsyncOperations as AsyncOperations
from .operations import Operations as Operations
from .tunings import AsyncTunings as AsyncTunings
from .tunings import Tunings as Tunings

class AsyncClient:
    def __init__(self, api_client: BaseApiClient) -> None: ...
    @property
    def models(self) -> AsyncModels: ...
    @property
    def tunings(self) -> AsyncTunings: ...
    @property
    def caches(self) -> AsyncCaches: ...
    @property
    def batches(self) -> AsyncBatches: ...
    @property
    def chats(self) -> AsyncChats: ...
    @property
    def files(self) -> AsyncFiles: ...
    @property
    def live(self) -> AsyncLive: ...
    @property
    def operations(self) -> AsyncOperations: ...

class DebugConfig(pydantic.BaseModel):
    client_mode: str | None
    replays_directory: str | None
    replay_id: str | None

class Client:
    def __init__(
        self,
        *,
        vertexai: bool | None = None,
        api_key: str | None = None,
        credentials: google.auth.credentials.Credentials | None = None,
        project: str | None = None,
        location: str | None = None,
        debug_config: DebugConfig | None = None,
        http_options: HttpOptions | HttpOptionsDict | None = None,
    ) -> None: ...
    @property
    def chats(self) -> Chats: ...
    @property
    def aio(self) -> AsyncClient: ...
    @property
    def models(self) -> Models: ...
    @property
    def tunings(self) -> Tunings: ...
    @property
    def caches(self) -> Caches: ...
    @property
    def batches(self) -> Batches: ...
    @property
    def files(self) -> Files: ...
    @property
    def operations(self) -> Operations: ...
    @property
    def vertexai(self) -> bool: ...
