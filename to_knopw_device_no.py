import sounddevice as sd
import soundfile as sf ,os
import faster_whisper
rate =48000
duration = 3

model = faster_whisper.WhisperModel("base",compute_type="int8",device="cpu",cpu_threads=8)
for i,k in enumerate(sd.query_devices()):
    print(i,k["name"])
    try:
        
        audio = sd.rec(int(rate*duration) ,channels=2, samplerate= rate , device= i , dtype="float32")
        print("divice : " , i)
        sd.wait()
        sf.write(f"{i}.wav",audio,samplerate=rate)
        segments , info = model.transcribe(
            f"{i}.wav",
            beam_size=1
        )
        for k in segments : 
            if k.text!= "":
                print(k.text)
    except : 
        print(i,"no")
        
