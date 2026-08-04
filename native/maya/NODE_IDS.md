# Maya Node ID Registry

`bakedanuki-util` の C++ ノードで使用する `MTypeId` を管理します。

| Node type | MTypeId | Status |
| --- | --- | --- |
| `bdDbl3_MultiplyMulti` | `0x0007F001` | Internal development |
| `bdDbl3_Multiply` | `0x0007F002` | Internal development |
| `bdDbl_MultiplyMulti` | `0x0007F003` | Internal development |
| `bdDbl_Multiply` | `0x0007F004` | Internal development |
| `bdDbl3_AddMulti` | `0x0007F005` | Internal development |
| `bdDbl3_Add` | `0x0007F006` | Internal development |
| `bdDbl_AddMulti` | `0x0007F007` | Internal development |
| `bdDbl_Add` | `0x0007F008` | Internal development |
| `bdDbl3_SubtractMulti` | `0x0007F009` | Internal development |
| `bdDbl3_Subtract` | `0x0007F00A` | Internal development |
| `bdDbl_SubtractMulti` | `0x0007F00B` | Internal development |
| `bdDbl_Subtract` | `0x0007F00C` | Internal development |
| `bdDbl3_DivideMulti` | `0x0007F00D` | Internal development |
| `bdDbl3_Divide` | `0x0007F00E` | Internal development |
| `bdDbl_DivideMulti` | `0x0007F00F` | Internal development |
| `bdDbl_Divide` | `0x0007F010` | Internal development |
| `bdDbl3_PowerMulti` | `0x0007F011` | Internal development |
| `bdDbl3_Power` | `0x0007F012` | Internal development |
| `bdDbl_PowerMulti` | `0x0007F013` | Internal development |
| `bdDbl_Power` | `0x0007F014` | Internal development |
| `bdDbl_Value` | `0x0007F015` | Internal development |
| `bdDbl3_Value` | `0x0007F016` | Internal development |
| `bdDbl3_Lerp` | `0x0007F017` | Internal development |
| `bdDbl_Lerp` | `0x0007F018` | Internal development |
| `bdDbl3_WeightedSumMulti` | `0x0007F019` | Internal development |
| `bdDbl_WeightedSumMulti` | `0x0007F01A` | Internal development |
| `bdDbl3_MinMulti` | `0x0007F01B` | Internal development |
| `bdDbl3_Min` | `0x0007F01C` | Internal development |
| `bdDbl_MinMulti` | `0x0007F01D` | Internal development |
| `bdDbl_Min` | `0x0007F01E` | Internal development |
| `bdDbl3_MaxMulti` | `0x0007F01F` | Internal development |
| `bdDbl3_Max` | `0x0007F020` | Internal development |
| `bdDbl_MaxMulti` | `0x0007F021` | Internal development |
| `bdDbl_Max` | `0x0007F022` | Internal development |
| `bdDbl3_Clamp` | `0x0007F023` | Internal development |
| `bdDbl_Clamp` | `0x0007F024` | Internal development |
| `bdDbl3_MapRange` | `0x0007F025` | Internal development |
| `bdDbl_MapRange` | `0x0007F026` | Internal development |
| `bdDbl3_Abs` | `0x0007F027` | Internal development |
| `bdDbl_Abs` | `0x0007F028` | Internal development |
| `bdDbl3_Negate` | `0x0007F029` | Internal development |
| `bdDbl_Negate` | `0x0007F02A` | Internal development |
| `bdDbl3_ConditionMulti` | `0x0007F02B` | Internal development |
| `bdDbl3_Condition` | `0x0007F02C` | Internal development |
| `bdDbl_ConditionMulti` | `0x0007F02D` | Internal development |
| `bdDbl_Condition` | `0x0007F02E` | Internal development |
| `bdDbl3_AverageMulti` | `0x0007F02F` | Internal development |
| `bdDbl3_Average` | `0x0007F030` | Internal development |
| `bdDbl_AverageMulti` | `0x0007F031` | Internal development |
| `bdDbl_Average` | `0x0007F032` | Internal development |
| `bdDbl3_WeightedAverageMulti` | `0x0007F033` | Internal development |
| `bdDbl_WeightedAverageMulti` | `0x0007F034` | Internal development |

現在の ID は `0x00000000` から `0x0007FFFF` までのローカルテスト用範囲です。
この ID のまま永続的な production scene を作成しないでください。

production 利用または配布を始める前に
[Autodesk Maya Developer Network](https://mayaid.autodesk.io/) から固有 ID block
を取得し、この表と実装を更新します。一度 production scene へ保存した `MTypeId`
は、その node type が存続する限り変更しません。
