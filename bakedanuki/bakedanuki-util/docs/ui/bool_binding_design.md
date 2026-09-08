# bool bindingの設計・保守メモ

bool UI基盤を読み直すときや、新しいView・値型を追加するときのための設計メモです。
公開API、引数、サンプル実行例は[UI README](README.md)を参照してください。
各名称の意味と利用コードとの対応は[このパッケージでのMVVMの役割](mvvm_roles.md)を参照してください。
ここでは、現在の構造を選んだ理由と、変更時に維持したい境界を説明します。

## コードを読む順番

まずMaya同期なしの経路を理解し、その後にMaya adapterと共有サンプルを読むと追いやすくなります。

| 順番 | 実装 | 確認すること |
| --- | --- | --- |
| 1 | [value.py](../../python/bd_util/ui/binding/bool/value.py) | Viewへ公開する現在値と変更通知 |
| 2 | [store.py](../../python/bd_util/ui/binding/bool/store.py) | 正本を読み書きする契約とPython object用の実装 |
| 3 | [command.py](../../python/bd_util/ui/binding/bool/command.py) | 値の変更要求と実行可否 |
| 4 | [view_model.py](../../python/bd_util/ui/binding/bool/view_model.py) | Storeの確定値を採用するHub |
| 5 | [view/check_box.py](../../python/bd_util/ui/binding/bool/view/check_box.py) | 入力と表示更新を分ける最小のQt View |
| 6 | [Maya binding/bool_plug.py](../../python/bd_util/maya/ui/binding/bool_plug.py) | MayaをStoreまたはViewとして扱うadapter |
| 7 | [binding.py](../../python/bd_util/ui/binding/bool/binding.py)・[Maya bool_binding.py](../../python/bd_util/maya/ui/binding/bool_binding.py)・[Maya bool_plug_binding.py](../../python/bd_util/maya/ui/binding/bool_plug_binding.py) | 1属性の組み立てと終了操作 |
| 8 | [bool_sample](../../python/bd_util/_sample/maya/ui/bool_sample) | 最小Widget・全View・共有Managerへの組み込み方 |

`BoolValueStore`はStoreの契約名であり、Model全体を表す基底クラスではありません。
dataclassを使うtoolでは、そのdataclassがModel、指定した1属性へのアクセス境界が
`PythonBoolAttributeStore`です。リグ固有のデータ構造や処理はこの汎用基盤へ入れません。

## 正本と入力経路を分けて考える

### BoolValueはViewが共通に読む窓口

Storeなしでは`BoolValue`がメモリ上の値を保持します。Storeありでは、Storeが扱う正本の
確定値をViewModelが`BoolValue`へ反映します。Viewはどちらでも同じAPIを使えますが、
Storeありの`BoolValue`は正本を直接参照するpropertyではなく、最後に同期した値です。

そのため、plain dataclassへ直接代入すると、明示的に`refresh_from_store(store)`するまでは
正本と公開値が異なることがあります。サンプルの`Print Data Value`は公開値ではなく
`store.read()`を出力するため、この違いも確認できます。

### Commandは入力窓口、ViewModelが確定処理を仲介する

`SetBoolCommand`は実行可否を公開し、要求をViewModelへ渡します。Command自身はWidgetや
Maya nodeの一覧を持ちません。ViewModelがStoreへ書き込み、`write()`の返す実値を採用し、
Viewがその通知を受けて表示を更新します。setterで要求値が補正・拒否されても、要求した値を
そのまま表示上の正本として扱わないための分担です。

| 入力・変更元 | 正本への適用 | ViewModelへの反映 |
| --- | --- | --- |
| Qt Viewの操作／共通APIからのPython入力 | CommandからViewModelを通してStoreへ書き込む | 書き込み後の実値を採用する |
| Python objectへの直接代入 | 呼び出し元ですでに変更済み | 明示的な`refresh_from_store(store)`で読み直す |
| `MayaBoolPlugStore`のplugへの外部変更 | Maya側ですでに変更済み | callbackからStoreを読み直し、書き戻さない |
| `MayaBoolPlugView`のplugへの外部変更 | Python Storeにはまだ未適用 | callback後にCommandへ入力し、Storeの実値を採用する |

「全入力をCommandへ集める」は変更要求の入口を揃える方針です。正本へ適用済みの外部変更を
通知する経路まで、書き込みCommandとして再実行する必要はありません。

