import whisper
from openai import OpenAI
import os
import re
import dotenv
dotenv.load_dotenv()
client = OpenAI()

def transcribe_audio(filename):
    model = whisper.load_model("turbo")
    result = model.transcribe(filename, language="es")  # 'es' is for Spanish
    return result["text"]

def save_transcription(text, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

def translate_paragraphs(text):
    # Split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = []
    
    # Group sentences into chunks of about 5
    for sentence in sentences:
        current_chunk.append(sentence)
        if len(current_chunk) >= 5:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
    
    # Add any remaining sentences as the last chunk
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    translated_text = ""
    
    for chunk in chunks:
        if chunk.strip():
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a translator. This is part of a transcript of a podcast from two native Mexican Spanish speakers. Translate the following Spanish text to English. Please try to keep your translations rather direct so that it will assist with learning."},
                    {"role": "user", "content": chunk}
                ]
            )
            translation = response.choices[0].message.content
            translated_text += f"{chunk}\n\n{translation}\n\n"
    
    return translated_text

def full_translation(text):
    response = client.chat.completions.create(
        model="gpt-4o",  
        messages=[
            {"role": "system", "content": "You are a translator. This is a transcript of a podcast from two native Mexican Spanish speakers. Translate the following Spanish text to English. Please try to keep your translation rather direct so that it will assist with learning."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

def main():
    input_file = "latest_episode.mp3"
    transcription_file = "Marcas Mexicanas_transcription.txt"
    combined_file = transcription_file.replace(".txt", "_combined.txt")
    # translation_file = "translation_english2.txt"

    # Step 1: Transcribe audio
    # print("Transcribing audio...")
    # transcription = transcribe_audio(input_file)

    # Step 2: Save transcription
    # print("Saving transcription...")
    # save_transcription(transcription, transcription_file)

    # Load transcription from file
    with open(transcription_file, "r", encoding="utf-8") as f:
        transcription = f.read()

    # Step 3: Translate paragraphs and combine
    print("Translating paragraphs...")
    combined_text = translate_paragraphs(transcription)

    # Step 4: Save combined transcription and translation
    print("Saving combined transcription and translation...")
    save_transcription(combined_text, combined_file)

    # # Step 5: Full translation
    # print("Performing full translation...")
    # full_translated_text = full_translation(transcription)

    # # Step 6: Save full translation
    # print("Saving full translation...")
    # save_transcription(full_translated_text, translation_file)

    print("Process completed. Files generated:")
    # print(f"1. Original audio: {input_file}")
    # print(f"2. Spanish transcription: {transcription_file}")
    # print(f"3. Combined transcription and translation: {combined_file}")
    # print(f"4. English translation: {translation_file}")

if __name__ == "__main__":
    main()