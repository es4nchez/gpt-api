import sounddevice as sd
from pydub import AudioSegment
from scipy.io.wavfile import write
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY") 

fs = 44100  # fréquence d'échantillonnage
seconds = 5  # durée de l'enregistrement

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
# Attendre la fin de l'enregistrement
sd.wait()

# Enregistrer en tant que fichier WAV
write('output.wav', fs, myrecording)

# Convertir au format mp3
# sound = AudioSegment.from_wav("output.wav")
# sound.export("output.mp3", format="mp3")



audio_file= open("output.wav", "rb")
transcript = openai.Audio.Transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

print(transcript)