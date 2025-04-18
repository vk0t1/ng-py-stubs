from google.cloud.bigquery import QueryJob as QueryJob
from google.cloud.bigquery.table import RowIterator as RowIterator

def get_progress_bar(progress_bar_type, description, total, unit): ...
def wait_for_query(
    query_job: QueryJob, progress_bar_type: str | None = None, max_results: int | None = None
) -> RowIterator: ...
