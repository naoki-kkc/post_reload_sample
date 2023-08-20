# post reload sample

## 概要
リロードした時の挙動を確認するためのflaskアプリケーション。

## 注意事項
macOS 12.6.8 で作成/実行しているため、Windows部分は未確認。

## 実行環境
- Python 3.10.6
- ライブラリはrequirements.txt参照

## 実行結果確認済み
- Safari 16.6
- Google Chrome 116.0.5845.96

## 実行手順

1. venvで仮想環境を構築

```
python -m venv %仮想環境名%
```

2. 仮想環境をアクティベート

```
# Windows
%仮想環境名%¥Scripts¥activate.bat

# macOS/Linux
source %仮想環境名%/bin/activate
```

3. requirements.txtの内容をインストール

```
pip install -r requirements.txt
```

4. サーバー起動用バッチファイルを実行

```
# Windows
run_server.bat

# macOS/Linux
% chmod 755 run_server.sh
% ./run_server.sh
```

5. サーバー起動メッセージのURLをブラウザで開く

下記例であれば「 http://127.0.0.1:5000 」
```
(env_fgp) naokikkc@MacBookAir flask_getpost % ./run_server.sh 
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

## ブラウザ
