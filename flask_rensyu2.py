# s24008
# flask_rensyu.py
# Flaskの練習 Hello Worldを出力する

# 事前にflaskモジュールをインストールすると使える
# render_templateはhtmlファイルを扱う際必要
from flask import Flask, render_template

# Flaskライブラリをインスタンス化し、app変数に割り当て
# その際、コンストラクタへの引数は実行中のモジュールを指定する
app = Flask(__name__)

# ルートURLに対するリクエストを処理する関数を定義するデコレーター
# 引数にルート'/'を指定するとアクセスした際index()関数がが呼び出される
@app.route('/')
def index():
    return "<h1>hello world</h1>"

@app.route("/himitu")
def himitu():
    return render_template("himitu.htmml")

if __name__=='__main__':
    app.run(debug=True)
