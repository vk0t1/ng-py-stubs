import httpx
import typing
from .core.client_wrapper import AsyncClientWrapper as AsyncClientWrapper, SyncClientWrapper as SyncClientWrapper
from .resources.annotation_queues.client import AnnotationQueuesClient as AnnotationQueuesClient, AsyncAnnotationQueuesClient as AsyncAnnotationQueuesClient
from .resources.comments.client import AsyncCommentsClient as AsyncCommentsClient, CommentsClient as CommentsClient
from .resources.dataset_items.client import AsyncDatasetItemsClient as AsyncDatasetItemsClient, DatasetItemsClient as DatasetItemsClient
from .resources.dataset_run_items.client import AsyncDatasetRunItemsClient as AsyncDatasetRunItemsClient, DatasetRunItemsClient as DatasetRunItemsClient
from .resources.datasets.client import AsyncDatasetsClient as AsyncDatasetsClient, DatasetsClient as DatasetsClient
from .resources.health.client import AsyncHealthClient as AsyncHealthClient, HealthClient as HealthClient
from .resources.ingestion.client import AsyncIngestionClient as AsyncIngestionClient, IngestionClient as IngestionClient
from .resources.media.client import AsyncMediaClient as AsyncMediaClient, MediaClient as MediaClient
from .resources.metrics.client import AsyncMetricsClient as AsyncMetricsClient, MetricsClient as MetricsClient
from .resources.models.client import AsyncModelsClient as AsyncModelsClient, ModelsClient as ModelsClient
from .resources.observations.client import AsyncObservationsClient as AsyncObservationsClient, ObservationsClient as ObservationsClient
from .resources.projects.client import AsyncProjectsClient as AsyncProjectsClient, ProjectsClient as ProjectsClient
from .resources.prompt_version.client import AsyncPromptVersionClient as AsyncPromptVersionClient, PromptVersionClient as PromptVersionClient
from .resources.prompts.client import AsyncPromptsClient as AsyncPromptsClient, PromptsClient as PromptsClient
from .resources.score.client import AsyncScoreClient as AsyncScoreClient, ScoreClient as ScoreClient
from .resources.score_configs.client import AsyncScoreConfigsClient as AsyncScoreConfigsClient, ScoreConfigsClient as ScoreConfigsClient
from .resources.sessions.client import AsyncSessionsClient as AsyncSessionsClient, SessionsClient as SessionsClient
from .resources.trace.client import AsyncTraceClient as AsyncTraceClient, TraceClient as TraceClient
from _typeshed import Incomplete

class FernLangfuse:
    annotation_queues: Incomplete
    comments: Incomplete
    dataset_items: Incomplete
    dataset_run_items: Incomplete
    datasets: Incomplete
    health: Incomplete
    ingestion: Incomplete
    media: Incomplete
    metrics: Incomplete
    models: Incomplete
    observations: Incomplete
    projects: Incomplete
    prompt_version: Incomplete
    prompts: Incomplete
    score_configs: Incomplete
    score: Incomplete
    sessions: Incomplete
    trace: Incomplete
    def __init__(self, *, base_url: str, x_langfuse_sdk_name: str | None = None, x_langfuse_sdk_version: str | None = None, x_langfuse_public_key: str | None = None, username: str | typing.Callable[[], str] | None = None, password: str | typing.Callable[[], str] | None = None, timeout: float | None = None, follow_redirects: bool | None = True, httpx_client: httpx.Client | None = None) -> None: ...

class AsyncFernLangfuse:
    annotation_queues: Incomplete
    comments: Incomplete
    dataset_items: Incomplete
    dataset_run_items: Incomplete
    datasets: Incomplete
    health: Incomplete
    ingestion: Incomplete
    media: Incomplete
    metrics: Incomplete
    models: Incomplete
    observations: Incomplete
    projects: Incomplete
    prompt_version: Incomplete
    prompts: Incomplete
    score_configs: Incomplete
    score: Incomplete
    sessions: Incomplete
    trace: Incomplete
    def __init__(self, *, base_url: str, x_langfuse_sdk_name: str | None = None, x_langfuse_sdk_version: str | None = None, x_langfuse_public_key: str | None = None, username: str | typing.Callable[[], str] | None = None, password: str | typing.Callable[[], str] | None = None, timeout: float | None = None, follow_redirects: bool | None = True, httpx_client: httpx.AsyncClient | None = None) -> None: ...
