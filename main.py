import requests
import random
from tkinter import *
import os

# CONSTANTS
GREEN = "#9bdeac"
FONT_NAME = "Courier"
API_KEY = os.environ.get("KEY")  # Create your own API_KEY on API Ninjas

categories = [
    "age", "alone", "amazing", "anger", "architecture", "art", "attitude", "beauty",
    "best", "birthday", "business", "car", "change", "communications", "computers", "cool",
    "courage", "dad", "dating", "death", "design", "dreams", "education", "environmental",
    "equality", "experience", "failure", "faith", "family", "famous", "fear", "fitness",
    "food", "forgiveness", "freedom", "friendship", "funny", "future", "god", "good",
    "government", "graduation", "great", "happiness", "health", "history", "home", "hope",
    "humor", "imagination", "inspirational", "intelligence", "jealousy", "knowledge",
    "leadership", "learning", "legal", "life", "love", "marriage", "medical", "men", "mom",
    "money", "morning", "movies", "success"
]


# FETCH CODES
def get_quote():
    category = random.choice(categories)
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    response.raise_for_status()
    data = response.json()
    try:
        quote = data[0]["quote"]
        author = data[0]["author"]
    except IndexError:
        pass
    else:
        canvas.itemconfig(quote_text, text=f"{quote}\n- {author}")


# UI INTERFACE
window = Tk()
window.title("A Quote for You...")
window.config(padx=50, pady=50, bg=GREEN)

canvas = Canvas(width=400, height=414, bg=GREEN, bd=FALSE, highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(200, 212, image=background_img)
quote_text = canvas.create_text(200, 190, text="THE QUOTE \n\n\n\nClick on the face", width=350,
                                font=(FONT_NAME, 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

face_img = PhotoImage(file="face.png")
quote_button = Button(image=face_img, highlightthickness=0, command=get_quote, bg=GREEN, bd=FALSE)
quote_button.grid(row=1, column=0)

window.mainloop()
