# Live System Audio Transcriber (Linux)

Convert live system audio output into real-time text transcription on Linux.

## Features

* Real-time transcription of system audio
* Captures audio directly from system output devices
* Simple device selection utility
* Linux-only support
* Easy dependency installation

## Files

### `transcribe.py`

Main script that captures system audio and converts it into live text transcription.

### `to_know_device_no.py`

Utility script to list available audio devices and find the correct output device number required by `transcribe.py`.

### `requirements.py`

Installs or manages all required dependencies for the project.

---

## Requirements

* Linux operating system
* Python 3.8+
* Audio output device configured correctly
* Internet connection (if the transcription model requires downloading resources)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Sahil3458Q/Audio_to_text.git
cd Audio_to_text
```

Install dependencies:

```bash
python requirements.py
```

(depending on how your project is configured)

---

## Finding the Audio Device Number

Before starting transcription, determine the device number of the system audio output.

Run:

```bash
python to_know_device_no.py
```

This will display the available audio devices.

Example output:

```text
0: Microphone
1: USB Audio Device
2: Monitor of Built-in Audio
```

Note the device number corresponding to your system output device.

---

## Running the Transcriber

After identifying the correct device number, update the device number in `transcribe.py` if required.

Run:

```bash
python transcribe.py
```
The Script will ask for Device Number and then will start listening to system audio and display transcribed text in real time.

---

## Notes

* This project currently supports Linux only.
* Make sure your audio system provides a monitor/output device that can be captured.
* PulseAudio or PipeWire monitor devices are commonly used for system audio capture.

---

## Troubleshooting

### No audio detected

* Verify the correct device number is selected.
* Ensure system audio is playing.
* Check that PulseAudio/PipeWire is running.

### Device not found

Run:

```bash
python to_know_device_no.py
```

again and verify the device number.

---

## License

MIT License
