import requests
import xml.etree.ElementTree as ET
import whisper


def fetch_rss_feed(url):
    try:
        # Send a GET request to fetch the RSS feed
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the XML content
            return response.content
        else:
            print(f"Failed to fetch RSS feed. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def parse_rss_feed(rss_content):
    try:
        root = ET.fromstring(rss_content)
        first_item = root.find('.//item')
        if first_item is not None:
            title = first_item.find('title').text
            link = first_item.find('enclosure').attrib['url']
            return title, link
        else:
            print("No items found in the RSS feed.")
            return None, None
    except Exception as e:
        print(f"An error occurred while parsing the RSS feed: {e}")
        return None, None
    

def download_audio_file(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"Downloaded: {filename}")
        return True
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")
        return False


def transcribe_audio(filename):
    model = whisper.load_model("turbo")
    result = model.transcribe(filename, language="es")  # 'es' is for Spanish
    return result["text"]


def save_transcription(text, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    # Step 1: Fetch the RSS feed content
    rss_url = "https://feeds.megaphone.fm/SONORO4487924320"
    rss_content = fetch_rss_feed(rss_url)

    if rss_content:
        # Step 2: Parse the RSS feed and get the first audio file link
        title, audio_url = parse_rss_feed(rss_content)
        
        if audio_url:
            print(f"Downloading episode: {title}")
            
            # Step 3: Download the audio file
            filename = f"{title}.mp3"
            if download_audio_file(audio_url, filename):
                
                # Step 4: Transcribe the audio file
                print("Transcribing audio...")
                transcription = transcribe_audio(filename)
                print("\nTranscription length:")
                print(len(transcription))
                # Step 5: Save the transcription to a file
                transcription_file = f"{title}_transcription.txt"
                save_transcription(transcription, transcription_file)
            else:
                print("Failed to download the audio file. Transcription aborted.")
        else:
            print("No audio URL found. Cannot proceed with download and transcription.")
    else:
        print("Failed to fetch RSS feed. Cannot proceed with parsing and transcription.")