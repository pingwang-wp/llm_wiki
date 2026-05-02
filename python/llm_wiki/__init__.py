"""Python port of core llm_wiki utilities."""

from .detect_language import detect_language
from .wiki_filename import QueryFilename, make_query_filename, make_query_slug
from . import lib

__all__ = [
    "detect_language",
    "QueryFilename",
    "make_query_slug",
    "make_query_filename",
    "lib",
]
