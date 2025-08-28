import whisper
import os
import subprocess
import sys

def check_ffmpeg_installed():
    """
    Check if ffmpeg is installed on the system and in PATH.
    
    Returns:
        bool: True if ffmpeg is installed, False otherwise.
    """
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True,check=True)
    except FileNotFoundError:
        print("[ERROR] ffmpeg is not installed or not found in PATH. Please install ffmpeg to proceed.")
        print("[INFO] You can download it from https://www.gyan.dev/ffmpeg/builds/ and add bin to your PATH")
        sys.exit(1)

def transcript (audio: str, model_size: str = "small", language: str = "es", save_output: bool = True) -> str:
    """
    Transcript an audio archive to text using OpenAI Whisper
    
    Parameters:
        audio (str): Path to the audio file.
        model_size (str): Indication of which Whisper model is wanted to choose.
        language (str): Language chosen to hear.
    
    Returns:
        str: Transcription.
    
    """
    
    check_ffmpeg_installed
    
    if not os.path.exists(audio):
        raise FileNotFoundError(f"The audio file {audio} doesn't exist.")
    
    print(f"[INFO] Loading Whisper Model.")
    model = whisper.load_model(model_size)
    
    print(f"[INFO] Transcripting audio {audio}...")
    result = model.transcribe(audio, language=language)
    
    text = result["text"]
    print(f"[INFO] Transcription complete: {text}.")
    
    #Save output
    if save_output:
        output_dir = os.path.join(os.getcwd(), "data_output")
        os.makedirs(output_dir, exist_ok=True)
        base_name = os.path.splitext(os.path.basename(audio))[0]
        output_file = os.path.join(output_dir, f"{base_name}_transcription.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[INFO] Transcription saved to {output_file}")
    
    return text

if __name__ == "__main__":
    #Testing, this executes only if this .py is executed directly.
    audio = os.path.join(os.getcwd(),"data_input", "test1.m4a")
    text = transcript(audio,"small", "es")
    print("Recognized text: \n", text)
    