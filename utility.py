import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

## getting the transcript data from yt videos
def get_video_transcript(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    

    ## getting the summary based on Prompt from Google Gemini Pro
def gemini(transcript_text,prompt):

    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text