`MayaBoolPlugView`の初期同期ではPython Storeの値をMayaへ適用します。作成時にMayaの値を
採用したいtoolは、先にPythonデータを初期化するか、Maya自体を正本とする
`MayaBoolPlugStore`を選びます。

### 同値通知と同期失敗にも意味がある

- `BoolValue.changed`は公開値が変わったときだけ通知する。
- Qt Viewへの表示更新では入力signalを抑制し、Commandへの折り返しを防ぐ。
- Maya Store自身の書き込みcallbackは確定値を取得するまで抑制し、その後にrefreshする。
  `changed` slotでBindingを終了しても破棄済みplugを再読込せず、slotから別の値を設定した
  場合は最新のMaya値を採用する。Storeへの直接writeでも変更通知を維持する。
- `SetBoolCommand.executed`と`BoolViewModel.store_refreshed`は、同値でも通知する経路がある。
  Maya入力の反映が保留中でも、後から確定したPython側の同値要求を優先するために使う。
  `changed`だけで足りると判断して削除しない。
- Maya Viewのlock・入力接続・同期失敗を理由に、Python Storeの編集まで停止しない。
  正本の実値とMayaとの同期状態は別に扱い、`is_synchronized`と`last_sync_error`／
  `sync_failed`で不一致を確認できるようにする。

`SetBoolCommand`はMayaの専用undo commandではありません。Mayaへの値設定はadapter内の
`cmds.setAttr()`を使用します。Pythonデータだけの変更をMaya undoへ登録する機能や、
PythonとMayaを一括で巻き戻す汎用transactionは提供していません。

## QObjectの所有とViewの参照を混同しない

### parentは見た目ではなく寿命のためにも使う

