# Nox Sample

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Nox](https://img.shields.io/badge/%F0%9F%A6%8A-Nox-D85E00.svg)](https://github.com/wntrblm/nox)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ntkm61027/nox-sample)

uv で Nox を使用するサンプルです。


## 実行例

### 1. すべてのセッション

```bash
nox
```
💡 実行後に `.nox` を確認すると、各セッション用の仮想環境が作成されている

### 2. セッション指定
- testsセッションのみ実行
  ```bash
  nox -s tests
  ```
- lintセッションのみ実行
  ```bash
  nox -s lint
  ```

### 3. タグ指定
- styleタグのセッションを実行（lint と typecheck）
  ```bash
  nox -t style
  ```
- testタグのセッションを実行（tests のみ）
  ```bash
  nox -t test
  ```

### 4. 複数のPythonバージョンでのテスト

```python
@nox.session(python=["3.11", "3.12", "3.13"], tags=["test"])  # 3.12と3.13を追加
def tests(session):
    ...
```
```bash
nox -s tests
```
  
## cf. noxを使わずに直接コマンドを実行する場合

💡 こちらは uv の仮想環境 `.venv` で実行される

### test
```bash
uv run pytest
```
```bash
# 複数バージョン

# Python 3.11
uv venv --python=3.11
uv pip install -e .
uv run pytest

# Python 3.12
uv venv --python=3.12
uv pip install -e .
uv run pytest

# Python 3.13
uv venv --python=3.13
uv pip install -e .
uv run pytest
```

### lint
```
uv run ruff check .
uv run ruff format .
```

### 型チェック
```bash
uv run mypy src
```