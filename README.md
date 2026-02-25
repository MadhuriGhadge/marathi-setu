# मराठी सेतू (Marathi Setu)

**Marathi Setu** is a premium, AI-powered language bridge designed to seamlessly translate text, voice, and documents into Marathi with high-fidelity neural voice playback.

[Try it out here](https://marathi-setu.streamlit.app/)

---

## ✨ Features

- **Multi-Language Translation**: Translate from **English, Hindi, and French** into Marathi using advanced AI.
- **🎙️ Voice & Text Tab**:
  - **Speech-to-Text**: Real-time voice capture with high-quality transcription.
  - **Text Input**: Direct typing for quick translations.
- **📸 OCR Document Scanner Tab**:
  - **Vision AI**: Upload images or photos of documents (English/Hindi) and let the AI extract and translate the text instantly.
- **🔊 Neural Text-to-Speech (TTS)**: Natural-sounding Marathi speech with two distinct voices:
  - **Aarohi (Female)**: A smooth, friendly neural voice.
  - **Manohar (Male)**: A clear, professional neural voice.
- **💎 Premium UI/UX**:
  - **Lohit Marathi Font**: Native font integration for traditional Marathi typography.
  - **Glassmorphism Design**: Modern, semi-transparent interface with smooth animations.
  - **Responsive Layout**: Optimized for desktop, tablets, and mobile.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Internet connection (for Translation, Neural TTS, and OCR model download)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd marathisetu
   ```

2. **Install dependencies**:
   ```bash
   pip install streamlit streamlit-mic-recorder deep-translator edge-tts easyocr pillow numpy
   ```

3. **Font Setup**:
   The native Marathi font is included in the `lohit-marathi-regular` directory and is automatically loaded by the app.

---

## 🎮 How to Use

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```
2. **Settings**: Use the sidebar to select your input language and your preferred voice (Aarohi or Manohar).
3. **Translate**:
   - **Voice**: In the first tab, click 🎙️ **Start Speaking**.
   - **Text**: Type in the box and hit **Translate**.
   - **OCR**: Switch to the **Scan Image** tab, upload a document, and click **Read & Translate**.
4. **Listen**: Every translation generates a high-quality audio clip which plays automatically.

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) - App framework.
- [Deep Translator](https://github.com/nidhaloff/deep-translator) - Core translation engine.
- [Edge-TTS](https://github.com/rany2/edge-tts) - Microsoft Azure neural voices.
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) - Powerful multi-language optical character recognition.
- [Streamlit Mic Recorder](https://github.com/theevas/streamlit_mic_recorder) - Professional voice capture.

---

## ❤️ Credits

Made with ❤️ for the Marathi language.  
*शब्दांना जोडूया, भाषा सांधूया.*
