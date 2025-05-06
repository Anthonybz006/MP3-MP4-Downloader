import subprocess
import requests
import zipfile
import shutil
import sys
import os

class FFmpegVerify:
    def __init__(self):
        """
        Inicializa a verificação do FFmpeg:
        - Verifica se o FFmpeg já está instalado
        - Caso não esteja, faz o download, extrai e adiciona ao PATH
        - Testa a instalação
        """
        # Garante que a pasta ./extensions/ existe
        os.makedirs("./extensions/", exist_ok=True)

        if not self.verify():  # Verifica se FFmpeg já está no sistema
            if not os.path.exists("./extensions/ffmpeg.zip"):
                self.download_ffmpeg()  # Baixa se o arquivo zip ainda não existe
            if not os.path.exists("./extensions/ffmpeg_folder"):
                self.unpack()  # Extrai se a pasta ainda não foi criada
            bin_path = self.find_bin_path()  # Localiza o diretório binário (executáveis)
            self.add_to_path(bin_path)  # Adiciona ao PATH permanentemente
            os.environ["PATH"] += os.pathsep + bin_path  # Adiciona ao PATH da sessão atual

            # Se FFmpeg ainda não for encontrado no PATH, usa o caminho completo do bin
            ffmpeg_exec = os.path.join(bin_path, "ffmpeg.exe" if sys.platform == "win32" else "ffmpeg")
            self.test_ffmpeg(ffmpeg_exec)
        else:
            self.test_ffmpeg("ffmpeg")  # Já estava no PATH, pode chamar normalmente

    @staticmethod
    def verify():
        """
        Verifica se o FFmpeg já está disponível no PATH do sistema.
        Retorna True se encontrado, False caso contrário.
        """
        if shutil.which("ffmpeg") is None:
            print("FFmpeg não encontrado. Precisamos baixar!")
            return False
        else:
            print("FFmpeg já está instalado.")
            return True

    @staticmethod
    def download_ffmpeg():
        """
        Faz o download do arquivo ZIP com os binários do FFmpeg
        de uma fonte confiável.
        """
        ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        output_path = "./extensions/ffmpeg.zip"

        try:
            response = requests.get(ffmpeg_url, stream=True)
            response.raise_for_status()  # Lança erro caso o download falhe
            with open(output_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print("Download concluído!")
        except requests.RequestException as e:
            print(f"Erro ao baixar FFmpeg: {e}")
            sys.exit(1)

    @staticmethod
    def unpack():
        """
        Extrai o conteúdo do arquivo ZIP para uma pasta chamada 'ffmpeg_folder'.
        """
        zip_path = "./extensions/ffmpeg.zip"
        extract_to = "./extensions/ffmpeg_folder"

        try:
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(extract_to)
            print("Arquivos extraídos!")
        except zipfile.BadZipFile:
            print("Erro: Arquivo ZIP corrompido.")
            sys.exit(1)

    @staticmethod
    def find_bin_path():
        """
        Localiza a pasta 'bin' dentro da estrutura extraída do ZIP.
        Retorna o caminho absoluto da pasta bin.
        """
        extract_to = os.path.abspath("./extensions/ffmpeg_folder")
        for root, dirs, files in os.walk(extract_to):
            if 'bin' in dirs:
                bin_path = os.path.join(root, 'bin')
                print(f"Pasta bin encontrada em: {bin_path}")
                return bin_path
        # Se não encontrar a pasta bin, aborta o programa
        print("Não foi possível encontrar a pasta 'bin' do FFmpeg.")
        sys.exit(1)

    @staticmethod
    def add_to_path(bin_path):
        """
        Adiciona o caminho da pasta bin ao PATH do sistema.
        No Windows: usa 'setx' para persistir em novas sessões.
        No Unix/Linux/Mac: adiciona export ao arquivo de configuração do shell.
        """
        if sys.platform == "win32":
            # Atenção: setx PATH tem limite de 1024 caracteres!
            subprocess.run(['setx', 'PATH', f'%PATH%;{bin_path}'], shell=True)
            print("FFmpeg adicionado ao PATH. Feche e abra o terminal novamente para aplicar as mudanças.")
        else:
            # Tenta detectar o arquivo de configuração do shell
            shell_files = ['~/.bashrc', '~/.bash_profile', '~/.zshrc']
            bash_profile = None
            for file in shell_files:
                path = os.path.expanduser(file)
                if os.path.exists(path):
                    bash_profile = path
                    break
            if not bash_profile:
                bash_profile = os.path.expanduser('~/.bashrc')

            export_line = f'\nexport PATH="$PATH:{bin_path}"\n'
            with open(bash_profile, "a") as file:
                file.write(export_line)
            print(f"FFmpeg foi adicionado ao PATH em {bash_profile}! Reinicie o terminal para aplicar as alterações.")

    @staticmethod
    def test_ffmpeg(ffmpeg_command):
        """
        Executa o comando 'ffmpeg -version' para testar se o FFmpeg está funcional.
        Aceita o nome 'ffmpeg' (se já estiver no PATH) ou caminho completo.
        """
        try:
            result = subprocess.run([ffmpeg_command, "-version"], capture_output=True, text=True, check=True)
            print("FFmpeg instalado com sucesso!")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Erro ao executar FFmpeg:")
            print(e.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Erro ao testar FFmpeg: {e}")
            sys.exit(1)

if __name__ == "__main__":
    FFmpegVerify()
