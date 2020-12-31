import ai
import audio
audio.captrue('voice/temp.wav')
text = ai.stt('voice/temp.pcm')
ai.tts(ai.chat(text))
audio.playback('voice/audio.wav')