import streamlit as st
from deep_translator import GoogleTranslator
import edge_tts
import asyncio
import base64
import speech_recognition as sr
import os

st.set_page_config(page_title="Marathi Setu", page_icon="🚩")

# Function to load font and encode to base64
@st.cache_data
def get_base64_font(font_path):
    with open(font_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to the font file
font_file = os.path.join("lohit-marathi-regular", "Lohit Marathi Regular", "Lohit Marathi Regular.ttf")

if os.path.exists(font_file):
    font_base64 = get_base64_font(font_file)
    font_style = f"""
    <style>
    @font-face {{
        font-family: 'Lohit Marathi';
        src: url(data:font/ttf;base64,{font_base64}) format('truetype');
    }}
    
    /* Apply font to translation result and specific headers */
    .marathi-text {{
        font-family: 'Lohit Marathi', sans-serif !important;
        font-size: 24px !important;
    }}
    
    h1, h2, h3, .stSubheader {{
        font-family: 'Lohit Marathi', sans-serif !important;
    }}
    </style>
    """
    st.markdown(font_style, unsafe_allow_html=True)

st.title("🚩 मराठी सेतू (Marathi Setu)")
st.subheader("Bridging Languages with AI")

# Sidebar for language choice
st.sidebar.title("Settings")
source_lang = st.sidebar.selectbox("Select Input Language", ["English", "Hindi", "Spanish", "French"])
lang_map = {"English": "en", "Hindi": "hi", "Spanish": "es", "French": "fr"}

# Voice Selection
voice_gender = st.sidebar.selectbox("Select Voice Gender", ["Female", "Male"])
voice_map = {
    "Female": "mr-IN-AarohiNeural",
    "Male": "mr-IN-ManoharNeural"
}

# Layout
col1, col2 = st.columns(2)

with col1:
    st.write(f"### Speak or Type in {source_lang}")
    user_input = st.text_input("Enter text here:")
    
    if st.button("Listen 🎙️"):
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                st.info("Listening...")
                audio = r.listen(source, timeout=5)
                user_input = r.recognize_google(audio, language=lang_map[source_lang])
        except Exception as e:
            st.error(f"Error: {e}")

async def generate_audio(text, voice):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("trans.mp3")

with col2:
    if user_input:
        # Translate
        translated = GoogleTranslator(source='auto', target='mr').translate(user_input)
        if not translated:
            st.error("Translation failed. Please try different text.")
        else:
            st.write("### मराठी भाषांतर:")
            st.markdown(f'<div class="marathi-text"><b>{translated}</b></div>', unsafe_allow_html=True)
            st.write("") # Add some spacing
            
            # Audio
            voice = voice_map[voice_gender]
            with st.spinner("Generating audio..."):
                try:
                    # Clear old audio file to avoid confusion if generation fails
                    if os.path.exists("trans.mp3"):
                        os.remove("trans.mp3")
                        
                    asyncio.run(generate_audio(translated, voice))
                    
                    if os.path.exists("trans.mp3"):
                        st.audio("trans.mp3")
                    else:
                        st.error("Audio file was not generated.")
                except Exception as e:
                    st.error(f"TTS Error: {e}")
                    st.info("Tip: Check your internet connection or try a shorter sentence.")