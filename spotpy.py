import os
from pytube import YouTube
import cv2
from ffpyplayer.player import MediaPlayer
from googleapiclient.discovery import build

# Chave da API do YouTube
YOUTUBE_API_KEY = 'YOUR API KEY'

# Função para buscar vídeos no YouTube
def search_video(query):
    response = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY).search().list(
        part='snippet', q=query, type='video', maxResults=1
    ).execute()
    video_id = response['items'][0]['id']['videoId']
    video_title = response['items'][0]['snippet']['title']
    return f'https://www.youtube.com/watch?v={video_id}', video_title

# Função para baixar vídeos do YouTube
def download_video(url, output_path):
    YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=output_path)
    return output_path

# Função para reproduzir vídeos com controle de teclado
def play_video(video_path, video_title):
    video = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    if not video.isOpened():
        print("Error: Could not open video.")
        return False

    paused, volume, muted = False, 1.0, False
    total_duration = video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS)
    video_finished = False

    print(f"Reproduzindo: {video_title}")

    while True:
        if not paused:
            ret, frame = video.read()
            if not ret:
                video_finished = True
                break

        audio_frame, val = player.get_frame()
        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame

        cv2.imshow('Video', frame)
        key = cv2.waitKey(25) & 0xFF
        if key == ord('q'): break # parar(break geral)
        elif key == ord('w'): volume = min(volume + 0.1, 1.0); player.set_volume(volume)  # aumentar volume
        elif key == ord('s'): volume = max(volume - 0.1, 0.0); player.set_volume(volume) # diminuir volume
        elif key == ord('d'): player.seek(5) # avançar 5 segundos na música 
        elif key == ord('a'): player.seek(-5) # voltar 5 segundos na música 
        elif key == ord('m'): muted = not muted; player.set_volume(0 if muted else volume) # mutar
        elif key == ord('p'): paused = not paused; player.set_pause(paused) # pausar e despausar
        elif key == ord('0'): player.seek(-total_duration) # voltar pro início
        elif key == ord('n'): video_finished = True; break  # avançar na playlist
        elif key == ord('b'): video_finished = 'prev'; break  # voltar na playlist
        print(f'Tempo atual: {player.get_pts() / 60:.2f}m / Duração total: {total_duration / 60:.2f}m', end='\r')

        # Verifica se faltam aproximadamente 3 segundos para o fim do vídeo
        if not paused and (total_duration - player.get_pts()) <= 3:
            video_finished = True
            break

    video.release()
    player.close_player()
    cv2.destroyAllWindows()
    return video_finished

# Função para criar resumo dos vídeos assistidos
def create_summary(summary_list):
    with open('summary.txt', 'w') as f:
        for item in summary_list:
            f.write(f'{item}\n')
    print("\nResumo das músicas que você escutou:")
    for item in summary_list:
        print(item)

# Função principal
def main():
    playlist, output_paths, summary_list = [], [], []
    while True:
        query = input("Digite o nome do vídeo ou 'done' para finalizar a lista: ")
        if query.lower() == 'done': break
        url, title = search_video(query)
        playlist.append((url, title))

    for index, (url, title) in enumerate(playlist):
        output_path = f'video_{index}.mp4'
        download_video(url, output_path)
        output_paths.append(output_path)
        summary_list.append(title)

    current_video_index = 0
    while current_video_index < len(output_paths):
        result = play_video(output_paths[current_video_index], playlist[current_video_index][1])  # Passa o título do vídeo
        if result == 'quit': break
        elif result == 'prev': current_video_index = max(0, current_video_index - 1)
        else: current_video_index += 1

    for path in output_paths:
        os.remove(path)
    create_summary(summary_list)

if __name__ == "__main__":
    main()
