# bakedanuki

このフォルダは、bakedanuki 系パッケージを Maya Module としてまとめて配置するための親フォルダです。

`bakedanuki-util`、`bakedanuki-tools`、今後追加予定の `bakedanuki-rig` などは、各パッケージの `bakedanuki` フォルダを同じ場所へ重ねて配置する想定です。

## Layout

```text
bakedanuki/
  installer.py
  uninstaller.py
  launchers/
    maya2025.bat
    maya2026.bat
    maya2027.bat
  modules/
    bd_util.mod
    bd_tools.mod

  bakedanuki-util/
    README.md
    LICENSE
    docs/
    plug-ins/
      maya2025/
        bdUtilNodes.mll
      maya2026/
        bdUtilNodes.mll
      maya2027/
        bdUtilNodes.mll
    python/

  bakedanuki-tools/
    README.md
    LICENSE
    docs/
    python/
    scripts/
```

将来`bakedanuki-rig`を同梱する場合は、同じrootにpackageフォルダと
`modules/bd_rig.mod`を重ねます。

Maya には `bakedanuki/modules` だけを `MAYA_MODULE_PATH` として追加します。

各 `.mod` ファイルが、それぞれのパッケージフォルダ内にある `python`、
Maya version 別の `plug-ins` などを Maya へ追加します。

## Setup With installer.py

最も簡単な導入方法は、[installer.py](installer.py) を Maya のビューポートへドラッグ&ドロップする方法です。

`installer.py` は、自分自身と同じ階層にある `modules` フォルダを検出し、現在起動している Maya が読む `Maya.env` に `MAYA_MODULE_PATH` を追加します。`MAYA_ENV_DIR` が指定されていればそのフォルダを優先し、それ以外ではバージョン別、共通の順に既存ファイルを探します。

追加前には確認ダイアログが表示され、`OK` を選んだ場合だけ `Maya.env` を更新します。`Cancel` を選んだ場合は何も変更しません。`Maya.env` が存在しない場合は新しく作成します。

同じ modules パスが既に登録されている場合は重複して追加しません。パスの大文字・小文字、区切り文字の `\` / `/`、末尾の区切り文字の違いも同じパスとして扱います。

`bakedanuki`メニューの「Maya 起動時に bakedanuki メニューを表示」をOFFにした場合は、次回起動から
メニューを自動表示しません。再び`installer.py`をドロップすると、modulesパスが
登録済みでも確認後に表示設定をONへ戻します。現在のMayaバージョンの設定だけを変更し、
反映にはMayaの再起動が必要です。OFFでもModuleの登録やツールの直接起動は維持されます。
表示設定は現在のMayaバージョンの`prefs/bakedanuki/menu.json`に保存します。
この操作でMayaの一般設定やShelfを明示的に保存することはありません。

別の bakedanuki フォルダを指すパスが登録されている場合は、置き換え確認のダイアログが表示されます。置き換え時も、bakedanuki 以外の module パスはそのまま維持されます。

installerは配布時の単一`bakedanuki/modules`を前提とし、既存の`MAYA_MODULE_PATH`に
`bakedanuki`フォルダを含むパスがあれば置き換え対象とします。開発用にtoolsとutilの
repositoryをsiblingに置き、それぞれの`bakedanuki/modules`を登録している場合は、
installerの再D&Dで片方のパスが外れます。この開発構成では両パスを各バージョンの
`Maya.env`へ手動登録してください。メニュー表示設定だけをONに戻す場合は、Script Editorで
次を実行できます。

```python
from bd_util.maya.ui import set_menu_auto_install_enabled

set_menu_auto_install_enabled(True)
```

起動時表示への反映にはMayaの再起動が必要です。

新規追加または置き換えられるパスは `/` 区切りで記述され、後から別のパスを追加しやすいように末尾へ `;` が付きます。

既存の `Maya.env` を変更するときは元の内容を同じフォルダの `Maya.env.bakedanuki-*.bak` に退避し、文字コード・BOM・改行を維持して一時ファイルから置き換えます。`MAYA_MODULE_PATH` が複数行にある場合や確認後にファイルが変更された場合は、安全のため書き換えを中止します。

実行時に生成された `installer.py` 自身の bytecode cache は処理終了時に削除されます。`__pycache__` 内に他の cache がある場合は、それらを残してフォルダも維持します。

変更を反映するには、Maya を再起動してください。

## Remove With uninstaller.py

1. 解除したいバージョンの Maya を起動します。
2. [uninstaller.py](uninstaller.py) をビューポートへドラッグ&ドロップします。
3. 対象の `Maya.env` と解除するパスを確認して `OK` を選びます。
4. Maya を再起動します。

`uninstaller.py` は、実行元の `modules` と同じパスだけを現在の Maya が読む `Maya.env` から解除します。共通 `modules` に同梱された util・tools・rig はまとめて次回起動から読み込まれなくなります。別の bakedanuki パスや他社の Module path は解除しません。対象がない場合と `Cancel` を選んだ場合は何も変更しません。

配布ファイル、シーン、`prefs/bakedanuki/menu.json` などの個人設定、現在実行中のメニューや plug-in は変更しません。配布フォルダが不要なら Maya を終了してから削除してください。複数の Maya バージョンへ登録した場合は、それぞれのバージョンで操作します。起動 bat や別の環境変数から追加したパスは、この操作の対象外です。

## Setup With Maya.env

`installer.py` を使用しない場合は、ユーザー自身の利用する Maya バージョン用 `Maya.env` に次の行を追加してください。

```env
MAYA_MODULE_PATH=D:/path/to/bakedanuki/modules;
```

Windows の標準的な配置先は次の通りです。Maya 2026 / 2027 を使う場合は、パス中の `2025` を利用するバージョンに読み替えてください。

```text
%USERPROFILE%\Documents\maya\2025\Maya.env
```

すでに `MAYA_MODULE_PATH` がある場合は、別行を作らず同じ行へ `;` 区切りで追加してください。

```env
MAYA_MODULE_PATH=D:/path/to/bakedanuki/modules;D:/another/maya/modules;
```

## Setup With bat

試しに起動するだけであれば、利用する Maya バージョンに合わせて次の bat を実行できます。

- [launchers/maya2025.bat](launchers/maya2025.bat)
- [launchers/maya2026.bat](launchers/maya2026.bat)
- [launchers/maya2027.bat](launchers/maya2027.bat)

これらの bat は、`bakedanuki/modules` を `MAYA_MODULE_PATH` の先頭に追加してから、対応する Maya を起動します。

Maya のインストール先が標準と異なる場合は、各 bat 内の `MAYA_EXE` を環境に合わせて変更してください。

## Check

Maya 起動後、Script Editor などで次を実行します。

```python
import bd_util

print(bd_util.__file__)
```

`bakedanuki/bakedanuki-util/python/bd_util/__init__.py` が表示されれば、`bakedanuki-util` のパスが通っています。

## Package Docs

- [bakedanuki-util](bakedanuki-util/README.md)
