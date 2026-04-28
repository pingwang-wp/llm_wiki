"""Python port of core llm_wiki utilities."""

from .detect_language import detect_language
from .wiki_filename import make_query_slug, make_query_filename

__all__ = [
    "detect_language",
    "make_query_slug",
    "make_query_filename",
]
