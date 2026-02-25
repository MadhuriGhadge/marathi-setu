import streamlit as st
from streamlit_mic_recorder import speech_to_text
from deep_translator import GoogleTranslator
import edge_tts
import asyncio
import base64
import os
import io
import easyocr
import numpy as np
from PIL import Image

st.set_page_config(page_title="Marathi Setu", page_icon="🚩", layout="wide")

# --- Premium UI & Font Logic ---
@st.cache_data
def get_base64_font(font_path):
    if os.path.exists(font_path):
        with open(font_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# Path for your font file
font_file = os.path.join("lohit-marathi-regular", "Lohit Marathi Regular", "Lohit Marathi Regular.ttf")
font_base64 = get_base64_font(font_file)

font_face_css = ""
if font_base64:
    font_face_css = f"""
    @font-face {{
        font-family: 'Lohit Marathi';
        src: url(data:font/ttf;base64,{font_base64}) format('truetype');
    }}
    """

st.markdown(f"""
    <style>
    {font_face_css}
    
    .main {{
        background: linear-gradient(135deg, #fff5e6 0%, #ffebcc 100%);
    }}
    
    .stApp {{
        font-family: 'Lohit Marathi', sans-serif !important;
    }}
    
    .marathi-card {{
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin-bottom: 20px;
    }}
    
    .marathi-text-result {{
        font-family: 'Lohit Marathi', sans-serif !important;
        font-size: 28px !important;
        color: #d35400;
        font-weight: bold;
        line-height: 1.4;
    }}
    
    .stButton>button {{
        background: linear-gradient(45deg, #ff4b4b, #ff7675);
        color: white;
        border-radius: 50px;
        padding: 0.6rem 2rem;
        border: none;
        transition: all 0.3s ease;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
    }}
    
    h1, h2, h3 {{
        color: #c0392b !important;
        font-family: 'Lohit Marathi', sans-serif !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- Logic for TTS ---
async def text_to_speech_edge(text, voice_name):
    communicate = edge_tts.Communicate(text, voice_name)
    audio_data = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]
    return audio_data

# --- Main App ---
st.title("मराठी सेतू (Marathi Setu)")
st.write("Bridging Languages with a Premium Touch | शब्दांना जोडूया, भाषा सांधूया.")

# Sidebar Settings
st.sidebar.markdown("### ⚙️ Settings / सेटिंग्ज")
source_lang_choice = st.sidebar.selectbox("Input Language / भाषा निवडा", ["English", "Hindi", "French"])
lang_map = {"English": "en", "Hindi": "hi", "French": "fr"}

voice_gender = st.sidebar.selectbox("Select Voice / आवाज निवडा", ["Female (Aarohi)", "Male (Manohar)"])
voice_map = {
    "Female (Aarohi)": "mr-IN-AarohiNeural",
    "Male (Manohar)": "mr-IN-ManoharNeural"
}

# OCR Reader initialization (Cached to improve speed)
@st.cache_resource
def load_ocr():
    return easyocr.Reader(['en', 'hi'])

reader = load_ocr()

# --- TABBED INTERFACE ---
tab1, tab2 = st.tabs(["🎙️ Voice & Text", "📸 Scan Image (OCR)"])

# --- TAB 1: VOICE & TEXT ---
with tab1:
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown('<div class="marathi-card">', unsafe_allow_html=True)
        st.markdown("### Input (इंग्रजी/हिंदी)")
        v_input = speech_to_text(
            language=lang_map[source_lang_choice],
            start_prompt="🎙️ Start Speaking",
            stop_prompt="🛑 Stop",
            key='STT_MAIN'
        )
        t_input = st.text_input("Or type here:", key="txt_input")
        translate_btn = st.button("Translate", key="btn_translate")
        st.markdown('</div>', unsafe_allow_html=True)

        final_input = v_input if v_input else (t_input if translate_btn else None)

    with col2:
        st.markdown('<div class="marathi-card">', unsafe_allow_html=True)
        st.markdown("### Marathi Output")
        if final_input:
            with st.spinner('Translating...'):
                translated = GoogleTranslator(source='auto', target='mr').translate(final_input)
                st.markdown(f'<p class="marathi-text-result">{translated}</p>', unsafe_allow_html=True)
                selected_voice = voice_map[voice_gender]
                audio_bytes = asyncio.run(text_to_speech_edge(translated, selected_voice))
                st.audio(audio_bytes, format='audio/mp3')
        else:
            st.info("Waiting for input...")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 2: OCR SCANNER ---
with tab2:
    st.markdown('<div class="marathi-card">', unsafe_allow_html=True)
    st.markdown("### 📸 Scan Document / फोटो काढा")
    uploaded_file = st.file_uploader("Upload Image (English/Hindi Text)", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Target Document", width=350)
        
        if st.button("Read & Translate Document"):
            with st.spinner('AI is reading the page...'):
                img_np = np.array(img)
                results = reader.readtext(img_np, detail=0)
                extracted_text = " ".join(results)
                
                if extracted_text:
                    st.write(f"**Extracted Text:** {extracted_text}")
                    # Translate OCR result
                    ocr_translated = GoogleTranslator(source='auto', target='mr').translate(extracted_text)
                    st.markdown(f'<p class="marathi-text-result">{ocr_translated}</p>', unsafe_allow_html=True)
                    
                    # Voice for OCR
                    selected_voice = voice_map[voice_gender]
                    audio_bytes = asyncio.run(text_to_speech_edge(ocr_translated, selected_voice))
                    st.audio(audio_bytes, format='audio/mp3')
                else:
                    st.warning("No text detected in the image.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Made with ❤️ | मराठी सेतू ")