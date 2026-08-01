# Maya Node ID Registry

`bakedanuki-util` の C++ ノードで使用する `MTypeId` を管理します。

| Node type | MTypeId | Status |
| --- | --- | --- |
| `bdDouble3MultMulti` | `0x0007F001` | Internal development |
| `bdDouble3Mult` | `0x0007F002` | Internal development |
| `bdDoubleMultMulti` | `0x0007F003` | Internal development |
| `bdDoubleMult` | `0x0007F004` | Internal development |
| `bdDouble3AddMulti` | `0x0007F005` | Internal development |
| `bdDouble3Add` | `0x0007F006` | Internal development |
| `bdDoubleAddMulti` | `0x0007F007` | Internal development |
| `bdDoubleAdd` | `0x0007F008` | Internal development |

現在の ID は `0x00000000` から `0x0007FFFF` までのローカルテスト用範囲です。
この ID のまま永続的な production scene を作成しないでください。

production 利用または配布を始める前に
[Autodesk Maya Developer Network](https://mayaid.autodesk.io/) から固有 ID block
を取得し、この表と実装を更新します。一度 production scene へ保存した `MTypeId`
は、その node type が存続する限り変更しません。
