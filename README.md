# YOUTUBE VIDEO TRANSCRIBE USING GEMINI AI

Use Gemini AI to transcribe YouTube videos quickly and accurately. using the transcription features, and editing the final transcript for accuracy. Ideal for content creators and anyone needing efficient transcription services,you can significantly enhance the accessibility and reach of your content..

# How to run?

### STEPS:

Clone the repository

```bash
Project repo https://github.com/codeakki/ChatWithPdfGemini.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n venv python=3.9 -y
```

```bash
conda activate venv
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# Finally run the following command
streamlit run app.py
```

Now,

```bash
open up localhost:

```

## Sample

![OpenAI Logo](https://github.com/codeakki/YouTubeTranscribeGemini/blob/master/image.png)
![OpenAI Logo](https://github.com/codeakki/YouTubeTranscribeGemini/blob/master/image%20copy.png)

### Techstack Used:

- Python
- Streamlit
- google-generativeai
- youtube_transcript_api
- pathlib
