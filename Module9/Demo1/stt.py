# run pip install google-cloud-speech pydub
from google.cloud import speech
from pydub import AudioSegment
import os
import sys

def transcribe_wav_file(file_path):
    """
    Ensures a WAV file is mono and LINEAR16 encoded, then transcribes it.
    """
    client = speech.SpeechClient()
    processed_file_path = "temp_processed_audio.wav"
    
    try:
        audio_segment = AudioSegment.from_wav(file_path)
        
        # Ensure sample rate is 44100 Hz for API compatibility
        target_sample_rate = 44100 
        
        if audio_segment.channels > 1 or audio_segment.frame_rate != target_sample_rate:
            print(f"Converting {file_path} to mono (1 channel) and {target_sample_rate} Hz...")
            audio_segment = audio_segment.set_channels(1)
            audio_segment = audio_segment.set_frame_rate(target_sample_rate)
            audio_segment.export(processed_file_path, format="wav")
            file_to_process = processed_file_path
        else:
            file_to_process = file_path
            print(f"Audio file is already compatible.")

        with open(file_to_process, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=target_sample_rate,
            language_code="en-US",
        )

        # Perform synchronous speech recognition
        response = client.recognize(config=config, audio=audio)

        # *** ADDED ERROR HANDLING HERE ***
        if not response.results:
            print("API returned no results. Check if the audio contains clear speech in the specified language.")
            return

        # Process and print the transcription results
        for result in response.results:
            if result.alternatives:
                print(f"Transcript: {result.alternatives[0].transcript}")
                print(f"Confidence: {result.alternatives[0].confidence}")
            else:
                print("Result object had no alternatives (no speech detected in this segment).")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        if os.path.exists(processed_file_path):
            os.remove(processed_file_path)

# Example usage
if __name__ == "__main__":
    # Ensure this points to your file
    audio_file_path = "harvard.wav" 
    transcribe_wav_file(audio_file_path)
