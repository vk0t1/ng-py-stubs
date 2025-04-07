import enum

class AutoRowIDs(enum.Enum):
    DISABLED = ...
    GENERATE_UUID = ...

class Compression(str, enum.Enum):
    GZIP = 'GZIP'
    DEFLATE = 'DEFLATE'
    SNAPPY = 'SNAPPY'
    ZSTD = 'ZSTD'
    NONE = 'NONE'

class DecimalTargetType:
    NUMERIC: str
    BIGNUMERIC: str
    STRING: str

class CreateDisposition:
    CREATE_IF_NEEDED: str
    CREATE_NEVER: str

class DefaultPandasDTypes(enum.Enum):
    BOOL_DTYPE = ...
    INT_DTYPE = ...
    DATE_DTYPE = ...
    TIME_DTYPE = ...
    RANGE_DATE_DTYPE = ...
    RANGE_DATETIME_DTYPE = ...
    RANGE_TIMESTAMP_DTYPE = ...

class DestinationFormat:
    CSV: str
    NEWLINE_DELIMITED_JSON: str
    AVRO: str
    PARQUET: str

class Encoding:
    UTF_8: str
    ISO_8859_1: str

class QueryPriority:
    INTERACTIVE: str
    BATCH: str

class QueryApiMethod(str, enum.Enum):
    INSERT = 'INSERT'
    QUERY = 'QUERY'

class SchemaUpdateOption:
    ALLOW_FIELD_ADDITION: str
    ALLOW_FIELD_RELAXATION: str

class SourceFormat:
    CSV: str
    DATASTORE_BACKUP: str
    NEWLINE_DELIMITED_JSON: str
    AVRO: str
    PARQUET: str
    ORC: str

class KeyResultStatementKind:
    KEY_RESULT_STATEMENT_KIND_UNSPECIFIED: str
    LAST: str
    FIRST_SELECT: str

class StandardSqlTypeNames(str, enum.Enum):
    TYPE_KIND_UNSPECIFIED = ...
    INT64 = ...
    BOOL = ...
    FLOAT64 = ...
    STRING = ...
    BYTES = ...
    TIMESTAMP = ...
    DATE = ...
    TIME = ...
    DATETIME = ...
    INTERVAL = ...
    GEOGRAPHY = ...
    NUMERIC = ...
    BIGNUMERIC = ...
    JSON = ...
    ARRAY = ...
    STRUCT = ...
    RANGE = ...
    FOREIGN = ...

class EntityTypes(str, enum.Enum):
    USER_BY_EMAIL = 'userByEmail'
    GROUP_BY_EMAIL = 'groupByEmail'
    DOMAIN = 'domain'
    DATASET = 'dataset'
    SPECIAL_GROUP = 'specialGroup'
    VIEW = 'view'
    IAM_MEMBER = 'iamMember'
    ROUTINE = 'routine'

class SqlTypeNames(str, enum.Enum):
    STRING = 'STRING'
    BYTES = 'BYTES'
    INTEGER = 'INTEGER'
    INT64 = 'INTEGER'
    FLOAT = 'FLOAT'
    FLOAT64 = 'FLOAT'
    DECIMAL = 'NUMERIC'
    NUMERIC = 'NUMERIC'
    BIGDECIMAL = 'BIGNUMERIC'
    BIGNUMERIC = 'BIGNUMERIC'
    BOOLEAN = 'BOOLEAN'
    BOOL = 'BOOLEAN'
    GEOGRAPHY = 'GEOGRAPHY'
    RECORD = 'RECORD'
    STRUCT = 'RECORD'
    TIMESTAMP = 'TIMESTAMP'
    DATE = 'DATE'
    TIME = 'TIME'
    DATETIME = 'DATETIME'
    INTERVAL = 'INTERVAL'
    RANGE = 'RANGE'
    FOREIGN = 'FOREIGN'

class WriteDisposition:
    WRITE_APPEND: str
    WRITE_TRUNCATE: str
    WRITE_EMPTY: str

class DeterminismLevel:
    DETERMINISM_LEVEL_UNSPECIFIED: str
    DETERMINISTIC: str
    NOT_DETERMINISTIC: str

class RoundingMode(str, enum.Enum):
    ROUNDING_MODE_UNSPECIFIED = ...
    ROUND_HALF_AWAY_FROM_ZERO = ...
    ROUND_HALF_EVEN = ...
