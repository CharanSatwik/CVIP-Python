from scipy.io.wavfile import write
import sounddevice as sd
dur = 12
fps = 44100
print("Recording started")
recording = sd.rec(int(dur*fps), samplerate=fps, channels=2)
sd.wait()
print("Recording Completed.")
write("Recording.wav", fps, recording)
