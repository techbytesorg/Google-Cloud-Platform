# pip install google-cloud-texttospeech
from google.cloud import texttospeech
import sys

def synthesize_text(text, output_filename="output.mp3"):
    """
    Synthesizes speech from the input text and saves it to an audio file.
    """
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Configure the voice parameters
    # Select the language code and SSML voice gender (optional)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", 
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL # Can be MALE, FEMALE, or NEUTRAL
    )

    # Configure the audio file format
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3 # MP3 is widely supported
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input, 
        voice=voice, 
        audio_config=audio_config
    )

    # The response's audio_content is binary.
    try:
        with open(output_filename, "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print(f'Audio content written to file "{output_filename}"')
    except IOError as e:
        print(f"Error writing file: {e}")
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    text_to_speak = "Hello, world! This is a demonstration of the Google Cloud Text to Speech API using Python."
    output_file = "hello_world.mp3"
    
    synthesize_text(text_to_speak, output_file)
