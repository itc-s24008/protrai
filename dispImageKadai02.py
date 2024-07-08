# 24008
# dispImageKadai01.py
# 画像を画面に出力する


import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).convert("L").rotate(90).transpose(PIL.Image.FLIP_LEFT_RIGHT).resize((300, 300))
    imageDate = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageDate)
    imageLabel.image = imageDate

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)
        lbl3 = tk.Label(text=fpath)
        lbl3.pack()

root = tk.Tk()
root.geometry("400x350")
lbl2 = tk.Label(text="🎨画像表示アプリ バージョン2.0🎨")
btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
lbl2.pack()
btn.pack()
imageLabel.pack()

tk.mainloop()

