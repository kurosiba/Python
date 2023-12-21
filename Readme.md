# pythonの勉強

## コーディング規則
クラス:upper
関数、メソッド、変数:rower & snake
定数:uppper & snake


## 二重アンダースコア変数について
**概要**：python実行時に自動で定義・初期化される変数のこと。
- 形式は__(name, all, author, version)__

### __name__について
 - 実行するスクリプトの__name__
 ⇒__main__が入ってる
 - importしてきたスクリプトの__name__
 ⇒import元のファイル名(拡張子は除く)

### if __name__==__main__:について
- おまじない
- 実行しているスクリプトの__name__が__main__としてなっていることを確認する

⇒実行しているファイルがmainだよねっていうことを担保している