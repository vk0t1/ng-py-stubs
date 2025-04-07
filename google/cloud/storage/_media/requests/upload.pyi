from _typeshed import Incomplete
from google.cloud.storage._media import _upload
from google.cloud.storage._media.requests import _request_helpers

class SimpleUpload(_request_helpers.RequestsMixin, _upload.SimpleUpload):
    def transmit(self, transport, data, content_type, timeout=...): ...

class MultipartUpload(_request_helpers.RequestsMixin, _upload.MultipartUpload):
    def transmit(self, transport, data, metadata, content_type, timeout=...): ...

class ResumableUpload(_request_helpers.RequestsMixin, _upload.ResumableUpload):
    def initiate(
        self,
        transport,
        stream,
        metadata,
        content_type,
        total_bytes: Incomplete | None = None,
        stream_final: bool = True,
        timeout=...,
    ): ...
    def transmit_next_chunk(self, transport, timeout=...): ...
    def recover(self, transport): ...

class XMLMPUContainer(_request_helpers.RequestsMixin, _upload.XMLMPUContainer):
    def initiate(self, transport, content_type, timeout=...): ...
    def finalize(self, transport, timeout=...): ...
    def cancel(self, transport, timeout=...): ...

class XMLMPUPart(_request_helpers.RequestsMixin, _upload.XMLMPUPart):
    def upload(self, transport, timeout=...): ...
