import requests
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text=str(price) + ' $')
    labelTime.config(text="Updated at " + time)

    canvas.after(5000, trackBitcoin)


canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Bitcoin Tracker")
canvas.config(bg="#f7931a")  # Bitcoin orange background


img = Image.open("bitcoin_logo.png")
img = img.resize((100, 100))
bitcoin_logo = ImageTk.PhotoImage(img)

labelLogo = tk.Label(canvas, image=bitcoin_logo, bg="#f7931a")
labelLogo.pack(pady=10)

# Fonts
f1 = ("Helvetica", 28, "bold")
f2 = ("Helvetica", 24, "bold")
f3 = ("Helvetica", 16, "italic")

# Labels
label = tk.Label(canvas, text="Bitcoin Price", font=f1, fg="white", bg="#f7931a")
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2, fg="#f7931a", bg="white", width=12, height=2, relief="solid", bd=1)
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font=f3, fg="white", bg="#f7931a")
labelTime.pack(pady=10)


trackBitcoin()
canvas.mainloop()
