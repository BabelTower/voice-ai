import ai
import audio
audio.captrue('voice/temp.wav')
text = ai.stt('voice/temp.pcm')
ai.tts(ai.chat(text) + ai.now() + ai.tomorrow() )
audio.playback('voice/audio.wav')