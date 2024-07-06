from gtts import gTTS
import os

# Path to your Telugu text file
input_file ="./Tel.txt"

# Read Telugu text from file
with open(input_file, 'r', encoding='utf-8') as file:
    mytext = file.read()

language = "te"  # Assuming "te" is for Telugu language

# Specify full path for saving on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file = os.path.join(desktop_path, "welcome111.mp3")

# Create gTTS object and save to the specified path
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save(output_file)

print(f"File saved to: {output_file}")
