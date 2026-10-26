# 補完設定とパッケージの標準値

このディレクトリには、パッケージの標準値・コピー用テンプレート・設定手順をまとめます。
利用者が編集する設定は、更新時に置き換える配布フォルダーの外へ保存します。
同梱ファイルはパッケージ更新の対象なので、通常は外部設定から補完対象を選んでください。

Maya preferences 内の UI 設定・保存データは、従来の保存先を使います。

## 外部設定を用意する

`typing_maya_version` を省略した `bdu.Nodes()` の補完対象は、外部の
`bd_util_typing_config.pyi` で指定します。プロジェクト用の配置例です。

```text
project-a/
├─ pyrightconfig.json
├─ config/
│  └─ bakedanuki/
│     └─ typings/
│        └─ bd_util_typing_config.pyi
└─ scripts/
   └─ build_rig.py
```

1. [プロジェクト用テンプレート](templates/project) のファイルを、利用先へコピーします。
   既存の `pyrightconfig.json` がある場合は上書きせず、必要な設定を追加します。
2. コピー先の `bd_util_typing_config.pyi` で、使うプロファイルを選びます。
3. `pyrightconfig.json` で、IDE が参照する配置先を指定します。

テンプレートは、正式対応済みの Maya 2026 以降で共通する補完を使う例です。

```python
from bd_util.typing_profiles import Maya2026Plus as DefaultNodes

__all__ = ["DefaultNodes"]
```

Maya 2026 だけを対象にする場合は `Maya2026`、2025 以降の共通部分なら
`Maya2025Plus` へ変更します。有効にする import は一つにし、`DefaultNodes` という名前と
`__all__ = ["DefaultNodes"]` を維持してください。

プロジェクト直下の `pyrightconfig.json` の例です。

```json
{
    "extraPaths": [
        "D:/path/to/bakedanuki/bakedanuki-util/python"
    ],
    "stubPath": "config/bakedanuki/typings"
}
```

`extraPaths` は実際の配布先へ変更してください。IDE が配布を認識済みなら追加は不要です。
`stubPath` の相対パスは `pyrightconfig.json` の場所を基準にします。
既存の `stubPath` がある場合はその配置先を維持し、そこへ
`bd_util_typing_config.pyi` を追加します。既存の他の stub は保持してください。
コピー元のテンプレートではなく、配布外のコピー先を編集します。

設定ファイルと `pyrightconfig.json` をプロジェクトの Git で共有できます。
配布をプロジェクト内の `vendor/bakedanuki` などへ置く場合も、利用者設定はその外に置き、
更新では配布フォルダーだけを置き換えます。

変更後は IDE の再解析で反映し、必要なら Language Server を再起動します。
設定は IDE で開いたフォルダー／ワークスペースに対応し、Maya の Set Project とは連動しません。

## 個人用の共通設定

複数プロジェクトで同じ設定を使う場合は、配布外の個人用フォルダーへ設定ファイルを
置くこともできます。

```text
D:/bakedanuki-user/config/typings/bd_util_typing_config.pyi
```

そのファイルを参照する各ワークスペースで、配置先を指定します。

```json
{
    "stubPath": "D:/bakedanuki-user/config/typings"
}
```

選んだフォルダーを参照するプロジェクトは、同じ補完設定を使います。
`stubPath` は一つのディレクトリを指定する設定です。プロジェクト用と個人用の設定を
自動的に多段探索・マージする仕組みではありません。既存の `stubPath` を使う場合は、
そのディレクトリへ設定ファイルを追加してください。

## プロファイルと優先順位

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
2. IDE の `stubPath` で参照する外部の `bd_util_typing_config.pyi`。
3. 外部設定がない場合のパッケージ標準値 `Maya2025Plus`。

省略と明示的な `None` は同じ設定を使います。共通補完を明示したい場合は、
`bdu.Nodes(typing_maya_version="2025+")` と指定できます。

この設定は IDE が読む型情報です。Maya の実行バージョン、利用可能なノード、
`bdu.node_types` の型注釈 module は変更しません。`typing_profiles` のプロファイルは
`.pyi` にだけ存在する型 alias なので、Maya の実行コードから import しません。
`Nodes()` の結果型を選ぶ設定であり、関数引数などの `bd_nodes: bdu.Nodes` は
引き続き全対応 version の共通基底型です。

## 同梱設定を編集済みの場合

配布を置き換える前に、選択したプロファイルを外部設定へ移してください。

1. 前述の手順で、配布外に `bd_util_typing_config.pyi` を用意します。
2. 同梱の `typing.pyi` で選んでいたプロファイルを、そのファイルへ指定します。
   外部設定の import は `from bd_util.typing_profiles import ...` と記します。
3. IDE の `stubPath` で外部設定を参照し、補完対象を確認します。

以後は外部設定を保持したまま配布を更新できます。
同梱の `typing.pyi` を引き続き直接編集した場合は、配布の置き換えで変更内容も
上書きされるため、更新前に外部へ保存してください。

## 配布側のファイル

`bd_util/config/typing.pyi` は、外部設定がない場合の標準値を定義します。
`python/bd_util_typing_config.pyi` は、標準値を取り次ぐ内部入口です。
これらはパッケージ側が管理し、通常の利用では外部設定から補完対象を指定します。

標準値とテンプレートは手書きで管理し、stub 生成器による上書きや `--check` の
生成内容一致検査には含めません。生成時に保持されることと、配布フォルダーを
丸ごと置き換えたときに保持されることは別です。
`bd_util/typing_profiles.pyi` と `maya/node/nodes.pyi` は生成物です。

version 別の型注釈や内部構成は
[Maya version 対応](../../../docs/maya/node_operator/maya_versions.md) を参照してください。
