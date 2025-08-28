from TTS.api import TTS
import os

#TODO: Add more voices and languages
#TODO: Add choice of voices

def text_to_speech(tts_model, text: str, speaker: str = "en_001", output_path: str = "output.wav"):
    
    """
    Convert text to speech using TTS library.
    
    Parameters:
        text (str): Text to be converted to speech.
        speaker (str): Speaker voice model.
        language (str): Language of the text.
        output_path (str): Path to save the output audio file.
    """
    
    print(f"[INFO] Loading TTS model.")
    #tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=True, gpu=False)
    
    print(f"[INFO] Generating speech...")
    tts_model.tts_to_file(text=text, speaker=speaker, file_path=output_path)
    
    print(f"[INFO] Speech synthesis complete. Audio saved to {output_path}")
    
    return output_path

if __name__ == "__main__":
    sample_text = "Hello! This is a test."
    tts = TTS("tts_models/en/vctk/vits")
    print(tts.speakers)
    #text_to_speech(text=sample_text, output_path="data_output/sample_output.wav")
    choice = tts.speakers[0]
    
    test_text = "Artificial intelligence is rapidly transforming the way we live, work, and communicate. From voice assistants on our smartphones to complex neural networks that can analyze medical images, AI has become an integral part of our daily lives. One of the most exciting aspects of this technology is speech synthesis, which allows machines to speak with human-like voices. By combining natural language processing with powerful text-to-speech models, developers can create applications that are not only functional but also accessible to people with different needs. Testing long paragraphs like this helps us evaluate whether the generated voice maintains clarity, proper intonation, and rhythm throughout the entire passage."
    
    text_to_speech(tts_model=tts,text=test_text, speaker=choice, output_path="data_output/sample_output.wav")