import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from streamlit_mic_recorder import speech_to_text
import io

st.set_page_config(page_title="Marathi Setu", page_icon="🚩", layout="wide")

# Custom CSS to make it look "Sohla" ready
st.markdown("""
    <style>
    .main { background-color: #fff5e6; }
    .stButton>button { background-color: #ff4b4b; color: white; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚩 मराठी सेतू (Marathi Setu)")
st.write("Type or Speak to see the magic of Marathi! | टाइप करा किंवा बोला.")

# Sidebar Settings
source_lang = st.sidebar.selectbox("Input Language / भाषा निवडा", ["English", "Hindi", "French"])
lang_map = {"English": "en", "Hindi": "hi", "French": "fr"}

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🗣️ Input (इंग्रजी/हिंदी)")
    
    # 1. Voice Option
    v_input = speech_to_text(
        language=lang_map[source_lang],
        start_prompt="🎙️ Start Speaking",
        stop_prompt="🛑 Stop",
        key='STT'
    )
    
    # 2. Typing Option
    t_input = st.text_area("Or type here / किंवा येथे टाइप करा:", height=150, placeholder="Enter text...")

    # Logic: Priority to Voice, then Text
    final_input = v_input if v_input else t_input

with col2:
    st.markdown("### 🚩 Marathi Output (मराठी)")
    
    if final_input:
        with st.spinner('Translating...'):
            # Translate
            translated = GoogleTranslator(source='auto', target='mr').translate(final_input)
            
            # Display text in a nice box
            st.success(f"**{translated}**")
            
            # Generate and Play Audio
            tts = gTTS(text=translated, lang='mr')
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            st.audio(audio_fp, format='audio/mp3')
            
            # Button to clear
            if st.button("Clear / साफ करा"):
                st.rerun()
    else:
        st.info("Waiting for your input... | तुमच्या शब्दांची वाट पाहत आहे...")