from pytube import YouTube
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def download_video(url, output_path='./'):
    try:
        video_id_match = re.match(r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)', url)
        if video_id_match:
            video_id = video_id_match.group(1)
            yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
            video = yt.streams.filter(file_extension='mp4').first()
            if video:
                video.download(output_path)
                return f"Downloaded: {yt.title}"
            else:
                return "No MP4 video format available for download."
        else:
            return "Invalid YouTube URL format. Please provide a valid URL."
    except Exception as e:
        return f"Error downloading video: {str(e)}"

def download_button_action():
    url = url_entry.get()
    output_path = filedialog.askdirectory()
    if output_path:
        result = download_video(url, output_path)
        messagebox.showinfo("Download Status", result)

def main():
    root = tk.Tk()
    root.title("YouTube Video Downloader")
    root.state('zoomed')
    
    frame = tk.Frame(root)
    frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
    
    tk.Label(frame, text="YouTube Video URL:", font=('Helvetica', 18)).pack(pady=10)
    
    global url_entry
    url_entry = tk.Entry(frame, width=50, font=('Helvetica', 16))
    url_entry.pack(pady=5)
    
    download_button = tk.Button(frame, text="Download", command=download_button_action, font=('Helvetica', 16))
    download_button.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()
