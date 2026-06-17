import os

print("\nDownloading required Modules : \n")

os.system("pip install faster-whisper soundfile sounddevice")

print("\n--Required Modules Downloaded.")
print("\nDownlaoding AI MODEL ~800MB. Please Wait and don't close the window : ")
import faster_whisper

model = faster_whisper.WhisperModel(
    "small",
    compute_type="int8",
)

print("\n--Downloaded Completed.")
