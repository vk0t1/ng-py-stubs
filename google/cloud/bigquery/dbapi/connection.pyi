from _typeshed import Incomplete
from google.cloud import bigquery as bigquery
from google.cloud.bigquery.dbapi import cursor as cursor

class Connection:
    def __init__(
        self,
        client: Incomplete | None = None,
        bqstorage_client: Incomplete | None = None,
        prefer_bqstorage_client: bool = True,
    ) -> None: ...
    def close(self) -> None: ...
    def commit(self) -> None: ...
    def cursor(self): ...

def connect(
    client: Incomplete | None = None, bqstorage_client: Incomplete | None = None, prefer_bqstorage_client: bool = True
): ...
