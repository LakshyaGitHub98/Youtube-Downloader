from pytube import YouTube
print("Welcome to Audio Downloader of youtube videos :)")
link = input("Paste the link of the video :")
auido = YouTube(link)
highest_resolution_stream = auido.streams.get_audio_only()
highest_resolution_stream.download()