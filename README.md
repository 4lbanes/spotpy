YouTube Video Playlist Manager
Este programa em Python permite buscar, baixar e reproduzir vídeos do YouTube com controle de teclado. Após reproduzir cada vídeo, ele cria um resumo dos vídeos assistidos.

Pré-requisitos
Python 3.x instalado

Pacotes necessários:

pytube
opencv-python
ffpyplayer
google-api-python-client
Você pode instalá-los usando o pip:

Copiar código
pip install pytube opencv-python ffpyplayer google-api-python-client
Uma chave de API do YouTube para acessar a API v3. Você pode obter uma em Google Developers Console.

Como usar
Configuração da Chave de API:

Substitua 'YOUR_YOUTUBE_API_KEY' na variável YOUTUBE_API_KEY no arquivo playlist_manager.py pela sua chave de API do YouTube.

Execução do Programa:

Execute o script playlist_manager.py no terminal:

Copiar código
python playlist_manager.py
Operação do Programa:

Digite o nome de um vídeo para buscar no YouTube.
Adicione quantos vídeos desejar à playlist, digitando o nome de cada vídeo.
Quando terminar de adicionar vídeos, digite 'done'.
O programa baixará os vídeos da playlist, os reproduzirá com controle de teclado e criará um arquivo summary.txt com o resumo dos vídeos assistidos.
Controles durante a Reprodução:

q: Parar a reprodução e fechar o programa.
w: Aumentar o volume.
s: Diminuir o volume.
d: Avançar 5 segundos no vídeo.
a: Retroceder 5 segundos no vídeo.
m: Alternar mudo (mutar/desmutar).
p: Pausar ou retomar a reprodução.
0: Reiniciar o vídeo.
n: Avançar para o próximo vídeo na playlist.
b: Voltar para o vídeo anterior na playlist.
Limpeza:

Após terminar a reprodução dos vídeos, os arquivos de vídeo serão removidos automaticamente.

Exemplo de Uso
Buscar vídeos musicais no YouTube.
Baixar e reproduzir vídeos com controle de teclado para ajustar volume, avançar/retroceder e pausar/reproduzir.
Criar um resumo dos vídeos assistidos no arquivo summary.txt.
