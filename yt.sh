#!/bin/bash

# URL da playlist do YouTube
echo "Link da playlist: "
read -a PLAYLIST_URL


echo "${#PLAYLIST_URL[1]}"


# # Diretório onde os vídeos serão baixados
# DOWNLOAD_DIR="~/Downloads/Waldik Soriano"

# # Criar o diretório de download, se não existir
# mkdir -p "$DOWNLOAD_DIR"

# # Baixar a playlist
# yt-dlp -i -x --audio-format mp3 -o "$DOWNLOAD_DIR/%(title)s.%(ext)s" "$PLAYLIST_URL"

# echo "Download da playlist concluído."

