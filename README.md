# NXTECH-Python-Task-2

# Speech Assistant App

The Speech Assistant App is a Python application that utilizes speech recognition and text-to-speech conversion to create a simple speech assistant. This assistant can take voice input from the user, process it, and respond with spoken or displayed output.

## Features

- Speech Recognition: The app can convert spoken language into text using the SpeechRecognition library.
- Text-to-Speech Conversion: The app can convert text into spoken language using the gTTS (Google Text-to-Speech) library.
- Command Processing: The app can process certain voice commands and respond accordingly.
- User-Friendly Interface: The app provides a simple and intuitive command-line interface for interaction.

## Installation

1. Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/speech-assistant-app.git
```

2. Navigate to the project directory:

```bash
cd speech-assistant-app
```

3. Install the required dependencies using pip:

```bash
pip install SpeechRecognition gTTS playsound
```

## Usage

1. Run the `speech_assistant.py` script to start the Speech Assistant App:

```bash
python speech_assistant.py
```

2. The app will wait for your voice input. Simply speak a command or a phrase.

3. The app will process your input and respond with spoken language.

## Commands

The following commands are supported by the app:

- **"Hello"**: The app will greet you.
- **"What's the time?"**: The app will tell you the current time.
- **"How are you?"**: The app will respond with a friendly message.
- **"Exit" or "Quit"**: The app will close.

## Customization

You can customize the app by adding more commands and responses in the `speech_assistant.py` script. Look for the section labeled "Command Processing" and add your own conditional statements for new commands.

## Limitations

- The accuracy of speech recognition may vary based on the quality of the audio input and the background noise.
- The app may not understand complex sentences or certain accents.
- It requires an active internet connection to utilize the gTTS library for text-to-speech conversion.

## Future Enhancements

- Integration with natural language processing for better command understanding.
- Adding support for multiple languages and accents.
- Implementing a graphical user interface (GUI) for a more user-friendly experience.

## Credits

- This app uses the SpeechRecognition library for speech recognition: https://pypi.org/project/SpeechRecognition/
- This app uses the gTTS library for text-to-speech conversion: https://pypi.org/project/gTTS/

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute, modify, and share the Speech Assistant App. If you have any suggestions or encounter issues, please create a new issue in the repository.
