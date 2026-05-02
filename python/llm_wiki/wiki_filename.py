"""Filename generation for user-initiated wiki writes."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import re
import unicodedata


@dataclass(frozen=True)
class QueryFilename:
    slug: str
    file_name: str
    date: str
    time: str


def make_query_slug(title: str) -> str:
    normalized = unicodedata.normalize("NFKC", title).strip()
    hyphenated = re.sub(r"\s+", "-", normalized)

    kept = "".join(ch for ch in hyphenated if ch == "-" or ch.isalnum())
    kept = re.sub(r"-+", "-", kept).strip("-").lower()[:50]
    return kept if kept else "query"


def make_query_filename(title: str, now: datetime | None = None) -> QueryFilename:
    slug = make_query_slug(title)
    now = now or datetime.now(timezone.utc)
    now_utc = now.astimezone(timezone.utc)
    date = now_utc.strftime("%Y-%m-%d")
    time = now_utc.strftime("%H%M%S")
    return QueryFilename(
        slug=slug,
        date=date,
        time=time,
        file_name=f"{slug}-{date}-{time}.md",
    )
