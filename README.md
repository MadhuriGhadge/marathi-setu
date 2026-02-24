# 🚩 मराठी सेतू (Marathi Setu)

**Marathi Setu** is a premium, AI-powered language bridge designed to seamlessly translate multiple languages into Marathi with high-fidelity neural voice playback.

---

## ✨ Features

- **Multi-Language Translation**: Translate from **English, Hindi, and French** into Marathi using advanced AI models.
- **Voice & Text Input**: 
  - **Speech-to-Text**: Simply click to speak and let the app transcribe your words.
  - **Text Input**: Type manually if you prefer.
- **Neural Text-to-Speech (TTS)**: Experience crystal-clear, natural-sounding Marathi speech with two distinct voices:
  - **Aarohi (Female)**: A smooth, friendly neural voice.
  - **Manohar (Male)**: A clear, professional neural voice.
- **Premium UI/UX**:
  - **Lohit Marathi Font**: Native font integration for a clean, traditional look.
  - **Glassmorphism Design**: Modern, semi-transparent "cards" for a sleek interface.
  - **Responsive Layout**: Optimized for both desktop and mobile viewing.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- An internet connection (for translation and neural voice generation)

### Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone <repository-url>
   cd marathisetu
   ```

2. **Install dependencies**:
   ```bash
   pip install streamlit streamlit-mic-recorder deep-translator edge-tts
   ```

3. **Font Setup**:
   Ensure the `lohit-marathi-regular` folder is present in the root directory to enable the native Marathi font.

---

## 🎮 How to Use

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```
2. **Select Input Language**: Use the sidebar to choose between English, Hindi, or French.
3. **Select Voice**: Choose between Aarohi (Female) or Manohar (Male) for the audio output.
4. **Input Text**: 
   - Click the 🎙️ **Start Speaking** button to use your microphone.
   - Or type in the text box and click **Translate**.
5. **Listen**: The translated Marathi text will appear, and the audio will play automatically.

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) - The fastest way to build and share data apps.
- [Deep Translator](https://github.com/nidhaloff/deep-translator) - Flexible translation tool.
- [Edge-TTS](https://github.com/rany2/edge-tts) - Microsoft Edge neural TTS interface.
- [Streamlit Mic Recorder](https://github.com/theevas/streamlit_mic_recorder) - For high-quality voice capture.

---

## ❤️ Credits

Made with ❤️ for the Marathi language.  
*शब्दांना जोडूया, भाषा सांधूया.*
