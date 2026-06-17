import faster_whisper 
import sounddevice as sd
import soundfile as sf
import os ,queue , threading 


device = input("Enter Your Device Number : ")
rate = 48000
duration = 3

model = faster_whisper.WhisperModel(
    "small",
    cpu_threads=8,
    compute_type="int8",
    device="cpu"
)

audio_qu = queue.Queue()

print("Script Started :- ")
def record():
    while True : 
        audio = sd.rec(int(rate*duration) ,channels=2, samplerate= rate , device= device , dtype="float32")
        sd.wait()
        audio_qu.put(audio)

def transcribe():
    
    count=0
    while True:
        count+=1
        sf.write(f"system_audio_{count}.wav",audio_qu.get(),samplerate= rate)
        segments , info = model.transcribe(
            f"system_audio_{count}.wav",
            beam_size=1,
            language="en"
        )
        for k in segments : 
            if k.text!= "":
                with open(mode="a+" ,file="subs.txt") as f:
                    f.write(k.text + "\n")
                print(k.text)
        os.remove(f"system_audio_{count}.wav")

record_thread = threading.Thread(target=record,daemon=True)
transcribe_thread = threading.Thread(target= transcribe,daemon=True)

record_thread.start()
transcribe_thread.start()

record_thread.join()
transcribe_thread.join()
