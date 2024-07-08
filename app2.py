# app2.py バージョン2


import tkinter as tk # tkinterをimportしてtkと略して使う

def dispLabel():
    lbl.config(text="こんにちは")

root = tk.Tk()
root.geometry("400x200") # 画面の大きさを決める


lbl = tk.Label(text="LABEL", font=("Helvetica", 20)) # ラベルを作る
btn = tk.Button(text="PUSH", command=dispLabel, font=("Helvetica", 20)) # ボタンを作る


lbl.pack() # 画面にラベルを配置する
btn.pack() #画面にボタンを配置する

lbl2 = tk.Label(text="ラベル2", font=("Helvetica", 20)).pack()

btn2 = tk.Button (text="何もしないボタン", command=dispLabel, font=("Helvetica")).pack()
tk.mainloop().pack # 作ったウインドウを表示する
