import tkinter as tk
import random
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def get_trending_news():
    """Fetch and return trending news headlines."""
    url = "http://newsapi.org/v2/top-headlines?country=us&apiKey=CREATE_YOUR_OWN"
    page = requests.get(url).json() 
    articles = page["articles"]
    results = [ar["title"] for ar in articles[:10]]
    headlines = "\n".join(f"{i + 1}. {title}" for i, title in enumerate(results))
    return headlines

def get_horoscope(sign_name):
    """Fetch and return horoscope for the specified sign."""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    signs = {
        'aries':1, 'taurus':2, 'gemini':3, 'cancer':4,
        'leo':5, 'virgo':6, 'libra':7, 'scorpio':8,
        'sagittarius':9, 'capricorn':10, 'aquarius':11, 'pisces':12
    }
    sign_id = signs.get(sign_name.lower())
    if sign_id is None:
        return "Sign not found."
    
    url = f'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={sign_id}'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        horoscope_text = soup.select('.main-horoscope p')[0].getText().strip().capitalize()
        sign = soup.select('h1')[0].getText().strip().capitalize()
        return f"{sign} Horoscope: {horoscope_text}"
    except:
        return "Could not fetch the horoscope."

def get_history_today():
    """Fetch and return historical events that happened on this day."""
    url = 'https://www.onthisday.com/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    history_list = soup.select('.event')[:5]  # Limit to 5 events
    
    events = [event.getText().strip() for event in history_list]
    history_text = "\n".join(events)
    return history_text

def show_popup():
    # Fetch information from each function
    news = get_trending_news()
    horoscope = get_horoscope('aries')  # Replace 'aries' with desired sign
    history = get_history_today()
    
    # Create the main Tkinter window
    root = tk.Tk()
    from datetime import datetime
    # Get the current date to disply on GUI 
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d %b %Y")
    
    root.title(f"Daily Update: {formatted_date}")
    root.geometry("500x600")
    root.configure(bg="#f0f0f5")  # Set background color

    # Set up a Canvas with a Scrollbar
    canvas = tk.Canvas(root, bg="#f0f0f5")
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f0f0f5")
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Define Canvas, Scrollbar and Colors
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    header_font = ("Arial", 14, "bold")
    text_font = ("Arial", 12)
    colors_list = ["#E4E0E1","#FFDDC1", "#D4E157", "#81D4FA", "#FFAB91", "#A5D6A7", "#FFF59D", "#CE93D8", "#B39DDB", "#90CAF9", "#FFE082", "#FFCCBC", "#AED581", "#FFE0B2", "#80CBC4", "#F48FB1"]
    section_bg = random.choice(colors_list) 

    # Function to create a section
    def create_section(parent, title, content, color):
        frame = tk.Frame(parent, bg=color, pady=10, padx=10)
        frame.pack(fill="x", pady=5, padx=5)
        title_label = tk.Label(frame, text=title, font=header_font, bg=color, fg="#333333")
        title_label.pack(anchor="w", pady=(0, 5))
        content_label = tk.Label(frame, text=content, justify="left", wraplength=450, bg=color, fg="#000000")
        content_label.pack(anchor="w")
        return frame

    # Add the trending news section
    create_section(scrollable_frame, "Trending News", news, section_bg)
    # Add the horoscope section
    create_section(scrollable_frame, "Horoscope", horoscope, section_bg)
    # Add the history today section
    create_section(scrollable_frame, "On This Day", history, section_bg)
   
    # Add a close button at the bottom
    close_button = ttk.Button(scrollable_frame, text="Close", command=root.destroy)
    close_button.pack(pady=20)
    root.mainloop()

# Run the script and show the popup on startup
if __name__ == "__main__":
    pass