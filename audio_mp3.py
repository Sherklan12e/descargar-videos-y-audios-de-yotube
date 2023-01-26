from pytube import YouTube

url = "https://www.youtube.com/watch?v=mLmOEdCgZPA"
yt = YouTube(url)
audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download(filename='audio_mp3.mp3')
