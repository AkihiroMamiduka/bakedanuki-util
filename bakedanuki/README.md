# bakedanuki

このフォルダは、bakedanuki 系パッケージを Maya Module としてまとめて配置するための親フォルダです。

`bakedanuki-util`、今後追加予定の `bakedanuki-rig`、`bakedanuki-tool` などは、各パッケージの `bakedanuki` フォルダを同じ場所へ重ねて配置する想定です。

## Layout

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
    bd_rig.mod
    bd_tool.mod

  bakedanuki-util/
    README.md
    LICENSE
    docs/
    python/

  bakedanuki-rig/
    README.md
    LICENSE
    docs/
    python/
    plugins/

  bakedanuki-tool/
    README.md
    LICENSE
    docs/
    python/
    scripts/
```

Maya には `bakedanuki/modules` だけを `MAYA_MODULE_PATH` として追加します。

各 `.mod` ファイルが、それぞれのパッケージフォルダ内にある `python`、`plugins` などを Maya へ追加します。

## Setup With installer.py

最も簡単な導入方法は、[installer.py](installer.py) を Maya のビューポートへドラッグ&ドロップする方法です。

`installer.py` は、自分自身と同じ階層にある `modules` フォルダを検出し、現在起動している Maya バージョン用の `Maya.env` に `MAYA_MODULE_PATH` を追加します。

追加前には確認ダイアログが表示され、`OK` を選んだ場合だけ `Maya.env` を更新します。`Cancel` を選んだ場合は何も変更しません。`Maya.env` が存在しない場合は新しく作成します。

同じ modules パスが既に登録されている場合は重複して追加しません。パスの大文字・小文字、区切り文字の `\` / `/`、末尾の区切り文字の違いも同じパスとして扱います。

別の bakedanuki フォルダを指すパスが登録されている場合は、置き換え確認のダイアログが表示されます。置き換え時も、bakedanuki 以外の module パスはそのまま維持されます。

新規追加または置き換えられるパスは `/` 区切りで記述され、後から別のパスを追加しやすいように末尾へ `;` が付きます。

変更を反映するには、Maya を再起動してください。

## Setup With Maya.env

ユーザー自身の利用する Maya バージョン用 `Maya.env` に、次の行を追加してください。

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

このフォルダにある [Maya.env](Maya.env) は追記例です。この場所に置くだけでは Maya には読み込まれないため、自分の Maya preferences 配下の `Maya.env` へ内容をコピーして使ってください。

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
