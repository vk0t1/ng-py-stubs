from . import EMPTY_RECT as EMPTY_RECT, Matrix as Matrix, Point as Point, Rect as Rect, TEXTFLAGS_TEXT as TEXTFLAGS_TEXT, TOOLS as TOOLS, message as message, sRGB_to_pdf as sRGB_to_pdf
from _typeshed import Incomplete
from collections.abc import Generator
from dataclasses import dataclass

EDGES: Incomplete
CHARS: Incomplete
TEXTPAGE: Incomplete
white_spaces: Incomplete

class UnsetFloat(float): ...

NON_NEGATIVE_SETTINGS: Incomplete
TABLE_STRATEGIES: Incomplete
UNSET: Incomplete
DEFAULT_SNAP_TOLERANCE: int
DEFAULT_JOIN_TOLERANCE: int
DEFAULT_MIN_WORDS_VERTICAL: int
DEFAULT_MIN_WORDS_HORIZONTAL: int
DEFAULT_X_TOLERANCE: int
DEFAULT_Y_TOLERANCE: int
DEFAULT_X_DENSITY: float
DEFAULT_Y_DENSITY: int
bbox_getter: Incomplete
LIGATURES: Incomplete

def to_list(collection) -> list: ...

class TextMap:
    tuples: Incomplete
    as_string: Incomplete
    def __init__(self, tuples: Incomplete | None = None) -> None: ...
    def match_to_dict(self, m, main_group: int = 0, return_groups: bool = True, return_chars: bool = True) -> dict: ...

class WordMap:
    tuples: Incomplete
    def __init__(self, tuples) -> None: ...
    def to_textmap(self, layout: bool = False, layout_width: int = 0, layout_height: int = 0, layout_width_chars: int = 0, layout_height_chars: int = 0, x_density=..., y_density=..., x_shift: int = 0, y_shift: int = 0, y_tolerance=..., use_text_flow: bool = False, presorted: bool = False, expand_ligatures: bool = True) -> TextMap: ...

class WordExtractor:
    x_tolerance: Incomplete
    y_tolerance: Incomplete
    keep_blank_chars: Incomplete
    use_text_flow: Incomplete
    horizontal_ltr: Incomplete
    vertical_ttb: Incomplete
    extra_attrs: Incomplete
    split_at_punctuation: Incomplete
    expansions: Incomplete
    def __init__(self, x_tolerance=..., y_tolerance=..., keep_blank_chars: bool = False, use_text_flow: bool = False, horizontal_ltr: bool = True, vertical_ttb: bool = False, extra_attrs: Incomplete | None = None, split_at_punctuation: bool = False, expand_ligatures: bool = True) -> None: ...
    def merge_chars(self, ordered_chars: list): ...
    def char_begins_new_word(self, prev_char, curr_char) -> bool: ...
    def iter_chars_to_words(self, ordered_chars) -> Generator[Incomplete, Incomplete]: ...
    def iter_sort_chars(self, chars) -> Generator[Incomplete, Incomplete, Incomplete]: ...
    def iter_extract_tuples(self, chars) -> Generator[Incomplete]: ...
    def extract_wordmap(self, chars) -> WordMap: ...
    def extract_words(self, chars: list) -> list: ...

def extract_words(chars: list, **kwargs) -> list: ...

TEXTMAP_KWARGS: Incomplete
WORD_EXTRACTOR_KWARGS: Incomplete

