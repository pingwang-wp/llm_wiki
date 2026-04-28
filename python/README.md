# LLM Wiki Python Port (Incremental)

这是一个**增量迁移**版本：先把 TypeScript 仓库中最核心、最易复用的纯逻辑模块迁移到 Python，便于后续把 ingest/search 等能力继续迁移。

## 已迁移模块

- `detect_language`：多语言检测（Unicode 脚本 + 拉丁语系规则）
- `make_query_slug` / `make_query_filename`：wiki 文件名生成策略

## 运行

```bash
cd python
PYTHONPATH=. pytest -q
```

## 说明

原仓库包含 React + Tauri 前端/桌面工程，无法直接“逐行翻译”为 Python。推荐路线：

1. 先迁移 `src/lib` 中纯函数模块（当前已开始）
2. 再迁移 ingest/search/graph 管道到 Python 包
3. 最后根据目标选择：
   - Python CLI（Typer）
   - Python Web UI（FastAPI + 前端）
   - Python 桌面端（PySide6 / Tauri+Python sidecar）
