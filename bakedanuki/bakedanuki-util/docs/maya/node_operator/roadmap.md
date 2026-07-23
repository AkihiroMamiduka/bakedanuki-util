# Roadmap

このページは `NodeOperator` 周辺の設計メモと今後の作業候補です。

1.0.0 までは開発中 API として扱い、必要なら破壊的変更も許容します。

## 現在固まっている方針

- Maya 専用パッケージとして割り切る。
- Maya 2025 / Python 3.11.4 以降を対象にする。
- `ModifierManager` を経由して `MDGModifier` / `MDagModifier` を扱う。
- `AttributeField` は entry point / descriptor に専念する。
- `AttrOperator` は定義情報を持つ。
- `PlugOperator` は scene 上の plug 操作を担当する。
- alias は同じ logical plug なら同じ instance を返す。
- `set_direct()` は便利用途として残すが undo 対象外と明記する。
- custom compound は低レベル型と意味付き alias を分ける。
- `Quat` は `Double4` の意味付き alias として扱う。

## 完了済みの大きな流れ

- pytest 導入。
- `plus_minus_average` / `wt_add_matrix` の代表的な挙動を pytest 化。
- `ModifierManager` 追加。
- NodeOperator / PlugOperator の modifier 参照を manager 経由へ移行。
- plug cache / indexed plug cache / child direct index などの速度改善。
- custom scalar compound の階層整理。
- `double2` / `double3` / `double4` / `float2` / `float3` などを custom compound 側へ移行。
- `long2` / `long3` / `short2` / `short3` を custom compound 側へ移行。
- unit compound の `double_angle2/3`、`double_linear2/3`、`float_angle2/3`、`float_linear2/3` を追加。
- compound `get()` / `set()` / `set_direct()` を整備。
- compound child limit の public method 化。
- `lookup.py` の double4 / quat 解決対応。

## 近い作業候補

### 1. docs の継続更新

仕様変更後は `bakedanuki/bakedanuki-util/docs/maya/node_operator` を更新します。

特に API の使用例、未対応仕様、設計判断の理由はここに残すと後続作業が安定します。

### 2. lookup.py の追従

新しい attribute type や custom compound を追加したら `lookup_attr_cls()` の解決対象に追加します。

混在型や未対応型は fallback せず、明示的に unsupported として扱う方針です。

### 3. pytest の移植

既存 `_test` のうち、仕様固定できるものを順次 pytest へ移します。

優先候補:

- extra attribute
- custom compound
- keyframe
- transform の built-in compound alias
- connect / disconnect / next index

ベンチマークは `_test` に残します。

### 4. MPxCommand 連携

`ModifierManager` を MPxCommand の undo / redo に組み込む設計を固めます。

目標は command ごとの実装を次の形に近づけることです。

```python
def undoIt(self):
    self.modifier_manager.undo_it()

def redoIt(self):
    self.modifier_manager.redo_it()
```

### 5. set_direct の扱い

`set_direct()` は高速で便利ですが、undo には参加しません。

今後も明確に「即時編集用」として扱い、undo が必要な処理では `set()` と `ModifierManager` を使います。

### 6. 文字化けコメントの整理

一部ソース内に文字化けしたコメントや docstring が残っています。

実装に影響しない箇所でも、今後の保守性のために UTF-8 の日本語コメントへ修復する価値があります。

### 7. 1.0.0 前の API 整理

正式リリース前に次を整理します。

- 公開 API と内部 API の境界。
- deprecated なしで削除してよい旧実装。
- `AddAttr` へ公開する型。
- docs と README の導線。
- MayaModule への導入方法。

## watch points

- `NodeOperator.__getitem__()` の文字列パス解析は未確定です。
- `set_direct()` は undo 非対応です。
- `lookup.py` は型追加時に更新漏れが起きやすいです。
- unit 系の戻り値や入力単位は、実装と docs を常に揃える必要があります。
- 速度改善は、利便性を壊さない範囲で行います。
