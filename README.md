# bakedanuki-util

`bakedanuki-util` は、Autodesk Maya 用の Python ユーティリティパッケージです。

今後制作予定の `bakedanuki-rig` / `bakedanuki-tool` などから共通利用するための基盤パッケージとして開発しています。

現在は **v1.0.0 未満の開発中 API** です。将来の設計と使いやすさを優先し、
互換性維持よりも改善を選んで、必要な破壊的変更を積極的に行います。
安定した API 互換性の提供は v1.0.0 以降を対象とします。

## Installation

`bakedanuki-util` は、Maya 2025 以降を対象とした Maya Module 形式の配布構成です。

`bakedanuki/modules` を `MAYA_MODULE_PATH` に追加すると、Maya が `modules/bd_util.mod` を読み込み、`bakedanuki-util/python` を Python path に追加します。`bakedanuki-util/python` を直接環境変数へ追加する必要はありません。

導入方法は、利用目的に合わせて次の3つから選べます。

### 1. installer.py

個人環境へ継続的に導入する場合は、[bakedanuki/installer.py](bakedanuki/installer.py) を使用する方法が最も簡単です。

1. 使用するバージョンの Maya を起動します。
2. `installer.py` を Maya のビューポートへドラッグ&ドロップします。
3. 確認ダイアログの内容を確認し、`OK` を選びます。
4. Maya を再起動します。

現在起動している Maya バージョン用の `Maya.env` に、`bakedanuki/modules` が `MAYA_MODULE_PATH` として登録されます。同じパスは重複して追加されず、既に別の bakedanuki パスが登録されている場合は置き換え確認が表示されます。

### 2. Maya Launcher

`Maya.env` を変更せずに試す場合は、使用する Maya バージョンに対応する起動バッチを実行します。

- [maya2025.bat](bakedanuki/launchers/maya2025.bat)
- [maya2026.bat](bakedanuki/launchers/maya2026.bat)
- [maya2027.bat](bakedanuki/launchers/maya2027.bat)

起動した Maya のプロセスにだけ `bakedanuki/modules` が追加されるため、ユーザー環境の `Maya.env` は変更されません。Maya のインストール先が標準と異なる場合は、起動バッチ内の `MAYA_EXE` を環境に合わせて変更してください。

### 3. Existing Maya Launcher

スタジオなどで既存の Maya 起動バッチを管理している場合は、Maya を起動する処理より前に次の設定を追加してください。

```bat
set "MAYA_MODULE_PATH=D:/path/to/bakedanuki/modules;%MAYA_MODULE_PATH%"
```

`D:/path/to/bakedanuki/modules` は、実際に配置した `bakedanuki/modules` の絶対パスへ置き換えます。この方法では各ユーザーの `Maya.env` を変更せず、起動バッチ側で使用するパッケージの配置先を一元管理できます。

### Check

導入後に Maya の Script Editor で次を実行します。

```python
import bd_util

print(bd_util.__file__)
```

`bakedanuki/bakedanuki-util/python/bd_util/__init__.py` が表示されれば導入できています。

## Development

VS Code / Pylance で開発する場合は、使用する Maya バージョンの
`mayapy.exe` を Python interpreter に選択してください。

Maya API の型スタブは `typings/maya` に同梱しています。
リポジトリ直下の `pyrightconfig.json` が自動的に参照するため、
クローン後に `maya-stubs` を別途インストールする必要はありません。

Pyright の型・補完 contract と pytest の実行方法は、
[testing.md](bakedanuki/bakedanuki-util/docs/maya/node_operator/testing.md) を参照してください。

### Maya C++ Plug-ins

C++ source は配布用 `bakedanuki` フォルダへ含めず、リポジトリ直下の
`native/maya` で管理します。Maya 2025 向けの build と test は次のコマンドです。

```powershell
.\scripts\build-native-maya2025.cmd
.\scripts\test-native-maya2025.cmd
```

必要な toolchain、成果物の配置、node ID の管理方針は
[native/maya/README.md](native/maya/README.md) を参照してください。

### Formatting

PythonコードはBlack 26.5.1で整形します。初回だけformat専用環境を作成してください。
この環境はMaya実行用のPython interpreterとは分離されています。

```powershell
.\scripts\setup-format.cmd
```

リポジトリのPythonコードを一括整形する場合と、差分を発生させず確認する場合は
次のコマンドを使用します。

```powershell
.\scripts\format.cmd
.\scripts\format.cmd -Check
.\scripts\format.cmd -Check -Diff
```

VS CodeのBlack Formatterも同じformat専用環境と`pyproject.toml`を参照します。
Generatorを実行した後は、生成差分を確認する前に`format.cmd`を実行してください。
外部由来のMaya API stubを置く`typings`は一括整形の対象外です。

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
- [AGENTS.md](AGENTS.md)
  - 開発者および AI Agent 向けの開発環境、テスト手順、作業方針です。

## Distribution Layout

配布時は、複数の bakedanuki 系パッケージの `bakedanuki` フォルダを同じ場所へまとめる想定です。

```text
bakedanuki/
  installer.py
  launchers/
    maya2025.bat
    maya2026.bat
    maya2027.bat
  modules/
    bd_util.mod

  bakedanuki-util/
    README.md
    LICENSE
    THIRD_PARTY_NOTICES.md
    docs/
    licenses/
    plug-ins/
      maya2025/
        bdUtilNodes.mll
    python/
      bd_util/
```

`bakedanuki/modules` を `MAYA_MODULE_PATH` に追加すると、`modules/bd_util.mod` 経由で `bakedanuki-util/python` が Maya の Python path に追加されます。

## License

MIT License

`bdUtilNodes.mll` が使用する第三者ライブラリについては
[THIRD_PARTY_NOTICES.md](bakedanuki/bakedanuki-util/THIRD_PARTY_NOTICES.md)
を参照してください。
