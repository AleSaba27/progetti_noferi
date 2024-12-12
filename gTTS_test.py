from gtts import gTTS
from playsound import playsound

# Correctly formatted text string
text = "This is in English language"

# Correctly use single or double quotes for the parameters
var = gTTS(text=text, lang='en')

# Save the audio file
var.save('eng.mp3')

# Play the audio file
playsound('./eng.mp3')
