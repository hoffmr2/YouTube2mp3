import tkinter as tk
from youTube2mp3 import YouTube2mp3
from tkinter import filedialog
from tkinter import ttk
import threading


def listen_for_result():

    if downloading_end[0]:
        text_url.configure(state="normal")
        button_download.configure(state="normal")
        progress["value"] = 0
    else:
        root.after(100, listen_for_result)


def downloadinginfo(bytes_in_stream,
                    total_bytes_downloaded,
                    ratio,
                    rate,
                    eta):
    progress["maximum"] = bytes_in_stream
    progress["value"] = total_bytes_downloaded


def download():

    yt2mp3 = YouTube2mp3()
    f = filedialog.asksaveasfile(mode='w', defaultextension=".mp3")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    destination = f.name
    f.close()
    text_url.configure(state="disabled")
    button_download.configure(state="disabled")
    t = threading.Thread(target=yt2mp3.download, args=(text_url.get("1.0", "end-1c"),
                                                       destination,
                                                       320,
                                                       downloadinginfo,
                                                       downloading_end))
    downloading_end[0] = False
    root.after(100, listen_for_result)
    t.start()


downloading_end = [False]
root = tk.Tk()
root.title("YouTube2mp3")
root.geometry("400x200+300+300")

text_url = tk.Text(root, height=1, width=30)
text_url.pack(pady=8)
button_download = tk.Button(root,
                            text="Download",
                            command=download)
button_download.place(y=5, x=330)

progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack()

root.mainloop()
