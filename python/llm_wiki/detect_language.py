"""Language detection ported from src/lib/detect-language.ts."""

from __future__ import annotations

import re
from collections import defaultdict


_LATIN_RULES: list[tuple[str, re.Pattern[str], re.Pattern[str] | None]] = [
    ("Vietnamese", re.compile(r"[ảạắằẳẵặấầẩẫậđẻẽẹếềểễệỉĩịỏọốồổỗộơớờởỡợủũụưứừửữựỷỹỵ]"), None),
    ("Turkish", re.compile(r"[ğış]"), re.compile(r"\b(bir|ve|için|ile|bu|da|de|değil|ama)\b")),
    ("Polish", re.compile(r"[ąćęłńóśźż]"), None),
    ("Czech", re.compile(r"[ěšžřďťňů]"), None),
    ("Romanian", re.compile(r"[ăâîșț]"), re.compile(r"\b(și|este|sau|care|pentru)\b")),
    ("Hungarian", re.compile(r"[őű]"), None),
]


def detect_language(text: str) -> str:
    counts: dict[str, int] = defaultdict(int)
    for ch in text:
        cp = ord(ch)
        if cp < 0x80:
            continue
        script = _get_script(cp)
        if script:
            counts[script] += 1

    if counts.get("Japanese", 0) > 0 and counts.get("Chinese", 0) > 0:
        return "Japanese"

    if counts:
        max_script, max_count = max(counts.items(), key=lambda x: x[1])
        if max_count >= 2:
            return max_script

    latin = _detect_latin_language(text)
    return latin if latin else "English"


def _in(cp: int, a: int, b: int) -> bool:
    return a <= cp <= b


def _get_script(cp: int) -> str | None:
    if _in(cp, 0x4E00, 0x9FFF) or _in(cp, 0x3400, 0x4DBF) or _in(cp, 0x20000, 0x2A6DF) or _in(cp, 0xF900, 0xFAFF):
        return "Chinese"
    if _in(cp, 0x3040, 0x309F) or _in(cp, 0x30A0, 0x30FF) or _in(cp, 0x31F0, 0x31FF) or _in(cp, 0xFF65, 0xFF9F):
        return "Japanese"
    if _in(cp, 0xAC00, 0xD7AF) or _in(cp, 0x1100, 0x11FF) or _in(cp, 0x3130, 0x318F):
        return "Korean"
    if _in(cp, 0x0600, 0x06FF) or _in(cp, 0x0750, 0x077F) or _in(cp, 0x08A0, 0x08FF) or _in(cp, 0xFB50, 0xFDFF) or _in(cp, 0xFE70, 0xFEFF):
        return "Arabic"
    if _in(cp, 0x0590, 0x05FF) or _in(cp, 0xFB1D, 0xFB4F):
        return "Hebrew"
    if _in(cp, 0x0E00, 0x0E7F):
        return "Thai"
    if _in(cp, 0x0900, 0x097F):
        return "Hindi"
    if _in(cp, 0x0980, 0x09FF):
        return "Bengali"
    if _in(cp, 0x0B80, 0x0BFF):
        return "Tamil"
    if _in(cp, 0x0C00, 0x0C7F):
        return "Telugu"
    if _in(cp, 0x0C80, 0x0CFF):
        return "Kannada"
    if _in(cp, 0x0D00, 0x0D7F):
        return "Malayalam"
    if _in(cp, 0x0A80, 0x0AFF):
        return "Gujarati"
    if _in(cp, 0x0A00, 0x0A7F):
        return "Punjabi"
    if _in(cp, 0x1000, 0x109F):
        return "Burmese"
    if _in(cp, 0x1780, 0x17FF):
        return "Khmer"
    if _in(cp, 0x0E80, 0x0EFF):
        return "Lao"
    if _in(cp, 0x10A0, 0x10FF) or _in(cp, 0x2D00, 0x2D2F):
        return "Georgian"
    if _in(cp, 0x0530, 0x058F):
        return "Armenian"
    if _in(cp, 0x1200, 0x137F):
        return "Amharic"
    if _in(cp, 0x0F00, 0x0FFF):
        return "Tibetan"
    if _in(cp, 0x0D80, 0x0DFF):
        return "Sinhala"
    if _in(cp, 0x0400, 0x04FF) or _in(cp, 0x0500, 0x052F):
        return "Russian"
    if _in(cp, 0x0370, 0x03FF) or _in(cp, 0x1F00, 0x1FFF):
        return "Greek"
    return None


def _detect_latin_language(text: str) -> str | None:
    lower = text.lower()

    for lang, chars, words in _LATIN_RULES:
        if chars.search(lower) and (words is None or words.search(lower)):
            return lang

    if re.search(r"[äöüß]", lower) or re.search(r"\b(und|der|die|das|ist|nicht|ein|eine)\b", lower):
        if re.search(r"\b(und|der|die|das|ist)\b", lower):
            return "German"

    if re.search(r"[àâçéèêëïîôùûüÿœæ]", lower) or re.search(r"\b(le|la|les|de|des|est|et|un|une|du|au)\b", lower):
        if re.search(r"\b(le|la|les|est|une|des)\b", lower):
            return "French"

    if re.search(r"[ãõç]", lower) and re.search(r"\b(o|a|os|as|de|do|da|é|em|um|uma|não|que)\b", lower):
        return "Portuguese"

    if re.search(r"[áéíóúñ¿¡]", lower) or re.search(r"\b(el|la|los|las|de|del|es|en|por|que|un|una)\b", lower):
        if re.search(r"\b(el|los|las|del|por)\b", lower) or re.search(r"[ñ¿¡]", lower):
            return "Spanish"

    return None
