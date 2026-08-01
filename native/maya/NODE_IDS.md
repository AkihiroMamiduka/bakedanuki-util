# Maya Node ID Registry

`bakedanuki-util` の C++ ノードで使用する `MTypeId` を管理します。

| Node type | MTypeId | Status |
| --- | --- | --- |
| `bdDbl3_MultMulti` | `0x0007F001` | Internal development |
| `bdDbl3_Mult` | `0x0007F002` | Internal development |
| `bdDbl_MultMulti` | `0x0007F003` | Internal development |
| `bdDbl_Mult` | `0x0007F004` | Internal development |
| `bdDbl3_AddMulti` | `0x0007F005` | Internal development |
| `bdDbl3_Add` | `0x0007F006` | Internal development |
| `bdDbl_AddMulti` | `0x0007F007` | Internal development |
| `bdDbl_Add` | `0x0007F008` | Internal development |
| `bdDbl3_SubMulti` | `0x0007F009` | Internal development |
| `bdDbl3_Sub` | `0x0007F00A` | Internal development |
| `bdDbl_SubMulti` | `0x0007F00B` | Internal development |
| `bdDbl_Sub` | `0x0007F00C` | Internal development |
| `bdDbl3_DivMulti` | `0x0007F00D` | Internal development |
| `bdDbl3_Div` | `0x0007F00E` | Internal development |
| `bdDbl_DivMulti` | `0x0007F00F` | Internal development |
| `bdDbl_Div` | `0x0007F010` | Internal development |
| `bdDbl3_PowMulti` | `0x0007F011` | Internal development |
| `bdDbl3_Pow` | `0x0007F012` | Internal development |
| `bdDbl_PowMulti` | `0x0007F013` | Internal development |
| `bdDbl_Pow` | `0x0007F014` | Internal development |
| `bdDbl_Value` | `0x0007F015` | Internal development |
| `bdDbl3_Value` | `0x0007F016` | Internal development |
| `bdDbl3_Lerp` | `0x0007F017` | Internal development |
| `bdDbl_Lerp` | `0x0007F018` | Internal development |
| `bdDbl3_WtAddMulti` | `0x0007F019` | Internal development |
| `bdDbl_WtAddMulti` | `0x0007F01A` | Internal development |

現在の ID は `0x00000000` から `0x0007FFFF` までのローカルテスト用範囲です。
この ID のまま永続的な production scene を作成しないでください。

production 利用または配布を始める前に
[Autodesk Maya Developer Network](https://mayaid.autodesk.io/) から固有 ID block
を取得し、この表と実装を更新します。一度 production scene へ保存した `MTypeId`
は、その node type が存続する限り変更しません。
