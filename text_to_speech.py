from gtts import gTTS

import os

# Define the text you want to convert to speech
text = "I actually did it (lost 10k. I make 21k/yr)"

# Create a gTTS object
tts = gTTS(text)
# Save the generated speech as an audio file
tts.save("output.mp3")

# Play the generated audio file

