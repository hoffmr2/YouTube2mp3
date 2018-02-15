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
    string = "Total kB: %d, downloaded kB: %d [%d%s], eta: %d s, rate %d kB/s " % (bytes_in_stream / 1000,
                                                                                   total_bytes_downloaded / 1000,
                                                                                   int(ratio * 100),
                                                                                   '%',
                                                                                   eta,
                                                                                   rate)
    v.set(string)


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
root.geometry("400x80+300+300")

text_url = tk.Text(root, height=1, width=30)
text_url.pack(pady=8)
button_download = tk.Button(root,
                            text="Download",
                            command=download)
button_download.pack(side=tk.RIGHT)
button_download.place(y=5, x=330)

progress = ttk.Progressbar(root, orient="horizontal", length=245, mode="determinate")
progress.pack()

label_url = tk.Label(root, text="url")
label_url.pack()
label_url.place(y=5, x=30)

v = tk.StringVar()
tk.Label(root, textvariable=v).pack()

v.set("Total kB: 0, downloaded kB: 0 [0%], eta: 0s, rate 0 kB/s ")

root.resizable(width=False, height=False)
root.mainloop()
