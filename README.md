# bakedanuki-util

`bakedanuki-util` は、Autodesk Maya 用の Python ユーティリティパッケージです。

今後制作予定の `bakedanuki-rig` / `bakedanuki-tool` などから共通利用するための基盤パッケージとして開発しています。

現在は **v1.0.0 未満の開発中 API** です。破壊的変更が入る可能性があります。

## Repository Entry Points

このリポジトリでは、開発リポジトリとしての入口と、配布用 `bakedanuki` フォルダとしての入口を分けています。

- [bakedanuki/README.md](bakedanuki/README.md)
  - Maya Module 配布フォルダ全体の説明です。
  - `MAYA_MODULE_PATH` の通し方、複数 bakedanuki 系パッケージをまとめる構成を説明しています。
- [bakedanuki/bakedanuki-util/README.md](bakedanuki/bakedanuki-util/README.md)
  - `bakedanuki-util` パッケージ本体の説明です。
  - 利用例、導入手順、詳細ドキュメントへのリンクを置いています。
- [bakedanuki/bakedanuki-util/docs/](bakedanuki/bakedanuki-util/docs/)
  - `NodeOperator` などの設計メモです。

## Distribution Layout

配布時は、複数の bakedanuki 系パッケージの `bakedanuki` フォルダを同じ場所へまとめる想定です。

```text
bakedanuki/
  installer.py
  Maya.env
  launchers/
    maya2025.bat
    maya2026.bat
    maya2027.bat
  modules/
    bd_util.mod

  bakedanuki-util/
    README.md
    LICENSE
    docs/
    python/
      bd_util/
```

`bakedanuki/modules` を `MAYA_MODULE_PATH` に追加すると、`modules/bd_util.mod` 経由で `bakedanuki-util/python` が Maya の Python path に追加されます。

## Development Setup

通常の Python では Maya API が import できないため、検証は `mayapy` で行います。

```powershell
$pytestTarget = Join-Path $env:TEMP 'codex-mayapy-pytest'
$pythonPath = Resolve-Path .\bakedanuki\bakedanuki-util\python
$env:PYTHONPATH = "$pytestTarget;$pythonPath"
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pytest tests
```

`pytest` が Maya Python から見えない場合は、先に一時ディレクトリへ追加します。

```powershell
& "C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" -m pip install --target $env:TEMP\codex-mayapy-pytest pytest
```

## License

MIT License
