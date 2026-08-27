# Core Attribute Access

このページは `AttributeField` / `AttrOperator` / `PlugOperator` 周辺のコア仕様をまとめます。
属性型そのものの仕様は [attributes.md](attributes.md)、生成器の仕様は [generator.md](generator.md) を参照します。

## 役割

`AttributeField` は entry point / descriptor です。
Field は node instance を保持せず、定義情報を持ち、アクセス元に応じて `AttrOperator` または `PlugOperator` を生成します。

`AttrOperator` は attribute 定義側の情報を持ちます。
`PlugOperator` は Maya scene 上の plug 操作を担当します。

## access mode

`AttributeField.__get__()` はアクセス元に応じて戻り値を変えます。

- `NodeClass.attr`
  - `AttrOperator` を返します。
- `node.attr`
  - `PlugOperator` を返します。
- `node.compound.child`
  - parent plug から child plug を返します。
- class 定義中の `compound.child` alias
  - `AttributeField` 自体を返し、parent/attr path を確定させます。

## plug cache

`NodeOperator` instance は `_plug_cache` を持ちます。
同じ logical plug へ複数経路からアクセスした場合でも、可能な限り同じ `PlugOperator` instance を返します。

```python
node.output3D is node.o3
node.output3D.output3Dx is node.output3Dx
node.wtMatrix[0].matrixIn is node.i[0].m
```

top-level plug は attr path を key にします。
child plug は logical path を含む key で cache します。
このため、long name / short name alias のどちらから入っても同じ plug を再利用できます。

## indexed plug cache

multi plug の index access は `PlugOperator.__getitem__()` で処理します。
`plug[0]` のような int access は `_indexed_plug_cache` に保存され、同じ index への再アクセスでは同じ `PlugOperator` instance を返します。

```python
node.input3D[0] is node.input3D[0]
```

`plug[next]` は Python builtin の `next` を sentinel として扱い、次に接続可能な logical index を取得します。
next index は connect 系処理の速度改善のため cache されます。

## child index

`AttributeField` は owner class 内での定義順から `_child_index` を持ちます。
同じ Field が short alias として複数名で定義されている場合は、同じ object id を重複カウントしません。

compound child plug の取得では、まず `MPlug.child(child_index)` を試し、失敗した場合だけ名前探索へ fallback します。
これにより、通常の compound child access は文字列探索を避けられます。

## attr path

child Field は parent Field / parent Plug / parent Attr からアクセスされたときに、parent attr path と自身の name から `_attr_path` を組み立てます。

Generator 由来の class では、Maya 側の path が Python field 名と異なる場合、Field constructor の `long_name=` / `short_name=` に本来の Maya 名を渡します。

```python
name_ = DataStringField(long_name="name", short_name="nm")
nm = name_
```

## get / set / set_direct / round

値操作methodは`PlugOperator`基底ではなく、実際に対応するplug型だけが
提供します。対応しないmethodはIDE補完にも表示されません。

`set()` は `ModifierManager.dg_mod` 経由の編集です。
undo / redo の対象にしたい処理ではこちらを使います。

`set_direct()` は即時編集用です。
速度計測や一時的な直接編集には便利ですが、`ModifierManager` の stack には積まれないため undo 対象外です。

`value` / `value_direct` propertyは提供しません。取得には`get()`、
編集には反映方法に応じて`set()`または`set_direct()`を使用します。

浮動小数点のscalar / scalar compound型は`round(ndigits=0)`を提供します。
現在のscene値をPython組み込みと同じ規則で丸め、`set()`と同じ
`ModifierManager.dg_mod`へ積みます。matrix、typed data、quaternion、整数型には
提供しません。

```python
node.translate.round(3)
mod.do_it_dg()
```

compound 系の `set()` / `set_direct()` は展開引数と sequence の両方を受け取ります。

```python
node.offset.set(1.0, 2.0, 3.0)
node.offset.set([1.0, 2.0, 3.0])
node.offset.set_direct(1.0, 2.0, 3.0)
```

要素数が child 数と一致しない場合は `TypeError` を出します。

## connect / disconnect

接続元の `connect()` / `disconnect()` は、`self` から引数のplugを操作します。

```python
src.output.connect(dst.input)
src.output.disconnect(dst.input)
```

接続先から操作する場合は `connect_from()` / `disconnect_from()` を使います。
接続元には `PlugOperator`、`"node.attr"`、node名とattribute pathを並べた
`list[str]` / `tuple[str, ...]` を渡せます。

```python
dst.input.connect_from(src.output)
dst.input.connect_from("src.output")
dst.input.connect_from(["src", "output"])
dst.input.disconnect_from("src.output")
```

いずれも `ModifierManager.dg_mod` へ操作を積み、`do_it_dg()` で実行します。

## 現状の注意点

- `set_direct()` は undo 対象外です。
- `PlugOperator.__getitem__()` の string access は `getattr(self, key)` 相当です。
- 過去に想定していた `"attrName[0].child"` のような文字列 path parser は、現状 active な仕様ではありません。
- alias は「同じ logical plug なら同じ instance」を返す方針です。
