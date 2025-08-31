from googletrans import Translator
import asyncio

def translate (text: str, dest_language: str = "en") -> str:
    """
    Translate a text to the desired language using google translation API.  
    
    Parameters:
        text (str): Text to be translated.
        dest_language (str): Destination language code.
        
    Returns:
        str: Translated text.
    """
    
    translator = Translator()
    translated = asyncio.run(translator.translate(text, dest=dest_language))
    print(f"[INFO] Translation complete: {translated.text}")
    
    return translated.text

