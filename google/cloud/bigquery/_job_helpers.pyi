from google.api_core import retry as retries
from google.cloud.bigquery import job as job
from google.cloud.bigquery import table as table
from google.cloud.bigquery.client import Client as Client
from google.cloud.bigquery.retry import POLLING_DEFAULT_VALUE as POLLING_DEFAULT_VALUE

def make_job_id(job_id: str | None = None, prefix: str | None = None) -> str: ...
def job_config_with_defaults(
    job_config: job.QueryJobConfig | None, default_job_config: job.QueryJobConfig | None
) -> job.QueryJobConfig | None: ...
def query_jobs_insert(
    client: Client,
    query: str,
    job_config: job.QueryJobConfig | None,
    job_id: str | None,
    job_id_prefix: str | None,
    location: str | None,
    project: str,
    retry: retries.Retry | None,
    timeout: float | None,
    job_retry: retries.Retry | None,
) -> job.QueryJob: ...
def query_jobs_query(
    client: Client,
    query: str,
    job_config: job.QueryJobConfig | None,
    location: str | None,
    project: str,
    retry: retries.Retry,
    timeout: float | None,
    job_retry: retries.Retry,
) -> job.QueryJob: ...
def query_and_wait(
    client: Client,
    query: str,
    *,
    job_config: job.QueryJobConfig | None,
    location: str | None,
    project: str,
    api_timeout: float | None = None,
    wait_timeout: float | object | None = ...,
    retry: retries.Retry | None,
    job_retry: retries.Retry | None,
    page_size: int | None = None,
    max_results: int | None = None,
) -> table.RowIterator: ...
