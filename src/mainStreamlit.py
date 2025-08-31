import os
import streamlit
import tempfile

from TTS.api import TTS
from transcriptor import transcript
from translator import translate
from voice import text_to_speech


# syncronization of the three modules
def main():
    #Setting the interface with streamlit
    streamlit.set_page_config(page_title="AI Translator", layout="centered")
    streamlit.title("AI Translator")

    #Upload audio file
    audio_file = streamlit.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])
    if audio_file is not None:
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".m4a") as temp_audio_file:
            temp_audio_file.write(audio_file.read())
            temp_audio_file_path = temp_audio_file.name
        
        streamlit.write("Uploaded Audio saved in:", temp_audio_file_path)
        streamlit.audio(audio_file, format="audio/m4a")
        
        target_language = streamlit.selectbox("Select target language", options=["en"])

        #speaker_choice = streamlit.selectbox("Select speaker", options=["p225", "p226", "p227", "p228", "p229", "p230"])
        if streamlit.button("Translate"):
            with streamlit.spinner("Processing..."):
                transcription = transcript(audio=temp_audio_file_path, model_size="small", language="es", save_output=True)
            # Call the main function to process the audio file
            streamlit.success("Transcription completed successfully.")
            
            with streamlit.spinner("Translating..."):
                translation = translate(text=transcription, dest_language=target_language)
                
            streamlit.success("Translation completed successfully.")
            streamlit.text_area("Translation: ", value=translation, height=200)
            
            with  streamlit.spinner("Generating speech..."):
                tts_model = TTS("tts_models/en/vctk/vits")
                choice = tts_model.speakers[0]
                text_to_speech(tts_model,text=translation, speaker=choice, output_path="data_output/translation_output.wav")
                streamlit.success("Audio generated. Check the data_output folder for results.")
                streamlit.audio("data_output/translation_output.wav", format="audio/wav")

if __name__ == "__main__":
    main()
    