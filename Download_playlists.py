from pytube import Playlist
playlist_link ='https://www.youtube.com/playlist?list=PLLCK2gut59nikMcUGxb8K_VeU-_bam5sm'
playlist = Playlist(playlist_link)

print(f"Titel is:  {playlist.title}") 

def finish():
    print("Download done Brother!")

for video in playlist.videos:
    video.streams.get_highest_resolution().download(output_path="D:\Youtube_Downloader_videos\D2")
    print(video.title)
    

finish()