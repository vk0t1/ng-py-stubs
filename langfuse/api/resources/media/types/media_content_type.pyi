import enum
import typing

T_Result = typing.TypeVar('T_Result')

class MediaContentType(str, enum.Enum):
    IMAGE_PNG = 'image/png'
    IMAGE_JPEG = 'image/jpeg'
    IMAGE_JPG = 'image/jpg'
    IMAGE_WEBP = 'image/webp'
    IMAGE_GIF = 'image/gif'
    IMAGE_SVG_XML = 'image/svg+xml'
    IMAGE_TIFF = 'image/tiff'
    IMAGE_BMP = 'image/bmp'
    AUDIO_MPEG = 'audio/mpeg'
    AUDIO_MP_3 = 'audio/mp3'
    AUDIO_WAV = 'audio/wav'
    AUDIO_OGG = 'audio/ogg'
    AUDIO_OGA = 'audio/oga'
    AUDIO_AAC = 'audio/aac'
    AUDIO_MP_4 = 'audio/mp4'
    AUDIO_FLAC = 'audio/flac'
    VIDEO_MP_4 = 'video/mp4'
    VIDEO_WEBM = 'video/webm'
    TEXT_PLAIN = 'text/plain'
    TEXT_HTML = 'text/html'
    TEXT_CSS = 'text/css'
    TEXT_CSV = 'text/csv'
    APPLICATION_PDF = 'application/pdf'
    APPLICATION_MSWORD = 'application/msword'
    APPLICATION_MS_EXCEL = 'application/vnd.ms-excel'
    APPLICATION_ZIP = 'application/zip'
    APPLICATION_JSON = 'application/json'
    APPLICATION_XML = 'application/xml'
    APPLICATION_OCTET_STREAM = 'application/octet-stream'
    def visit(self, image_png: typing.Callable[[], T_Result], image_jpeg: typing.Callable[[], T_Result], image_jpg: typing.Callable[[], T_Result], image_webp: typing.Callable[[], T_Result], image_gif: typing.Callable[[], T_Result], image_svg_xml: typing.Callable[[], T_Result], image_tiff: typing.Callable[[], T_Result], image_bmp: typing.Callable[[], T_Result], audio_mpeg: typing.Callable[[], T_Result], audio_mp_3: typing.Callable[[], T_Result], audio_wav: typing.Callable[[], T_Result], audio_ogg: typing.Callable[[], T_Result], audio_oga: typing.Callable[[], T_Result], audio_aac: typing.Callable[[], T_Result], audio_mp_4: typing.Callable[[], T_Result], audio_flac: typing.Callable[[], T_Result], video_mp_4: typing.Callable[[], T_Result], video_webm: typing.Callable[[], T_Result], text_plain: typing.Callable[[], T_Result], text_html: typing.Callable[[], T_Result], text_css: typing.Callable[[], T_Result], text_csv: typing.Callable[[], T_Result], application_pdf: typing.Callable[[], T_Result], application_msword: typing.Callable[[], T_Result], application_ms_excel: typing.Callable[[], T_Result], application_zip: typing.Callable[[], T_Result], application_json: typing.Callable[[], T_Result], application_xml: typing.Callable[[], T_Result], application_octet_stream: typing.Callable[[], T_Result]) -> T_Result: ...