def chars_to_textmap(chars: list, **kwargs) -> TextMap: ...
def extract_text(chars: list, **kwargs) -> str: ...
def collate_line(line_chars: list, tolerance=...) -> str: ...
def dedupe_chars(chars: list, tolerance: int = 1) -> list: ...
def line_to_edge(line): ...
def rect_to_edges(rect) -> list: ...
def curve_to_edges(curve) -> list: ...
def obj_to_edges(obj) -> list: ...
def filter_edges(edges, orientation: Incomplete | None = None, edge_type: Incomplete | None = None, min_length: int = 1) -> list: ...
def cluster_list(xs, tolerance: int = 0) -> list: ...
def make_cluster_dict(values, tolerance) -> dict: ...
def cluster_objects(xs, key_fn, tolerance) -> list: ...
def move_object(obj, axis: str, value): ...
def snap_objects(objs, attr: str, tolerance) -> list: ...
def snap_edges(edges, x_tolerance=..., y_tolerance=...): ...
def resize_object(obj, key: str, value): ...
def join_edge_group(edges, orientation: str, tolerance=...): ...
def merge_edges(edges, snap_x_tolerance, snap_y_tolerance, join_x_tolerance, join_y_tolerance): ...
def bbox_to_rect(bbox) -> dict: ...
def objects_to_rect(objects) -> dict: ...
def merge_bboxes(bboxes): ...
def objects_to_bbox(objects): ...
def words_to_edges_h(words, word_threshold: int = ...): ...
def get_bbox_overlap(a, b): ...
def words_to_edges_v(words, word_threshold: int = ...): ...
def edges_to_intersections(edges, x_tolerance: int = 1, y_tolerance: int = 1) -> dict: ...
def obj_to_bbox(obj): ...
def intersections_to_cells(intersections): ...
def cells_to_tables(page, cells) -> list: ...

class CellGroup:
    cells: Incomplete
    bbox: Incomplete
    def __init__(self, cells) -> None: ...

class TableRow(CellGroup): ...

class TableHeader:
    bbox: Incomplete
    cells: Incomplete
    names: Incomplete
    external: Incomplete
    def __init__(self, bbox, cells, names, above) -> None: ...

class Table:
    page: Incomplete
    cells: Incomplete
    header: Incomplete
    def __init__(self, page, cells) -> None: ...
    @property
    def bbox(self): ...
    @property
    def rows(self) -> list: ...
    @property
    def row_count(self) -> int: ...
    @property
    def col_count(self) -> int: ...
    def extract(self, **kwargs) -> list: ...
    def to_markdown(self, clean: bool = True): ...
    def to_pandas(self, **kwargs): ...

@dataclass
class TableSettings:
    vertical_strategy: str = ...
    horizontal_strategy: str = ...
    explicit_vertical_lines: list = ...
    explicit_horizontal_lines: list = ...
    snap_tolerance: float = ...
    snap_x_tolerance: float = ...
    snap_y_tolerance: float = ...
    join_tolerance: float = ...
    join_x_tolerance: float = ...
    join_y_tolerance: float = ...
    edge_min_length: float = ...
    min_words_vertical: float = ...
    min_words_horizontal: float = ...
    intersection_tolerance: float = ...
    intersection_x_tolerance: float = ...
    intersection_y_tolerance: float = ...
    text_settings: dict = ...
    def __post_init__(self) -> TableSettings: ...
    @classmethod
    def resolve(cls, settings: Incomplete | None = None): ...

class TableFinder:
    page: Incomplete
    settings: Incomplete
    edges: Incomplete
    intersections: Incomplete
    cells: Incomplete
    tables: Incomplete
    def __init__(self, page, settings: Incomplete | None = None) -> None: ...
    def get_edges(self) -> list: ...
    def __getitem__(self, i): ...

def make_chars(page, clip: Incomplete | None = None): ...
def make_edges(page, clip: Incomplete | None = None, tset: Incomplete | None = None, add_lines: Incomplete | None = None): ...
def page_rotation_set0(page): ...
def page_rotation_reset(page, xref, rot, mediabox): ...
def find_tables(page, clip: Incomplete | None = None, vertical_strategy: str = 'lines', horizontal_strategy: str = 'lines', vertical_lines: list = None, horizontal_lines: list = None, snap_tolerance: float = ..., snap_x_tolerance: float = None, snap_y_tolerance: float = None, join_tolerance: float = ..., join_x_tolerance: float = None, join_y_tolerance: float = None, edge_min_length: float = 3, min_words_vertical: float = ..., min_words_horizontal: float = ..., intersection_tolerance: float = 3, intersection_x_tolerance: float = None, intersection_y_tolerance: float = None, text_tolerance: int = 3, text_x_tolerance: int = 3, text_y_tolerance: int = 3, strategy: Incomplete | None = None, add_lines: Incomplete | None = None): ...
