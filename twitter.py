import os
import yt_dlp as youtube_dl

def criar_pasta_videos():
    if not os.path.exists("videos"):
        os.makedirs("videos")

def truncar_nome(nome, max_length=50):
    return nome if len(nome) <= max_length else nome[:max_length]

def limpar_arquivos_part(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.part') or 'Frag' in arquivo:
            os.remove(os.path.join(pasta, arquivo))
            print(f"Arquivo incompleto removido: {arquivo}")

def download_video_from_x(url):
    ydl_opts = {
        'outtmpl': 'videos/%(title).50s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'cookiefile': 'cookies.txt',
        'continue': True,  # Habilita a retomada de downloads
        'noprogress': False,  # Mostra o progresso do download
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Download do vídeo concluído e salvo na pasta 'videos'.")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

def baixar_videos_de_txt(caminho_txt):
    urls_baixadas = set()

    try:
        with open(caminho_txt, 'r') as file:
            urls = file.readlines()

        for url in urls:
            url = url.strip()
            if url and url not in urls_baixadas:
                print(f"Baixando vídeo da URL: {url}")
                download_video_from_x(url)
                urls_baixadas.add(url)
            elif url in urls_baixadas:
                print(f"URL duplicada encontrada e ignorada: {url}")

        limpar_arquivos_part("videos")  # Limpa arquivos .part após o download

    except Exception as e:
        print(f"Erro ao ler o arquivo .txt: {e}")

def main():
    criar_pasta_videos()

    caminho_txt = input("Digite o caminho do arquivo .txt com as URLs: ")
    
    if os.path.exists(caminho_txt):
        baixar_videos_de_txt(caminho_txt)
    else:
        print("Arquivo .txt não encontrado. Verifique o caminho e tente novamente.")

if __name__ == "__main__":
    main()

