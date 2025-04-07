from ...commons.types.usage import Usage as Usage
from .open_ai_usage import OpenAiUsage as OpenAiUsage

IngestionUsage = Usage | OpenAiUsage
