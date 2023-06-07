import tkinter as tk

# Create a window
window = tk.Tk()

# Set the window title
window.title("Internet Download Manager")

# Set the window size
window.geometry("400x300")

# download function
def download():
    print("hey")

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

# download button
download_btn = tk.Button(window, text="Download", command=download)
download_btn.pack()


# Run the application
window.mainloop()