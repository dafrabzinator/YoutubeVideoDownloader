import tkinter as tk
from tkinter import ttk
import pytube

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.url_label = ttk.Label(self, text="YouTube Video URL:")
        self.url_label.pack()

        self.url_entry = ttk.Entry(self)
        self.url_entry.pack()

        self.download_button = ttk.Button(self, text="Download", command=self.download_video)
        self.download_button.pack()

    def download_video(self):
        url = self.url_entry.get()
        path = "E:/"
        filename = pytube.YouTube(url).title
        stream = pytube.YouTube(url).streams.get_highest_resolution()
        stream.download(path, filename=filename)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
