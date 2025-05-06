
# YouTube Downloader com FFmpeg (yt-dlp + verificação automática)

Este projeto é uma aplicação Python simples que permite baixar vídeos ou áudios do YouTube (ou outros sites suportados) no formato **MP3** ou **MP4** diretamente pelo terminal, utilizando as bibliotecas **yt-dlp** e **FFmpeg**.

O diferencial é que o programa **verifica automaticamente se o FFmpeg está instalado** no sistema. Caso não esteja, ele faz o **download, extrai e configura** o FFmpeg para uso, incluindo a adição ao PATH (temporária ou permanente, dependendo do sistema operacional).

## 📝 Funcionalidades

- Download de **áudio em MP3** com qualidade máxima disponível.
- Download de **vídeo em MP4** com melhor qualidade de vídeo e áudio combinados.
- Suporte para **links individuais ou playlists inteiras**.
- Interface de terminal simples, com seleção interativa.
- Verificação automática do FFmpeg: download, extração e configuração sem necessidade de instalação manual.
- Compatível com Windows, Linux e macOS.

## 🚀 Como utilizar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Execute o programa:
   ```bash
   python main.py
   ```

4. Siga as instruções no terminal para escolher o tipo de download e a pasta de destino.

---

## ⚠️ Aviso importante

> Este projeto foi desenvolvido **exclusivamente para fins educacionais e de uso pessoal**.
> 
> O autor **não endossa ou incentiva o download de conteúdos protegidos por direitos autorais ou a violação dos Termos de Serviço de plataformas como o YouTube**.
> 
> **O uso deste código para finalidades que infrinjam direitos autorais ou políticas de uso de terceiros é de inteira responsabilidade do usuário.**
> 
> Lembre-se: sempre respeite os direitos dos criadores de conteúdo e as leis de sua região.

---

## 📚 Tecnologias utilizadas

- Python 3.x
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)
- requests
- zipfile
- subprocess
- tkinter (para seleção da pasta)

---

## 🖋️ Licença

Este projeto está licenciado sob a **Licença MIT**. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou **pull requests** com melhorias, correções ou sugestões.
