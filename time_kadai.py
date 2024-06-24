# s24008
# importを駆使して現在の時間を表示する
# 実行が確認出来たら時間を表示させる「時計アプリ」を作ってみます
# 時計アプリはモジュール名「time_katai.py」で作成します
# 時計アプリを使いやすくバージョンアップしていきます

import datetime
import tkinter as tk # GUIでアプリを作ることができる

# 時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime(now.strftime("%Y年%m月%d日 %H時%M分%S秒"))
    lbl.config(text=current_time)
    root.after(1000, update_time)

# Tkinterのウインドウを作成
root = tk.Tk()　# 初めのおまじない

root.title("時計アプリ")
# ラベルとテキストボックスを作成する
lbl = tk.Label()
lbl.config(text="", font=("Helvetica", 20))
lbl.pack()

# 関数からの呼び出し
update_time()

root.mainloop()

