import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((200, 300))
    imageDate = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageDate)
    imageLabel.image = imageDate

def openFile():
    fpath = fd.asdopenfilename()
    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Brtton(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()

tk.mainloop()

