class AvroOptions:
    def __init__(self) -> None: ...
    @property
    def use_avro_logical_types(self) -> bool | None: ...
    @use_avro_logical_types.setter
    def use_avro_logical_types(self, value) -> None: ...
    @classmethod
    def from_api_repr(cls, resource: dict[str, bool]) -> AvroOptions: ...
    def to_api_repr(self) -> dict: ...

class ParquetOptions:
    def __init__(self) -> None: ...
    @property
    def enum_as_string(self) -> bool: ...
    @enum_as_string.setter
    def enum_as_string(self, value: bool) -> None: ...
    @property
    def enable_list_inference(self) -> bool: ...
    @enable_list_inference.setter
    def enable_list_inference(self, value: bool) -> None: ...
    @property
    def map_target_type(self) -> bool | str | None: ...
    @map_target_type.setter
    def map_target_type(self, value: str) -> None: ...
    @classmethod
    def from_api_repr(cls, resource: dict[str, bool]) -> ParquetOptions: ...
    def to_api_repr(self) -> dict: ...
