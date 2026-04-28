from llm_wiki.detect_language import detect_language


def test_detect_japanese_mixed_with_kanji():
    assert detect_language("日本語のテストです。東京") == "Japanese"


def test_detect_chinese():
    assert detect_language("这是一个中文测试") == "Chinese"


def test_detect_turkish_latin_rules():
    assert detect_language("Bu bir Türkçe metindir ve güzel çalışır") == "Turkish"


def test_default_english():
    assert detect_language("This is an English sentence.") == "English"
