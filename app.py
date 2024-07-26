import streamlit as st
from dotenv import load_dotenv
from promopt import prompt
load_dotenv() ##load all the nevironment variables
import os
import google.generativeai as genai
from utility import get_video_transcript,gemini

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))





st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")



# Display the thumbnail of the video
if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)



# if st.button("Get Transcript"):
#     transcript
#  Get the transcript of the video
if st.button("Get Detailed Notes"):
    transcript_text=get_video_transcript(youtube_link)

    if transcript_text:
        summary=gemini(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)




