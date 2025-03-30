# Have you ever been overwhelmed by copied text, 
# unable to track what you’ve pasted, or, worse, losing important snippets? 
# Have you ever struggled with text in a non-native language, 
# constantly visiting Google Translate for a quick conversion? 
# Ever Thought of having a tool that captures everything you copy 
# and effortlessly translates it into English? 
# This automation script is your clipboard assistant. 
# It monitors all the text you copy and 
# provides seamless translations.


import tkinter as tk
from tkinter import ttk
import pyperclip   # PIP Install
from deep_translator import GoogleTranslator
from langdetect import detect

def detect_and_translate(text):
    try:
        # Detect the language
        detected_language = detect(text)
        print(f"Detected language: {detected_language}")
        if detected_language != 'en':
            translated_text = GoogleTranslator(source=detected_language, target='en').translate(text)
            print(f"Translated text: {translated_text}")
            return translated_text
        else:
            print("The text is already in English.")
            return text
    except Exception as e:
        print(f"Error: {e}")
        return text

## Update and Append GUI with Newly Coped Text
def update_listbox():
    new_item = pyperclip.paste()
    new_item = detect_and_translate(new_item)
    if new_item not in X:
        X.append(new_item)
        listbox.insert(tk.END, new_item)
        listbox.insert(tk.END, "----------------------")
    listbox.yview(tk.END)
    root.after(1000, update_listbox)

## Checks for Copied Contet
def copy_to_clipboard(event):
    selected_item = listbox.get(listbox.curselection())
    if selected_item:
        pyperclip.copy(selected_item)

X = []
root = tk.Tk()
root.title("Clipboard Manager")
root.geometry("500x500")
root.configure(bg="#f0f0f0")
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=10, pady=10)
label = tk.Label(frame, text="Clipboard Contents:", bg="#f0f0f0")
label.grid(row=0, column=0)
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(root, width=150, height=150, yscrollcommand=scrollbar.set)
listbox.pack(pady=10)
scrollbar.config(command=listbox.yview)
update_listbox()
listbox.bind("<Double-Button-1>", copy_to_clipboard)
root.mainloop()
