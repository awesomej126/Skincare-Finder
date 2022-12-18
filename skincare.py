# Skincare Routine Finder using tkinter
# All products are drugstore/under $20
# Donot take this seriously, not a licensed dermatologist/aesthetician, just wanted to do this for fun
# Consult your dermatologist/aesthetician for more specific advice
# Kinda a coincidence most of the products are from CeraVe
# Asll suggestions chosen from online beauty magazine articles and from my own experience (I have oily skin)

import tkinter as tk

# Window
window = tk.Tk()
window.title("Skincare Routine")
window.geometry("1000x500")

# Dicitionaries for skincare products
cleansers = {
    "oily": "CeraVe Foaming Facial Cleanser",
    "dry": "CeraVe Hydrating Facial Cleanser",
    "combination": "CeraVe Hydrating Cream-To-Foam Cleanser",
    "sensitive": "Cetaphil Gentle Skin Cleanser",
}

moisturizers = {
    "oily": "CeraVe PM Moisturizing Lotion",
    "dry": "CeraVe Moisturizing Cream",
    "combination": "CeraVe Daily Moisturizing Lotion",
    "sensitive": "Neutrogena Oil-Free Moisturizer for Sensitve Skin",
}

sunscreens = {
    "oily": "CeraVe Ultra-Light Face Moisturizer with Sunscreen SPF 30",
    "dry": "CeraVe Hydrating Mineral Sunscreen SPF 30",
    "combination": "Cetapil Sheer Mineral Face Liquid Sunscreen SPF 50",
    "sensitive": "Versed Guards Up Daily Mineral Sunscreen SPF 35",
}

# Functions
def build():
    main_text["text"] = "Here is your skincare rountine:"
    build_routine["state"] = "disabled"
    reset_button["state"] = "normal"
    label = input.get()
    if label.casefold() == "oily":
        label = "oily"
    elif label.casefold() == "dry":
        label = "dry"
    elif label.casefold() == "combination" or label.casefold() == "combo":
        label = "combination"
    elif label.casefold() == "sensitive":
        label = "sensitive"
    cleanser_selection["text"] = "Cleanser: " + cleansers.get(label)
    moisturizer_selection["text"] = "Moisturizer: " + moisturizers.get(label)
    sunscreen_selection["text"] = "Sunscreen: " + sunscreens.get(label)
 
def reset():
    main_text["text"] = "What is your skin type?"
    reset_button["state"] = "disabled"
    build_routine["state"] = "normal"
    cleanser_selection["text"] = ""
    moisturizer_selection["text"] = ""
    sunscreen_selection["text"] = ""
    user_input.delete(0, "end")

# Buttons, Labels, & Input Stuff
main_text = tk.Label(window, text="What is your skin type?")
main_text.pack(pady=10)

input = tk.StringVar()
user_input = tk.Entry(window, textvariable=input)
user_input.pack(pady=10)

build_routine = tk.Button(window, command=build, text="Build My Skincare Routine")
build_routine.pack(pady=10)

cleanser_selection = tk.Label(window, text="")
cleanser_selection.pack(pady=10)

moisturizer_selection = tk.Label(window, text="")
moisturizer_selection.pack(pady=10)

sunscreen_selection = tk.Label(window, text="")
sunscreen_selection.pack(pady=10)

reset_button = tk.Button(window, command=reset, text="Reset", state="disabled")
reset_button.pack(pady=10)

window.mainloop()
