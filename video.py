from pytube import YouTube
print("URL")
url = (input(""))
yt = YouTube(url)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
#MUY FACIL DEBES DE TENER DESCARGADO pytube
#Instalar pytube pip install pytube
#actualizar pytube pip install --upgrade pytube