`BoolViewModel`は見た目を持ちませんが、signalを使う`QObject`です。QObjectの`parent`は
所有者を表し、親が破棄されると子も破棄されます。[Qt公式: Object Trees & Ownership](https://doc.qt.io/qt-6/objecttrees.html)

- 1つのFeature Widgetで完結する場合は、`BoolViewModel(parent=self)`でよい。
- 複数Windowで共有する場合は、個々のWindowから独立した共通ownerを使う。
- Viewは受け取ったViewModelを参照するだけで、`setParent()`によって所有権を移さない。
- Python変数でViewModelを参照していても、Qtの親が破棄したC++ objectの寿命は延ばせない。

共有サンプルのManagerは通常のPythonクラスで、その中に共通owner用の`MayaBoolBinding`を
保持します。Windowの実際のQt parentはMaya main windowです。Managerによる管理・参照と、
Qt parentによる親子関係は別の関係です。

### 遅延させているのはViewの破棄ではなく、破棄通知後のUI操作

開発中、共通親の破棄に伴うViewModelの`destroyed`通知から、同じ親の下にあるViewを
同期的に操作する経路で、Windowを閉じるとMayaも終了する現象を確認しました。
現行実装では、この通知からUIへ再入しないようにしています。

1. ViewModelの`destroyed`は、View側の引数なし`@qt.Slot()`へ`QueuedConnection`で接続する。
2. Viewも親と一緒に破棄される場合は、Qtの親子関係に従って破棄される。
3. Viewだけが残る場合は、後で届く通知によって入力接続を解除し、Viewを無効化する。

ViewModelはViewに`deleteLater()`を呼びません。View自身の破棄責任はそのQt親などのownerに
あります。破棄されたQObjectへのsignal接続と未処理eventはQtが除去するため、受信側Viewも
破棄された場合はそのViewへの保留中の通知も除去されます。[Qt公式: QObjectデストラクタ](https://doc.qt.io/qt-6/qobject.html#dtor.QObject)

QObject Storeの破棄通知も、ViewModelを経由してViewの有効状態を変更するため、同様に
遅延させます。`qt.isValid()`は破棄済みobjectへのアクセス防止に使いますが、親の破棄途中に
同期的なUI操作を行ってよいという判定には使いません。

利用側で「全Viewを作ってからViewModelへparentを設定する」手順は不要です。
通常の値変更通知をすべて遅延させる設計でもありません。破棄通知の接続を短縮したり、
受信側を持たないlambdaへ置き換えたりするときは、この寿命管理を崩さないか確認してください。

### Maya callback解除は待たせない

ownerやMaya adapter自体の破棄時には、callback IDの解除は即座に行います。一方、その破棄中の
通知からViewModel経由でUIを同期操作することは避けます。外部resourceの解除と、UIへの
状態反映は別の仕事です。予約済みのMaya入力も、adapterの`dispose()`後には適用しません。

`MayaBoolPlugView.dispose()`は同期を停止する処理であり、Maya nodeやPythonデータを
削除する処理ではありません。明示的な`dispose()`やnode削除の処理と、QObjectの破棄通知を
同じタイミングの処理としてまとめ直さないでください。

同様の終了問題が再発した場合は、共通親の破棄中のsignal経路とcallback残存を確認します。
今回の問題への対処として、`WA_DeleteOnClose`を無効化して破棄を避けたり、
`WA_QuitOnClose`やアプリ全体の`quitOnLastWindowClosed`を変更したりする必要はありません。

## サンプルの責務と使い分け

`BoolBinding`は1つのStoreと専用ViewModelを組み立てるQObjectです。正本の値を追加で保持せず、
`value`・`set_value()`・`refresh()`を既存ViewModelへ委譲します。`from_attribute()`は
`PythonBoolAttributeStore[T]`を作り、`store.instance`の具体型を維持します。
外部StoreのQt parentは変更せず、そのStoreの破棄責任も引き取りません。
`MayaBoolBinding`は同じownerに任意のMaya Viewを1つ追加し、同期状態は`maya_view`へ公開します。

`MayaBoolPlugBinding`はMaya plugを正本とし、`MayaBoolPlugStore`と専用ViewModelを所有します。
Storeのcallback先とattach先を同じViewModelにするため、`BoolBinding._initialize()`で
ViewModelを作成した後にStore factoryを呼びます。この入口はconstructor専用で、
通常の`BoolBinding(store)`も同じ初期化処理へ委譲します。Storeの差し替えには使用しません。
外部から渡されたStoreの終了責任は引き取りませんが、Maya plug版で内部生成したStoreは
Bindingの`dispose()`から即座に終了します。途中で構築・初期読込が失敗してもcallbackを解除します。
Maya callback registryはownerを保持するため、最後のPython参照やViewの消滅によるGCを
終了条件にはしません。Qt parentの破棄または明示的な`dispose()`で管理します。

`BoolBinding.changed`は`view_model.value.changed`を返す読み取り専用propertyです。
Qtの送信元は既存の`BoolValue`のままで、signalの中継接続や変更判定を追加しません。
通知タイミング・引数・接続解除は元のsignalと共通で、具体的な`SignalInstance`の型を公開します。
`MayaBoolBinding`・`MayaBoolPlugBinding`もこれを継承します。初期値の再通知、同値の通知、
Maya同期完了の通知は行いません。
終了後の取得は既存の`view_model`と同じ検証で拒否し、通知中の`dispose()`にも対応します。

Qt Bool Viewの第1引数は`BoolViewModel | BoolBinding[BoolValueStore]`です。
`view/_source.py`で生成前に入力元を検証し、ViewModelと参照保持用のBindingへ解決します。
Viewはその後もViewModelのCommandと通知だけを使い、StoreやMaya Viewを直接操作しません。
`view_model=`キーワードと`view.view_model: BoolViewModel`は維持します。

`BoolBinding`のStore型引数は共変です。公開Storeは読み取り専用propertyで、生成後に
別Storeを受け取るAPIもないため、具体的な`PythonBoolAttributeStore[T]`を持つBindingを
共通のStore境界へ渡せます。呼び出し元の`binding.store.instance`では具体型Tが残ります。
実行時に失われる型引数のcastは、引数を解決する共通処理の境界に限定します。

ViewがBindingを受け取った場合は、ViewModelに加えてBinding自体も参照保持します。
これは、一時生成した親なしBindingがViewを返すfactoryから脱落しないためです。
`setParent()`による所有権移動や、Viewを閉じた際の共有Bindingの`dispose()`は行いません。
明示終了済み・Qt破棄済みBindingは既存の`binding.view_model`の検証で拒否します。
ViewModelを直接渡す経路も継続し、既存のqueued破棄通知を利用します。

明示的なbindingの`dispose()`は、Maya callbackを即座に解除し、ViewModelの`dispose()`で
CommandとStore再読込を停止してからQt削除を予約します。`BoolViewModel.dispose()`自体は
QObjectを削除しません。値変更通知のslot内で終了した場合も、処理の後半でCommandが再び
有効にならないよう終了状態を確認します。Qt親の破棄では従来の破棄通知とcallback registryが
後始末を担当し、破棄通知から同期的なUI操作は追加しません。

関連ファイルはすべて`bd_util/_sample/maya/ui/bool_sample/`以下にあります。
共通の`data.py`はサンプルデータ、`bool_plug.py`は任意Maya指定の組み合わせの検証です。
名前からのplug解決はMaya基盤の`bool_plug_resolver.py`へ移し、`resolve_bool_plug()`として
公開しています。最上位の単一boolに範囲を限定し、配列・compound・子属性・属性パスを拒否します。

- `minimal.py`: `BoolBinding.from_attribute()`の結果を直接CheckBoxへ渡す入口。
- `maya_plug.py`: 既存Maya bool plugを正本にする最小WidgetとWindow。`show()`は対象を
  検証してから前のWindowを置き換え、`dispose()`はnodeを残してUIとcallbackを終了する。
- `multi_attribute/widget.py`: 3つのbool属性に個別のBindingを作り、`changed`でプレビューの
  表示と編集可否を更新する。初期値を別途適用し、データへ直接代入した場合は
  `refresh_from_data()`で全Bindingを読み直す。編集可否は親の設定欄に適用し、
  Bool View自身のCommand実行可否を上書きしない。UIを無効にしても属性値は保持する。
- `multi_attribute/data.py`と`window.py`: サンプル固有の表示設定と、既存Controllerによる
  Window管理。各BindingはWidgetが所有し、再表示では新しいデータを作る。
- `bool_views/widget.py`: 自己完結するFeature Widget。渡されたPython object・属性名から
  `MayaBoolBinding`とQt View一式を構築する。
- `bool_views/window.py`: WindowはFeature WidgetとMaya指定を保持し、Managerは構成による
  再利用判定とWindow Controllerを管理する。生成引数はfactory呼び出し中だけManagerが保持する。
- `shared_bool_views/manager.py`: Windowから独立した`MayaBoolBinding`を保持する。
  Window A／Bの生成・再表示・終了をControllerへ委譲する。
- `shared_bool_views/widget.py`と`window.py`: 受け取った共有ViewModelを表示する。
  ViewModelを直接渡す例として残し、WindowごとのStoreやMaya Viewは作らない。

最初の組み込み例には`minimal`、複数属性とUI連動には`multi_attribute`、全View一覧には
`bool_views`、表示の寿命とbindingの寿命を分ける例には`shared_bool_views`を使います。
共有Window版で共有するのは1つのViewModelであり、複数のViewModel同士を
同期する仕組みではありません。

共有サンプルでは両Windowを閉じてもbindingは存続します。Managerを変数などで保持し、
toolの終了時には`manager.dispose()`を呼びます。終了済みManagerの再利用は行わず、
新しいManagerを作成します。再表示でMaya callbackがWindow数に応じて増えないことも重要です。

`bool_views.show()`は短い実行例のため、module内の既定Managerへ委譲します。
module-levelの参照が完全になくなったわけではありません。独立した寿命が必要なtoolでは、
Managerインスタンスを上位のtool Controllerなどで保持してください。

## 今後の拡張で維持すること

- 新しいBool Viewは`ui/binding/bool/view/`へ置き、公開APIは`bd_util.ui`から辿れるようにする。
  入力はCommandへ渡し、表示はViewModelから受け取り、他のViewやStoreを直接操作しない。
- 表示文字列とbool値を分離し、入力拒否・値の補正時にはStoreの実値へ表示を戻す。
  読み取り専用Viewは、Storeが書き込み不可でも現在値を表示する。
- 新しいStoreの`write()`は成功可否ではなく確定後のbool実値を返す。値を暗黙に`bool()`へ
  変換して型違反を隠さず、利用不可と書き込み不可を区別する。
- Maya固有の処理は`bd_util.maya.ui`へ閉じ込め、汎用側では`bd_util.ui.qt`を使う。
  Pylance向けの型情報と、PySide6の対応version間の接続・切断方法も確認する。
- 破棄順の安全性は新しいViewでも維持する。単独破棄と、共通親による一括破棄の両方を試す。
- 現状は1つのViewModelにStoreは1つ、Maya Viewは最大1つ。Storeの動的差し替えや
  複数Maya View、bool以外の値型、汎用の共有Sessionは未実装として扱う。
  `BoolBinding`はbool 1属性の組み立て補助に留め、汎用SessionやView一括生成へ拡張する場合は
  実際の用途を確認してから検討する。

## 変更時の確認先

| 対象 | 回帰テスト |
| --- | --- |
| Value・Store・Command・全Qt View・破棄順 | [tests/ui/test_bool_binding.py](../../../../tests/ui/test_bool_binding.py) |
| 組み立てAPI・変更通知・明示終了・最小sample | [tests/ui/test_bool_binding_facade.py](../../../../tests/ui/test_bool_binding_facade.py) |
| ViewへのBinding直接入力・一時参照・共有寿命 | [tests/ui/test_bool_view_source.py](../../../../tests/ui/test_bool_view_source.py) |
| Maya組み立て・名前解決・callback解放 | [tests/maya/ui/test_maya_bool_binding_facade.py](../../../../tests/maya/ui/test_maya_bool_binding_facade.py) |
| Maya plug正本の組み立て・初期読込・終了・構築失敗 | [tests/maya/ui/test_maya_bool_plug_binding_facade.py](../../../../tests/maya/ui/test_maya_bool_plug_binding_facade.py) |
| Maya plug版の全View・共有寿命・サンプル | [tests/ui/test_maya_bool_plug_binding_sample.py](../../../../tests/ui/test_maya_bool_plug_binding_sample.py) |
| Maya plug版の型・補完 | [maya_bool_plug_binding_contract.py](../../../../tests/typecheck/maya_bool_plug_binding_contract.py) |
| 自己完結WidgetとWindow Manager | [tests/ui/test_bool_views_sample.py](../../../../tests/ui/test_bool_views_sample.py) |
| 複数属性・UI連動・初期表示・編集禁止中の更新 | [tests/ui/test_multi_attribute_bool_sample.py](../../../../tests/ui/test_multi_attribute_bool_sample.py) |
| 複数Window・再表示・共有Maya callback | [tests/ui/test_shared_bool_views_sample.py](../../../../tests/ui/test_shared_bool_views_sample.py) |
| Mayaを正本とする同期 | [tests/maya/ui/test_bool_plug_binding.py](../../../../tests/maya/ui/test_bool_plug_binding.py) |
| Python正本とMaya View・保留入力・同期失敗 | [tests/maya/ui/test_bool_plug_view.py](../../../../tests/maya/ui/test_bool_plug_view.py) |
| 公開APIの型・補完 | [ui_contract.py](../../../../tests/typecheck/ui_contract.py)、[bool_view_source_contract.py](../../../../tests/typecheck/bool_view_source_contract.py)、[multi_attribute_bool_sample_contract.py](../../../../tests/typecheck/multi_attribute_bool_sample_contract.py)、[shared_bool_views_contract.py](../../../../tests/typecheck/shared_bool_views_contract.py) |

特に、同値Command／refreshが保留中のMaya入力より優先されること、初期同期に失敗しても
callbackを残さないこと、`dispose()`後に保留入力を適用しないことを維持します。

開発中のUI確認はrepository直下で`.\scripts\test-ui-maya-all.cmd`、最終確認は
`.\scripts\verify.cmd`を使います。対応環境と自動テスト結果は[UI README](README.md)へ
集約し、このメモでは重複管理しません。

Maya本体での確認では、単一／共有サンプルについて次も確認してください。

1. UI操作、Python Command、Maya外部変更が同じ値へ同期する。
2. Pythonデータへの直接代入と明示refreshの違いを`Print Data Value`で確認できる。
3. Maya指定なしでも動作し、Windowの×ボタンでMayaが終了しない。
4. 共有Windowの一方を閉じても、もう一方とMayaの同期が続く。
5. 両方を閉じた後もManager経由で操作でき、再表示時に最新値が表示される。
6. toolの`dispose()`後は同期が止まり、データとMaya node自体は残る。

module reloadは古いManagerの`dispose()`を先に実行し、古いQObjectやcallbackを残さずに
行ってください。自動テストの成功だけで、Maya本体でのWindow終了確認を代替しない方針です。
