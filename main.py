from tkinter.filedialog import askdirectory
from FFmpegVerify import FFmpegVerify
from yt_dlp import YoutubeDL


class Main:

    @staticmethod
    def download_mp3():
        FFmpegVerify()
        url = input("\nDigite a URL: ")
        print("")
        folder = askdirectory(title="Select a folder")

        ydl_opts = {

            'format': 'bestaudio/best',
            'extract_audio': True,
            'outtmpl': f'{folder}/%(title)s.mp3',
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)

    @staticmethod
    def download_mp4():
        FFmpegVerify()
        url = input("\nDigite a URL: ")
        print("")
        folder = askdirectory(title="Select a folder")

        ydl_opts = {

            'format': 'bestvideo+bestaudio',
            'outtmpl': f'{folder}/%(title)s.mp4',
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)



if __name__ == "__main__":

    while True:

        options = eval(input(
        """
        Escolha uma opção:

        [0] Sair
        [1] Baixar em mp3
        [2] Baixar em mp4

        Obs.: Caso o vídeo esteja em uma pleylist, será baixado todos os vídeos.

        Digite a opção escolhida: """))

        try:
    
            if options == 0: break
            if options == 1: Main.download_mp3()
            if options == 2: Main.download_mp4()

        except: break