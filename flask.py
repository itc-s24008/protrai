# s24008
# Flaskの練習

# 事前にflaskモジュールをインストールすると使える
from flask import Flask

# Flaskライブラリをインスタンス化し、app変数に割り当て
# その際、コンストラクタへの引数は実行中のモジュールを指定する
app = Flask(__name__)

# ルートURLに対するリクエストを処理する関数を定義するデコレーター
# 引数にルート'/'を指定するとアクセスした際index()関数がが呼び出される
app.ruote('/')
def index():
    return "<h1>hello world<h1>"

if __name__=='__main__'
    app.run(debug=True)
