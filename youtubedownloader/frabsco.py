import pytube
import tkinter as tk

def start_download():
    url = entry.get()
    path = "E"

    yt = pytube.YouTube(url)
    stream = yt.streams.get_highest_resolution()

    filename = yt.title + "." + stream.subtype

    stream.download(path, filename=filename)

    label["text"] = "Download complete"

root = tk.Tk()
root.title("YouTube Downloader")

label = tk.Label(root, text="Enter the video URL:")
entry = tk.Entry(root)
button = tk.Button(root, text="Download", command=start_download)

label.pack()
entry.pack()
button.pack()

root.mainloop()
