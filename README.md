# RSS Feed Transcriber

A Python tool that fetches Spanish podcasts from RSS feeds and transcribes them using OpenAI's Whisper.

## Requirements

- Python 3.8+
- FFmpeg (required by Whisper for audio processing)
- OpenAI Whisper
- Python packages: requests, xml

## Installation

1. Clone this repository:

```bash
git clone https://github.com/derickdecesare/rss_feed_transcriber.git
cd rss_feed_transcriber
```

2. Create a virtual environment:

```bash
python -m venv spanish_env
source spanish_env/bin/activate  # On Windows: spanish_env\Scripts\activate
```

3. Install FFmpeg:

   - **macOS**: `brew install ffmpeg`
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - **Linux**: `sudo apt install ffmpeg`

4. Install Python dependencies:

```bash
pip install openai-whisper requests
```

**Note:** When you first run the script, Whisper will automatically download the model files (several hundred MB). This happens only once, but the first run may take longer because of this download.

## Usage

Run the script to fetch and transcribe the latest episode:

```bash
python fetchRss.py
```

The script will:

1. Fetch the RSS feed
2. Download the latest podcast episode
3. Transcribe the audio using Whisper
4. Save the transcription to a text file

## Configuration

Edit `fetchRss.py` to change the RSS feed URL or Whisper model settings.
