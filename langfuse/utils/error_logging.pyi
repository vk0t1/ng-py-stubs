# mypy: ignore-errors

from _typeshed import Incomplete

logger: Incomplete

def catch_and_log_errors(func): ...
def auto_decorate_methods_with(decorator, exclude: list[str] | None = []): ...
