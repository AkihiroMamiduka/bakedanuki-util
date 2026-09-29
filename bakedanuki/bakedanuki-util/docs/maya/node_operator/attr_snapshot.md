# 属性値スナップショット

`bdu.AttrSnapshot` は、複数ノードの評価済み現在値をシーンから独立して保持します。`AnimationClip` と同じ `capture()` / `save()` / `load()` / `extract()` / `restore()` を使用します。時間範囲やカーブ全体は保存せず、復元時点で指定した値を適用します。

```python
import bd_util as bdu

snapshot = bdu.AttrSnapshot.capture(["ctrlA", "settings"])
snapshot.save("pose/values.json")

loaded = bdu.AttrSnapshot.load("pose/values.json")
mod = bdu.ModifierManager()
report = loaded.restore(mod, frame=12, anim_layer="PoseLayer")
mod.do_it_dg()
print(report.applied_count, report.skipped)
```

`capture()` は即時取得です。既定では keyable 属性と Channel Box 専用属性を収集し、Channel Box に表示されない属性は除外します。`include_channel_box=False` で Channel Box 専用属性を除外し、`include_hidden=True` で Channel Box 非表示属性を含めます。この `hidden` は `MFnAttribute.hidden` ではありません。`attributes=[...]` で明示した属性は表示条件に関係なく取得します。複合属性は末端へ展開し、配列は存在する logical index のみ保存します。

対応する値は bool、整数、浮動小数点、enum の数値、角度、距離、文字列です。角度は degree、距離は centimeter で保存します。matrix、message、その他の typed data は対象外です。JSON は schema 1 として値型・ノード名・属性パスを保持します。`save()` / `load()` はシーンを編集せず、ファイル操作は Undo 対象外です。

## 保存ノードの部分抽出

`extract(nodes=...)` は保存済みのノードから指定したものだけを選び、その全属性を持つ独立した `AttrSnapshot` を即時に返します。指定順が新しい保存順になり、`restore(targets=...)` の位置対応にも使われます。元データ、シーン、予約中の操作は変更しません。

```python
part = loaded.extract(nodes=["ctrlA", "settings"])
part.save("pose/part.json")

mod = bdu.ModifierManager()
part.restore(mod, targets=["other_ctrl", "other_settings"])
mod.do_it_dg()
```

`nodes` は保存名、`NodeOperator`、`MObject` を混在できる iterable です。文字列なら元ノードがシーンから消えていても選択できます。名前空間は省略せず、短い DAG 名は保存名の末尾と一意に一致するときだけ使えます。`|` を含む名前は保存名との完全一致です。既存ノード参照では現在の full path を優先し、次に短い名前で照合します。明示名を持つ作成待ち `NodeOperator` も使用できますが、予約中の作成は実行しません。

空の指定、不明名、曖昧な短名、重複指定はエラーです。属性のないノードは他に値を持つノードがあれば残し、選択結果全体に属性がない場合はエラーです。抽出結果は元と同じ schema 1 で `save()` / `restore()` を使用できます。

`restore()` は `ModifierManager` に予約し、`do_it_dg()` で実行します。`targets` は保存ノード順に対応する別ノードの列、`namespace` は保存名の名前空間置換です。両者は併用できません。入力接続がなければ `anim_layer` の指定に関係なく通常の値設定を行います。既存の時間アニメーションカーブで駆動される属性は、`frame` の時刻にキーを設定します。`frame=None` は予約時の Maya UI 時刻です。`anim_layer=None` はルートレイヤーを使用します。指定レイヤーに属性が所属していない場合、別のレイヤーへ勝手にキーを設定しません。

通常の DG 入力接続、存在しない属性、型不一致、ロック・参照・書き込み不可の属性などは、接続を維持したまま属性単位でスキップします。キー設定先のアニメーションカーブがロックまたは参照されている場合も、その属性だけをスキップします。カーブのノードロックやキーに関わる Plug のロックは保護として扱い、カーブへ追加された無関係な属性のロックは対象外です。`anim_layer` を指定した場合はそのレイヤーのカーブだけを判定します。

`report.skipped` で理由を確認できます。`strict=True` は `do_it_dg()` 時、復元前に全対象を確認し、スキップ対象があれば例外にします。予期しない実行時エラーは操作全体をロールバックします。`report.complete` は `do_it_dg()` 後に `True` になります。復元は `ModifierManager.undo_it()` / `redo_it()` で取り消し・やり直しできます。
