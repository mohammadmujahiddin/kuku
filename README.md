# 🎧 Kuku AI Companion — Smart Visual & Voice Enhancer for Audiobooks

Welcome to the **Kuku AI Companion**, a generative AI-powered enhancement for audiobook platforms like Kuku FM. This prototype brings stories to life using AI-generated visuals, personalized audio summaries, smart resume features, and even celebrity voice narration (conceptual).

---

## 🔍 Objective

To reduce distraction and improve comprehension while listening to audiobooks by:
- Generating **AI visuals** that reflect the audiobook content
- Providing **smart caching and resumption**
- Offering **celebrity voice customization** (conceptual feature)
- Summarizing content through audio and visuals

---

## 👤 User Persona

**Ravi Verma**, a 22-year-old visual learner, finds it hard to stay focused while listening to audiobooks. The Kuku AI Companion helps him stay engaged and better recall content using visuals and personalized voiceovers.

---

## ✨ Key Features

- 🎨 **AI-Generated Visuals**: Real-time or cached animations based on audio content
- 🔁 **Smart Resume**: Auto-saves progress and shows summaries
- 🗣️ **Celebrity Voice Option**: (Conceptual) Choose a familiar voice to narrate
- 🧠 **Quick Summaries**: Text + visual recaps of listened segments

---

## 🛠️ Tech Stack

| Feature                  | Tools Used                                |
|--------------------------|--------------------------------------------|
| Audio Transcription      | OpenAI Whisper                             |
| Visual Generation        | Stable Diffusion, DALL·E                   |
| Voice Cloning (concept)  | ElevenLabs, Respeecher                     |
| UI & Prototype           | Streamlit, Python                          |

---

## 🔁 Workflow

1. Upload or play audiobook audio
2. Transcribe using Whisper
3. Summarize the transcript (manually or with GPT-based summarizer)
4. Generate visuals from summaries using Stable Diffusion
5. Display visuals with playback and summary

---

## 🚀 Prototype Setup

### Requirements
- Python 3.x
- Streamlit
- OpenAI Whisper
- HuggingFace Transformers
- Diffusers (Stable Diffusion)
  
### Run Locally
```bash
git clone https://github.com/mohammadmujahiddin/kuku
cd kuku
pip install -r requirements.txt
streamlit run app.py
