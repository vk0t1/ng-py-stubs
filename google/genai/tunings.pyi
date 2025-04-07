from _typeshed import Incomplete

from . import _api_module
from . import types as types
from ._api_client import BaseApiClient as BaseApiClient
from .pagers import AsyncPager as AsyncPager
from .pagers import Pager as Pager

logger: Incomplete

class Tunings(_api_module.BaseModule):
    def list(self, *, config: types.ListTuningJobsConfigOrDict | None = None) -> Pager[types.TuningJob]: ...
    def get(self, *, name: str, config: types.GetTuningJobConfigOrDict | None = None) -> types.TuningJob: ...
    def tune(
        self,
        *,
        base_model: str,
        training_dataset: types.TuningDatasetOrDict,
        config: types.CreateTuningJobConfigOrDict | None = None,
    ) -> types.TuningJob: ...

class AsyncTunings(_api_module.BaseModule):
    async def list(self, *, config: types.ListTuningJobsConfigOrDict | None = None) -> AsyncPager[types.TuningJob]: ...
    async def get(self, *, name: str, config: types.GetTuningJobConfigOrDict | None = None) -> types.TuningJob: ...
    async def tune(
        self,
        *,
        base_model: str,
        training_dataset: types.TuningDatasetOrDict,
        config: types.CreateTuningJobConfigOrDict | None = None,
    ) -> types.TuningJob: ...

class _IpythonUtils:
    displayed_experiments: set[str]
    @staticmethod
    def is_ipython_available() -> bool: ...
    @staticmethod
    def display_experiment_button(experiment: str, project: str) -> None: ...
    @staticmethod
    def display_model_tuning_button(tuning_job_resource: str) -> None: ...
