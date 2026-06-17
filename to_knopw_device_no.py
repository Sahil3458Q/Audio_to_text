import sounddevice as sd

for i,k in enumerate(sd.query_devices()):
    print(i,k["name"])
