# LLM Wiki Python Port

已将 `src/lib` 下所有 TypeScript 模块映射为 Python 模块（1:1 文件对应）。

## 转换结果

- 每个 `src/lib/*.ts`（非测试文件）都对应到 `python/llm_wiki/lib/*.py`
- 已完成功能级迁移：
  - `detect-language.ts` -> `detect_language.py`
  - `wiki-filename.ts` -> `wiki_filename.py`
- 其余模块已创建 Python scaffold（保留同名导出符号占位，后续逐个补全实现）

详细映射请看：`TS_TO_PYTHON_LIB_MAPPING.md`

## 运行

```bash
cd python
PYTHONPATH=. pytest -q
```
