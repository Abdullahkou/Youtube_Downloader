from pytube import YouTube
link ='https://www.youtube.com/watch?v=8Z1eMy2FoX4&ab_channel=Arc%27teryx'
video = YouTube(link)
print(f"Titel is:  {video.title}") 

def finish():
    print("Download done Brother!")

video.streams.filter(res="2160p")[0].download(output_path="/Users/Abdul/Desktop")
video.register_on_complete_callback(finish())