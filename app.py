import streamlit as st
import whisper
from PIL import Image
import base64
import openai  # Make sure your OpenAI key is set in environment or use st.secrets

st.set_page_config(page_title="Audio to Visual", layout="centered")
st.title("🎧 Audio to Visual")

# Upload or use sample audio
audio_file = st.file_uploader("Upload your audio file (mp3/wav)", type=["mp3", "wav"])
sample_path = "./fromsunriseland_trimmed.mp3"

if audio_file is not None:
    with open("temp_audio.mp3", "wb") as f:
        f.write(audio_file.read())
    audio_path = "temp_audio.mp3"
else:
    try:
        with open(sample_path, "rb") as f:
            audio_bytes = f.read()
        audio_path = sample_path
        st.audio(audio_bytes, format="audio/mp3")
    except FileNotFoundError:
        st.warning("No sample audio found and no file uploaded.")

# Transcribe
if st.button("Transcribe & Generate Visual"):
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        transcript = result["text"]
        st.subheader("📝 Transcription")
        st.success(transcript)

        # Generate visual (text-to-image)
        st.subheader("🖼️ Generated Visual")
        with st.spinner("Generating visual..."):
            openai.api_key = "YOUR_OPENAI_API_KEY"

            response = openai.Image.create(
                prompt=transcript,
                n=1,
                size="512x512"
            )
            image_url = response["data"][0]["url"]
            st.image(image_url, caption="Generated from transcript")

    except Exception as e:
        st.error(f"Transcription or image generation failed: {e}")
