import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
import threading

def convert_mp4_to_gif():
    mp4_file_path = filedialog.askopenfilename(title="選擇 MP4 文件", filetypes=[("MP4 files", "*.mp4")])
    if not mp4_file_path:
        return

    gif_file_path = mp4_file_path.rsplit('.', 1)[0] + ".gif"

    threading.Thread(target=perform_conversion, args=(mp4_file_path, gif_file_path)).start()

def perform_conversion(mp4_file_path, gif_file_path):
    try:
        with VideoFileClip(mp4_file_path) as video:
            video.write_gif(gif_file_path)

        messagebox.showinfo("完成", f"轉換完成！GIF 文件保存在：\n{gif_file_path}")
    except Exception as e:
        messagebox.showerror("錯誤", f"轉換過程中出現錯誤：\n{str(e)}")

root = tk.Tk()
root.title("MP4 轉 GIF 工具")

convert_button = tk.Button(root, text="選擇 MP4 並轉換為 GIF", command=convert_mp4_to_gif)
convert_button.pack(pady=20)

root.mainloop()
