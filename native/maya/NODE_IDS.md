# Maya Node ID Registry

`bakedanuki-util` の C++ ノードで使用する `MTypeId` を管理します。

| Node type | MTypeId | Status |
| --- | --- | --- |
| `bdMultDouble3Multi` | `0x0007F001` | Internal development |
| `bdMultDouble3Pair` | `0x0007F002` | Internal development |
| `bdMultDoubleMulti` | `0x0007F003` | Internal development |
| `bdMultDoublePair` | `0x0007F004` | Internal development |
| `bdAddDouble3Multi` | `0x0007F005` | Internal development |
| `bdAddDouble3Pair` | `0x0007F006` | Internal development |
| `bdAddDoubleMulti` | `0x0007F007` | Internal development |
| `bdAddDoublePair` | `0x0007F008` | Internal development |
| `bdSubDouble3Multi` | `0x0007F009` | Internal development |
| `bdSubDouble3Pair` | `0x0007F00A` | Internal development |
| `bdSubDoubleMulti` | `0x0007F00B` | Internal development |
| `bdSubDoublePair` | `0x0007F00C` | Internal development |
| `bdDivDouble3Multi` | `0x0007F00D` | Internal development |
| `bdDivDouble3Pair` | `0x0007F00E` | Internal development |
| `bdDivDoubleMulti` | `0x0007F00F` | Internal development |
| `bdDivDoublePair` | `0x0007F010` | Internal development |
| `bdPowDouble3Multi` | `0x0007F011` | Internal development |
| `bdPowDouble3Pair` | `0x0007F012` | Internal development |
| `bdPowDoubleMulti` | `0x0007F013` | Internal development |
| `bdPowDoublePair` | `0x0007F014` | Internal development |
| `bdDoubleValue` | `0x0007F015` | Internal development |
| `bdDouble3Value` | `0x0007F016` | Internal development |
| `bdLerpDouble3Pair` | `0x0007F017` | Internal development |
| `bdLerpDoublePair` | `0x0007F018` | Internal development |
| `bdWtAddDouble3Multi` | `0x0007F019` | Internal development |
| `bdWtAddDoubleMulti` | `0x0007F01A` | Internal development |

現在の ID は `0x00000000` から `0x0007FFFF` までのローカルテスト用範囲です。
この ID のまま永続的な production scene を作成しないでください。

production 利用または配布を始める前に
[Autodesk Maya Developer Network](https://mayaid.autodesk.io/) から固有 ID block
を取得し、この表と実装を更新します。一度 production scene へ保存した `MTypeId`
は、その node type が存続する限り変更しません。
