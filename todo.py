from pytube import YouTube
from tqdm import tqdm

def descargar_video():
    url = input("Ingrese el link del video: ")
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
#MUY FACIL DEBES DE TENER DESCARGADO pytube
#Instalar pytube pip install pytube
#actualizar pytube pip install --upgrade pytube
    print("Video descargado con éxito.")

def descargar_audio():
    url = input("Ingrese el link del video: ")
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename='audio_mp3.mp3')

    print("Audio descargado con éxito.")

opcion = int(input("1. Descargar video\n2. Descargar audio\n"))
if opcion == 1:
    descargar_video()
elif opcion == 2:
    descargar_audio()
else:
    print("Opción inválida.")
