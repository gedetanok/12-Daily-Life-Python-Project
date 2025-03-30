
import tkinter as tk
from tkinter import messagebox
import pyaudio
import wave
import os
from datetime import datetime
from playsound import playsound

# Ensure directory exists for recordings
os.makedirs("assets/recordings", exist_ok=True)

# Initialize the main window
root = tk.Tk()
root.title("VoiceNotes Maker 🎙️")
root.geometry("550x500")
root.config(bg="#F1F5F9")  # Background color

# Initialize notes list
notes = []
def record_audio(duration):
    fs = 48000  # Sample rate
    channels = 2  # Stereo
    chunk = 1024  # Size of each audio chunk
    
    # Filename for saving your voicenotes
    filename = f"assets/recordings/AudioNote_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
    p = pyaudio.PyAudio()

    # Open the stream for audio recording
    stream = p.open(format=pyaudio.paInt16,  # Audio format (16-bit)
                    channels=channels,
                    rate=fs,
                    input=True,
                    frames_per_buffer=chunk)
    frames = []
    # Record audio in chunks
    for _ in range(0, int(fs / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    # Stop recording
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # Save audio to a .wav file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
   
    # Add recording to the list
    notes.append(filename)
    note_list.insert(tk.END, os.path.basename(filename))

def play_audio():
    selected_index = note_list.curselection()
    if selected_index:
        filename = notes[selected_index[0]]
        # Use playsound to play the selected audio file
        playsound(filename)
    else:
        messagebox.showwarning("No Selection", "Please select a note to play.")

# Load any existing notes
for file in os.listdir("assets/recordings"):
    if file.endswith(".wav"):
        notes.append(f"assets/recordings/{file}")

# Set up the basic UI elements
header_frame = tk.Frame(root, bg="#4C6EF5", pady=20)
header_frame.pack(fill="x")
header_label = tk.Label(header_frame, text="Memoir🎙️", bg="#4C6EF5", fg="white", font=("Arial", 20, "bold"))
header_label.pack()
tk.Label(root, text="Record for (seconds):", bg="#F1F5F9", font=("Arial", 12)).pack(pady=(10, 5))
button_frame = tk.Frame(root, bg="#F1F5F9")
button_frame.pack()

# Record duration buttons with improved colors
record_buttons = [("5s", 5),("10s", 10),("15s", 15)]
for text, duration in record_buttons:
    button = tk.Button(button_frame, text=text, command=lambda d=duration: record_audio(d), bg="#5CBBF6", fg="white", font=("Arial", 12, "bold"), width=8, relief="flat")
    button.grid(row=0, column=record_buttons.index((text, duration)), padx=15, pady=10)
tk.Label(root, text="Recorded Notes:", bg="#F1F5F9", font=("Arial", 12)).pack(pady=(15, 5))
note_list = tk.Listbox(root, height=8, font=("Arial", 12), bg="#FFFFFF", fg="#333333", selectmode=tk.SINGLE, bd=2, relief="groove")
note_list.pack(padx=20, pady=10, fill=tk.BOTH)

# Populate the notes list box
for note in notes:
    note_list.insert(tk.END, os.path.basename(note))

# Playback button with a sleek design
play_button = tk.Button(root, text="Play Selected Note", command=play_audio, bg="#FF6F61", fg="white", font=("Arial", 12, "bold"), width=20, relief="flat")
play_button.pack(pady=(15, 5))

# Footer with app description
footer_frame = tk.Frame(root, bg="#4C6EF5", pady=10)
footer_frame.pack(fill="x", side="bottom")
footer_label = tk.Label(footer_frame, text="A Tool for managing VoiceNotes Effortlessly!!", bg="#4C6EF5", fg="white", font=("Arial", 10))
footer_label.pack()
root.mainloop()