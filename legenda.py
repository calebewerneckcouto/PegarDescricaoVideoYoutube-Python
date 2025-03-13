from youtube_transcript_api import YouTubeTranscriptApi

# ID do vídeo do YouTube
video_id = '_oTDEVr60rc'

# Tentar pegar a legenda em português
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt'])

# Exibe a legenda completa
for entry in transcript:
    print(f"{entry['start']} -> {entry['start'] + entry['duration']}: {entry['text']}")
