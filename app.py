import streamlit as st
from streamlit_mic_recorder import speech_to_text
from deep_translator import GoogleTranslator
from gtts import gTTS
import base64
import os
import io

st.set_page_config(page_title="Marathi Setu", page_icon="🚩")

# --- Custom Font Logic ---
@st.cache_data
def get_base64_font(font_path):
    with open(font_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

font_file = os.path.join("lohit-marathi-regular", "Lohit Marathi Regular", "Lohit Marathi Regular.ttf")

if os.path.exists(font_file):
    font_base64 = get_base64_font(font_file)
    font_style = f"""
    <style>
    @font-face {{
        font-family: 'Lohit Marathi';
        src: url(data:font/ttf;base64,{font_base64}) format('truetype');
    }}
    .marathi-text {{
        font-family: 'Lohit Marathi', sans-serif !important;
        font-size: 24px !important;
    }}
    h1, h2, h3, .stSubheader, p, div {{
        font-family: 'Lohit Marathi', sans-serif !important;
    }}
    </style>
    """
    st.markdown(font_style, unsafe_allow_html=True)
# -------------------------

st.title("🚩 मराठी सेतू (Marathi Setu)")
st.write("सुरु करण्यासाठी खालील बटण दाबा आणि इंग्रजी किंवा हिंदीत बोला.")

# This component handles the microphone through the browser perfectly
text = speech_to_text(
    language='en', 
    start_prompt="बोलण्यासाठी क्लिक करा (Click to Speak) 🎙️", 
    stop_prompt="थांबा (Stop) 🛑", 
    key='STT'
)

if text:
    st.info(f"You said: {text}")
    
    # Translation Logic
    with st.spinner('भाषांतर करत आहे...'):
        translated = GoogleTranslator(source='auto', target='mr').translate(text)
        st.write("### मराठी भाषांतर:")
        st.markdown(f'<div class="marathi-text"><b>{translated}</b></div>', unsafe_allow_html=True)
        
        # Voice Logic
        tts = gTTS(text=translated, lang='mr')
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        st.audio(audio_fp, format='audio/mp3')
        st.caption("वरील प्लेअरमध्ये आवाज ऐका")