# t検定ツール
対応の無い2郡のデータでt検定（Welch）とグラフ作成を行います。

## 環境
|package|ver.|
|:--|:--|
|python |3.7.5 |
|numpy |1.18.1 |
|pandas |1.0.1 |
|scipy |1.4.1 |
|matplotlib |3.2.0 |
|seaborn |0.10.0 |

## インストール方法
```
pip install numpy
pip install pandas
pip install scipy
pip install matplotlib
pip install seaborn
```

## 実行方法
1. csvデータを用意
2. `py tTest.py`　もしくは　[ここ](https://github.com/Kahiro-M/TTestByPython/releases)からダウンロードしたexeを実行
3. 生成されたresult.htmlを開く

## 入力データの形式
### ファイル名
- A.csv
- b.csv

### データ構造
A.csvのデータ構造（例）
|No.|ラベル(任意の文字列)|データ(実数)|備考|
|:--|:--|:--|:--|
|1|A_user|A_data|この行は変更不可|
|2|hoge |157.9 |
|3|hogehoge |158 |
|4|hogehogehoge |158.1 |
|5... |...|...|

B.csvのデータ構造（例）
|No.|ラベル(任意の文字列)|データ(実数)|備考|
|:--|:--|:--|:--|
|1|B_user|B_data|この行は変更不可|
|2|fuga |170.7 |
|3|fugafuga |170.8 |
|4|fugafugafuga |170.9 |
|5... |...|...|