# imports
import tkinter as tk
from classes.Downloader import Downloader

# Create a window
window = tk.Tk()

# Set the window title
window.title("Internet Download Manager")

# Set the window size
window.geometry("400x300")



# url label and input field
url_entry_label = tk.Label(window, text="URL: ")
url_entry_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# file name label and input field
filename_label = tk.Label(window, text="Save file as: ")
filename_label.pack()
filename_entry = tk.Entry(window, textvariable="Save file as")
filename_entry.pack()

# download function
def download():
    downloader = Downloader(url_entry.get(), filename_entry.get())
    downloader.download_file()

# download button
download_btn = tk.Button(window, text="Download", command=download)
download_btn.pack()


# Run the application
window.mainloop()