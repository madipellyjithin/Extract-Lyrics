import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def fetch_lyrics():
    artist = artist_entry.get()
    song = song_entry.get()
    
    if not artist or not song:
        messagebox.showerror("Error", "Both fields are required")
        return

    try:
        lyrics = get_lyrics(artist, song)
        if lyrics:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, lyrics)
        else:
            messagebox.showerror("Error", "Lyrics not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def get_lyrics(artist, song):
    base_url = "https://api.lyrics.ovh/v1"
    url = f"{base_url}/{artist}/{song}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("lyrics")
    else:
        return None

# Create the main window
root = tk.Tk()
root.title("Lyrics Finder")

# Create and place the labels and text entry boxes
tk.Label(root, text="Artist:").grid(row=0, column=0, padx=10, pady=10)
artist_entry = tk.Entry(root)
artist_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Song:").grid(row=1, column=0, padx=10, pady=10)
song_entry = tk.Entry(root)
song_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the fetch button
fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create and place the text area for displaying lyrics
result_text = tk.Text(root, wrap='word', height=20, width=50)
result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
