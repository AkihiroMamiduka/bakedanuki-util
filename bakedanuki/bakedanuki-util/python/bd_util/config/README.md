# パッケージの既定設定

利用者が編集する同梱設定を、このディレクトリにまとめます。
Maya preferences 内の UI 設定・保存データは、従来の保存先を使います。

## `Nodes()` の IDE 補完

`typing.pyi` の import を変更すると、`typing_maya_version` を省略した
`bdu.Nodes()` の補完対象を選べます。初期値は `Maya2025Plus` です。

```python
from ..typing_profiles import Maya2025Plus as DefaultNodes
```

Maya 2026 だけを対象にする場合です。

```python
from ..typing_profiles import Maya2026 as DefaultNodes
```

正式対応済みの Maya 2026 以降で共通する補完を使う場合です。

```python
from ..typing_profiles import Maya2026Plus as DefaultNodes
```

有効にする import は一つにし、`DefaultNodes` という名前と、末尾の
`__all__ = ["DefaultNodes"]` を維持してください。

| プロファイル | 対応する明示引数 | 現在の補完対象 |
| --- | --- | --- |
| `Maya2025` | `"2025"` | Maya 2025 |
| `Maya2026` | `"2026"` | Maya 2026 |
| `Maya2027` | `"2027"` | Maya 2027 |
| `Maya2025Plus` | `"2025+"` | Maya 2025 / 2026 / 2027 の共通部分 |
| `Maya2026Plus` | `"2026+"` | Maya 2026 / 2027 の共通部分 |
| `Maya2027Plus` | `"2027+"` | Maya 2027 |

`Plus` の対象は正式対応済みの最新 version までです。対応 version を追加すると、
対象範囲の共通部分を再計算します。

```python
import bd_util as bdu

bd_nodes = bdu.Nodes()
```

設定は `create`、`existing`、`create.with_transform` に適用します。
優先順位は次のとおりです。

1. `typing_maya_version` に明示した version または `+` 範囲。
2. プロジェクトの `stubPath` にある `bd_util_typing_config.pyi`。
3. 同梱の `bd_util/config/typing.pyi`。

省略と明示的な `None` は同じ設定を使います。共通補完を明示したい場合は、
`bdu.Nodes(typing_maya_version="2025+")` と指定できます。

この設定は IDE が読む型情報です。Maya の実行バージョン、利用可能なノード、
`bdu.node_types` の型注釈 module は変更しません。`typing_profiles` のプロファイルは
`.pyi` にだけ存在する型 alias なので、Maya の実行コードから import しません。
`Nodes()` の結果型を選ぶ設定であり、関数引数などの `bd_nodes: bdu.Nodes` は
引き続き全対応 version の共通基底型です。

## プロジェクトごとの上書き

同じ配布を複数プロジェクトで共有する場合は、プロジェクト側の設定を使います。
同梱設定を書き換えた場合は、その配布を参照する全プロジェクトに適用されます。

```text
project-a/
├─ pyrightconfig.json
├─ typings/
│  └─ bd_util_typing_config.pyi
└─ scripts/
   └─ build_rig.py
```

`typings/bd_util_typing_config.pyi` に、プロジェクトで使う型を指定します。
同梱設定と異なり、こちらは利用先からの絶対 import です。

```python
from bd_util.typing_profiles import Maya2026Plus as DefaultNodes

__all__ = ["DefaultNodes"]
```

プロジェクト直下の `pyrightconfig.json` で、その配置先を指定します。

```json
{
    "extraPaths": [
        "D:/path/to/bakedanuki/bakedanuki-util/python"
    ],
    "stubPath": "typings"
}
```

`extraPaths` は実際の配布先へ変更してください。IDE が配布を認識済みなら追加は不要です。
既存の `pyrightconfig.json` や `stubPath` がある場合はその設定を維持し、指定先へ
`bd_util_typing_config.pyi` を追加します。既存の他の stub を削除・置換しません。
設定とファイルをプロジェクトの Git で共有できます。

[プロジェクト用テンプレート](templates/project) に、この二つのファイルを同梱しています。
このテンプレートはコピー元です。プロジェクトへコピーしたファイルを編集してください。

プロジェクトの設定ファイルがなければ同梱設定を使います。変更後は IDE の再解析で
反映し、必要なら Language Server を再起動します。設定は IDE で開いたフォルダー／
ワークスペースに対応し、Maya の Set Project とは連動しません。

## 設定ファイルの保守

同梱の `typing.pyi` は手書きの利用者設定です。stub 生成器は上書きせず、
`--check` の生成内容一致検査にも含めません。配布の更新時には、変更した設定を
引き継いでください。

`python/bd_util_typing_config.pyi` は、プロジェクト側から上書きするための内部入口です。
通常は `bd_util/config/typing.pyi` を取り次ぐだけなので、同梱の入口は編集しません。
`bd_util/typing_profiles.pyi` と `maya/node/nodes.pyi` は生成物です。

version 別の型注釈や内部構成は
[Maya version 対応](../../../docs/maya/node_operator/maya_versions.md) を参照してください。
