YouTube Transcript API Example
Este projeto utiliza a biblioteca youtube-transcript-api para extrair e exibir legendas de vídeos do YouTube em um idioma específico (neste caso, português).

Requisitos
Python 3.x
Biblioteca youtube-transcript-api
Instalação
Clone o repositório ou faça o download do código.
Instale as dependências necessárias com o seguinte comando:

pip install youtube-transcript-api
Como Usar
Certifique-se de ter o ID do vídeo do YouTube do qual deseja obter a legenda.

O ID do vídeo é a sequência de caracteres que aparece após v= na URL do vídeo. Exemplo: https://www.youtube.com/watch?v=_oTDEVr60rc, onde _oTDEVr60rc é o ID do vídeo.
Altere a variável video_id no código com o ID do vídeo desejado.

Execute o script Python para obter a transcrição em português.



python script_name.py
Funcionamento
O script obtém as legendas do vídeo do YouTube usando a API YouTubeTranscriptApi e exibe as legendas com o tempo de início e fim, além do texto correspondente.

O código tenta buscar as legendas no idioma português (languages=['pt']). Se não houver legendas disponíveis nesse idioma, será gerado um erro ou uma transcrição no idioma disponível.

Exemplo de saída

0.0 -> 3.0: Olá, bem-vindos ao meu canal!
3.1 -> 6.5: Neste vídeo, vamos aprender a usar a API do YouTube.
6.6 -> 10.0: Espero que gostem e aproveitem o conteúdo.
Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
