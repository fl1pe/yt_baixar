import os
import yt_dlp as youtube_dl

def criar_pasta_videos():
    # Cria a pasta "videos" se ela não existir
    if not os.path.exists("videos"):
        os.makedirs("videos")

def truncar_nome(nome, max_length=50):
    # Trunca o nome do arquivo se for maior que o limite
    return nome if len(nome) <= max_length else nome[:max_length]

def download_video_from_x(url):
    ydl_opts = {
        'outtmpl': 'videos/%(title).50s.%(ext)s',  # Limita o nome do arquivo a 50 caracteres
        'format': 'bestvideo+bestaudio/best',  # Melhor qualidade disponível
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Converte para MP4
        }],
        'cookiefile': 'cookies.txt',  # Arquivo de cookies no formato Netscape
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Baixa o vídeo da URL
            print(f"Download do vídeo concluído e salvo na pasta 'videos'.")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

def main():
    criar_pasta_videos()  # Cria a pasta "videos" ao iniciar o programa

    while True:
        url = input("Digite a URL do vídeo do X (ou 'sair' para encerrar): ")
        
        # Permite que o usuário encerre o loop
        if url.lower() == "sair":
            print("Encerrando o programa.")
            break

        # Verifica se a URL é válida e segue o padrão do X (antigo Twitter)
        if not url.startswith("https://x.com/") or "/status/" not in url:
            print("A URL fornecida não é válida ou não segue o padrão do X. Tente novamente.")
            continue
        
        download_video_from_x(url)

if __name__ == "__main__":
    main()
