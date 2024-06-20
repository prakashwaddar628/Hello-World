import tkinter as tk

# Define the translations
translations = {
    "English": "Hello, World!",
    "Hindi": "नमस्ते दुनिया!",
    "Bengali": "হ্যালো, ওয়ার্ল্ড!",
    "Tamil": "வணக்கம், உலகம்!",
    "Telugu": "హలో, ప్రపంచం!",
    "Marathi": "नमस्कार, जग!",
    "Gujarati": "હેલો, વર્લ્ડ!",
    "Kannada": "ನಮಸ್ಕಾರ",
    "Malayalam": "ഹലോ, ലോകം!",
    "Punjabi": "ਸਤ ਸ੍ਰੀ ਅਕਾਲ, ਦੁਨਿਆ!",
    "Odia": "ନମସ୍କାର, ବିଶ୍ଵ!"
}

# List of languages
languages = list(translations.keys())
current_language_index = 0

def change_language():
    global current_language_index
    current_language_index = (current_language_index + 1) % len(languages)
    selected_language = languages[current_language_index]
    label.config(text=translations[selected_language])
    button.config(text=f"Change to {languages[(current_language_index + 1) % len(languages)]}")

# Create the main window
root = tk.Tk()
root.title("Hello World Translator")
root.configure(bg="#f0f0f0")  # Set background color

# Create a label to display the text
label = tk.Label(root, text=translations[languages[current_language_index]], font=("Helvetica", 16), bg="#f0f0f0")
label.pack(pady=20)

# Create a button to change the language
button = tk.Button(root, text=f"Change to {languages[(current_language_index + 1) % len(languages)]}", command=change_language, font=("Helvetica", 12), bg="#4CAF50", fg="white", activebackground="#45a049", padx=10, pady=5, relief=tk.RAISED, bd=2)
button.pack(pady=10)

# Run the application
root.mainloop()
