import typing

FileContent = typing.IO[bytes] | bytes | str
File = FileContent | tuple[str | None, FileContent] | tuple[str | None, FileContent, str | None] | tuple[str | None, FileContent, str | None, typing.Mapping[str, str]]

def convert_file_dict_to_httpx_tuples(d: dict[str, File | list[File]]) -> list[tuple[str, File]]: ...
