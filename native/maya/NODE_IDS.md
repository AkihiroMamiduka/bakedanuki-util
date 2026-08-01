# Maya Node ID Registry

`bakedanuki-util` の C++ ノードで使用する `MTypeId` を管理します。

| Node type | MTypeId | Status |
| --- | --- | --- |
| `bdDbl3MultMulti` | `0x0007F001` | Internal development |
| `bdDbl3Mult` | `0x0007F002` | Internal development |
| `bdDblMultMulti` | `0x0007F003` | Internal development |
| `bdDblMult` | `0x0007F004` | Internal development |
| `bdDbl3AddMulti` | `0x0007F005` | Internal development |
| `bdDbl3Add` | `0x0007F006` | Internal development |
| `bdDblAddMulti` | `0x0007F007` | Internal development |
| `bdDblAdd` | `0x0007F008` | Internal development |
| `bdDbl3SubMulti` | `0x0007F009` | Internal development |
| `bdDbl3Sub` | `0x0007F00A` | Internal development |
| `bdDblSubMulti` | `0x0007F00B` | Internal development |
| `bdDblSub` | `0x0007F00C` | Internal development |
| `bdDbl3DivMulti` | `0x0007F00D` | Internal development |
| `bdDbl3Div` | `0x0007F00E` | Internal development |
| `bdDblDivMulti` | `0x0007F00F` | Internal development |
| `bdDblDiv` | `0x0007F010` | Internal development |
| `bdDbl3PowMulti` | `0x0007F011` | Internal development |
| `bdDbl3Pow` | `0x0007F012` | Internal development |
| `bdDblPowMulti` | `0x0007F013` | Internal development |
| `bdDblPow` | `0x0007F014` | Internal development |
| `bdDblValue` | `0x0007F015` | Internal development |
| `bdDbl3Value` | `0x0007F016` | Internal development |
| `bdDbl3Lerp` | `0x0007F017` | Internal development |
| `bdDblLerp` | `0x0007F018` | Internal development |
| `bdDbl3WtAddMulti` | `0x0007F019` | Internal development |
| `bdDblWtAddMulti` | `0x0007F01A` | Internal development |

現在の ID は `0x00000000` から `0x0007FFFF` までのローカルテスト用範囲です。
この ID のまま永続的な production scene を作成しないでください。

production 利用または配布を始める前に
[Autodesk Maya Developer Network](https://mayaid.autodesk.io/) から固有 ID block
を取得し、この表と実装を更新します。一度 production scene へ保存した `MTypeId`
は、その node type が存続する限り変更しません。
