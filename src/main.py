import os
from TTS.api import TTS

from transcriptor import transcript
from translator import translate
from voice import text_to_speech


# syncronization of the three modules


def main():
    audio_path = "data_input/test1.m4a"  # Path to the input audio file
    model_size = "small"  # Whisper model size
    source_language = "es"  # Source language code (Spanish)
    target_language = "en"  # Target language code (English)
    
    # Step 1: Transcribe the audio file
    transcription = transcript(audio=audio_path, model_size=model_size, language=source_language, save_output=True)
    
    # Step 2: Translate the transcription
    translation = translate(text=transcription, dest_language=target_language)
    
    # Step 3: Convert the translation to speech
    tts_model = TTS("tts_models/en/vctk/vits")
    choice = tts_model.speakers[0]

    text_to_speech(tts_model,text=translation, speaker=choice, output_path="data_output/translation_output.wav")    
    # Save the translation to a file
    output_dir = os.path.join(os.getcwd(), "data_output")
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    output_file = os.path.join(output_dir, f"{base_name}_translation.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(translation)
    print(f"[INFO] Translation saved to {output_file}.")
    
if __name__ == "__main__":
    main()
    