from pytube import Playlist
import validators

def is_youtube_url(url):
    # Verifica se a URL é válida e se é do YouTube
    return validators.url(url) and "youtube.com" in url

def get_video_urls_from_playlist(playlist_url):
    # Cria um objeto Playlist a partir da URL fornecida
    playlist = Playlist(playlist_url)
    # Retorna uma lista de URLs de vídeos na playlist
    return playlist.video_urls

def main():
    while True:
        url = input("Digite a URL da playlist do YouTube: ")
        
        if not is_youtube_url(url):
            print("A URL fornecida não é válida ou não é do YouTube. Tente novamente.")
            continue
        
        try:
            video_urls = get_video_urls_from_playlist(url)
        except Exception as e:
            print(f"Erro ao acessar a playlist: {e}")
            continue
        
        # Salva as URLs em um arquivo .txt
        with open("video_urls.txt", "w") as file:
            for video_url in video_urls:
                file.write(video_url + "\n")
        
        print("As URLs dos vídeos foram salvas em video_urls.txt")
        break

if __name__ == "__main__":
    main()
