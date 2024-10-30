import whisper
import sys
from pathlib import Path

def transcribe_audio(audio_path):
    # Load the Whisper model (you can choose different sizes: tiny, base, small, medium, large)
    model = whisper.load_model("base")
    
    # Perform the transcription
    print("Transcribing... This may take a while depending on the file size.")
    result = model.transcribe(audio_path)
    
    
    save_transcription(audio_path, result["text"])

def save_transcription(audio_path, transcription):
    # Create output folder path
    output_folder = Path(audio_path).parent / "output"
    
    # Create the output folder if it doesn't exist
    output_folder.mkdir(exist_ok=True)
    
    # Create output file path (using original filename but in output folder)
    original_filename = Path(audio_path).stem  # Gets filename without extension
    output_path = output_folder / f"{original_filename}_transcription.txt"
    
    # Save the transcription
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(transcription)
    
    print(f"Transcription saved to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py <path_to_audio_file>")
        sys.exit(1)
    
    audio_path = sys.argv[1]
    transcribe_audio(audio_path)

