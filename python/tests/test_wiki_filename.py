from datetime import datetime, timezone

from llm_wiki.wiki_filename import make_query_filename, make_query_slug


def test_slug_keeps_cjk():
    assert make_query_slug("机器学习 入门") == "机器学习-入门"


def test_slug_fallback():
    assert make_query_slug("🎉 !!!") == "query"


def test_filename_shape():
    out = make_query_filename("My Topic", datetime(2026, 4, 23, 14, 30, 52, tzinfo=timezone.utc))
    assert out.file_name == "my-topic-2026-04-23-143052.md"
