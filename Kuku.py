import streamlit as st
import whisper
import os
from PIL import Image, ImageDraw, ImageFont
import uuid

st.set_page_config(page_title="Audio to Visuals", layout="centered")

st.title("🎧 Audio to Visuals Generator")

# Initialize model
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

# Sample file download
st.markdown("### 📥 Download Sample Audio")
sample_audio_path = "./fromsunriseland_trimmed.mp3"
with open(sample_audio_path, "rb") as f:
    st.download_button("Download Sample", f, file_name="sample_audio.mp3")

# Upload audio file
uploaded_file = st.file_uploader("📤 Upload an Audio File", type=["mp3", "wav"])

if uploaded_file:
    st.audio(uploaded_file, format="audio/mp3")

    with open("temp_audio.mp3", "wb") as f:
        f.write(uploaded_file.read())

    st.markdown("### 📝 Transcribing Audio...")
    result = model.transcribe("temp_audio.mp3")
    transcript = result["text"]
    st.success("Transcription Complete!")
    st.markdown("#### Transcript")
    st.write(transcript)

    st.markdown("### 🎨 Generating Visuals...")

    def generate_image(text):
        img = Image.new('RGB', (720, 400), color=(240, 240, 255))
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        draw.text((20, 180), text[:100] + ('...' if len(text) > 100 else ''), font=font, fill=(0, 0, 0))
        return img

    # Generate 1 simple visual for now
    img = generate_image(transcript)
    img_id = f"visual_{uuid.uuid4().hex}.png"
    img.save(img_id)

    st.image(img, caption="Generated Visual", use_column_width=True)

    with open(img_id, "rb") as f:
        st.download_button("📥 Download Visual", f, file_name="generated_visual.png")

    os.remove("temp_audio.mp3")
    os.remove(img_id)
