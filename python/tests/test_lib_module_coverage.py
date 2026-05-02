from __future__ import annotations

from importlib import import_module
from pathlib import Path


def _ts_modules() -> set[str]:
    src = Path(__file__).resolve().parents[2] / "src" / "lib"
    out = set()
    for p in src.glob("*.ts"):
        if ".test." in p.name:
            continue
        out.add(p.stem.replace("-", "_"))
    return out


def _py_modules() -> set[str]:
    pkg = Path(__file__).resolve().parents[1] / "llm_wiki" / "lib"
    return {p.stem for p in pkg.glob("*.py") if p.name != "__init__.py"}


def test_every_typescript_lib_module_has_python_counterpart():
    assert _ts_modules() == _py_modules()


def test_all_generated_modules_are_importable():
    for mod in sorted(_py_modules()):
        import_module(f"llm_wiki.lib.{mod}")
