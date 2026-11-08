# サイト情報とブラウザー起動

`bd_util.site`は、配布する`python/bd_util/site/site.json`を正本として
公開サイトの基点URLを扱います。初回のモジュール読込時にJSONを検証し、
`SITE_BASE_URL: Final[str]`へ保持します。
利用側は定数かURL生成APIを参照し、その都度JSONを読み直す必要はありません。

tools・rigなどは個別ページのパスを所有し、基点URLを重複して手書きしません。
パッケージ間のヘルプ連携仕様の正本は、bakedanuki-toolsの
`bakedanuki/bakedanuki-tools/docs/help_integration.md`です。
本書はutilで実装したAPIの利用方法を説明します。

## URLの取得

MayaのPythonから次のように使用します。

```python
from bd_util import site

site.SITE_BASE_URL
site.build_url("")
site.build_url("tools/tool/bd-channel-box/")
```

`SITE_BASE_URL`は読み取り用の公開定数です。Pythonコードにも同じURLを手書きせず、
JSONを変更・リリースして更新します。変更用setterやファイルの自動監視は設けません。
`build_url("")`はトップページ、空でない引数は相対ページパスを表します。
パスは先頭`/`なし・末尾`/`ありで、小文字英数字とハイフンからなる階層にします。
絶対URL、親階層、空の階層、クエリ、フラグメント、percent encodingは拒否します。
基点に`/bakedanuki-web/`などの共通パスがあっても、それを維持して結合します。
URL生成ではページの存在を確認する通信を行いません。

site.jsonはUTF-8・BOMなしで、`schema_version`は整数の`1`、
`base_url`は末尾が`/`のHTTPS絶対URLです。ホストはDNS名またはIPv6を検証し、
ユーザー情報、クエリ、フラグメント、空白・制御文字を含めません。
共通パスはページパスと同じ文字の規則に従います。
未知フィールド・未知schema・重複キー・形式不正は対象ファイル付きの`ValueError`、
読込失敗は`OSError`です。不正な値を補正したり、代替URLへ変更したりしません。

## ブラウザーで開く

```python
from bd_util import site
from bd_util.py.web import open_url

opened = open_url(site.build_url("tools/tool/bd-channel-box/"))
```

`open_url(url: str) -> bool`はHTTP/HTTPSのホスト付き絶対URLを検証して、
`webbrowser.open(url, new=2)`へ渡します。DNS名・国際化ドメイン・IPv6を扱い、
不正なホスト、空や範囲外のポート、空白・制御文字・バックスラッシュは拒否します。
引数を正規化して書き換えず、元のURLをブラウザーへ渡します。
新規タブなどの表示方法はOS・ブラウザー側に従います。

戻り値は起動依頼の成否であり、HTTP成功やページ表示完了を保証しません。
不正URLは`ValueError`、`webbrowser.Error`・`OSError`は呼び出し側へ伝わります。
利用側UIは`False`や例外を既存の通知経路で扱います。
importやURL生成だけでブラウザーを開くことはありません。

Web関連の処理は`py/web/`へまとめます。`__init__.py`は`open_url`の公開を担当し、
ブラウザー起動の実装は`browser.py`、siteと共有するURL検証は`_url.py`へ置きます。
公開入口は`bd_util.py.web.open_url`です。import時には実装も読み込みます。

## 配布とWeb側の読み取り

`site/__init__.py`・`site/site.json`と、`py/web/`内の`__init__.py`・
`browser.py`・`_url.py`を同梱します。
利用側のヘルプ原稿が存在しなくても、URL生成は可能です。
Web側は採用したutil ReleaseのJSONを直接読み、Pythonをimportしません。
この機能のためにMayaをWeb生成環境へ用意する必要はありません。
utilのトップレベル自体にはMaya依存があるため、
通常のPythonからの`import bd_util.site`は前提にしません。

サイトの住所を変更しても、古いutilを使う環境や既存のブックマークには届きません。
利用者はutilを更新し、Web側も同じ公開版を採用します。
旧URLからの転送は、公開先を継続利用できる範囲でWeb側に用意します。

## 開発時の再読み込み

JSONを書き換えただけでは保持値は変わりません。
toolsのUIを使用している場合は、次の入口でUIを破棄してからutilとtoolsを再構築します。

```python
import bd_tools

bd_tools.reload_package(reload_util=True)
```

利用側UIを開いていないutil単独の開発では、`bd_util.reload_package()`も使用できます。
開発中の旧配置`py/web.py`・`py/_url.py`から更新する場合は旧ファイルを残さず、
Mayaを再起動して新しいパッケージ配置を読み込みます。
個別モジュールや定数を変数へ保持していた場合は、reload後にimportし直してください。
複数の利用側が稼働していて一括reloadが未整備なら、Mayaを再起動します。
個人用TOML・UI設定保存・scene・Undoとは独立した固定情報です。

## 検証

`tests/py/test_site.py`はJSON、基点と相対パス、CWD非依存、保持値、正規reload、
同梱ファイルの欠落を検証します。siteとwebの両方のimport順で、起動の副作用がなく、
正規reload後に更新したサイト情報とブラウザーAPIを利用できることも確認します。
`tests/py/test_web.py`はブラウザー起動を差し替え、
起動URL・戻り値・例外・不正入力時に起動しないことを確認します。
`tests/typecheck/site_contract.py`は公開定数とAPIの型を固定します。

開発中の対象テストは次の入口を使います。

```powershell
.\scripts\test-pytest-maya2025.cmd tests/py/test_site.py tests/py/test_web.py
```

最終検証は`AGENTS.md`に従い`.\scripts\verify.cmd`を実行します。
ブラウザー起動を差し替えたテストは、HTTP到達や本体での操作確認の代わりではありません。
実ブラウザーの起動先確認は、利用側のヘルプUIを実装する段階で別途行います。
