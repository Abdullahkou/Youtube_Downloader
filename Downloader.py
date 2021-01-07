from pytube import YouTube
""" link ='https://www.youtube.com/watch?v=8Z1eMy2FoX4&ab_channel=Arc%27teryx' """  """ pyinstaller --onefile 'Downloader.py'  """
link = input("video-Url eingeben: ")
video = YouTube(link)
print(f"Titel ist:  {video.title}") 

def finish():
    print("Download done Brother!")

video.streams.get_highest_resolution().download(output_path="D:\Youtube_Videos_Downloader")
video.register_on_complete_callback(finish())