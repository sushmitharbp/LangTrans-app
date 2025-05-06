import streamlit as st
from googletrans import Translator
from gtts import gTTS
import base64
import os

# Translator setup
translator = Translator()

# Language mapping
language = {
    "bn": "Bangla", "en": "English", "ko": "Korean", "fr": "French",
    "de": "German", "he": "Hebrew", "hi": "Hindi", "it": "Italian",
    "ja": "Japanese", "la": "Latin", "ms": "Malay", "ne": "Nepali",
    "ru": "Russian", "ar": "Arabic", "zh": "Chinese", "es": "Spanish"
}
language_reverse = {v: k for k, v in language.items()}

# UI layout
st.set_page_config(page_title="🈯 Language Translator", layout="centered")
st.title("🈯 Language Translator")


# Show dropdowns and text input from start
source_lang = st.selectbox("Select Source Language", ["Select Language"] + list(language.values()))
if source_lang != "Select Language":
    source_code = language_reverse[source_lang]

target_lang = st.selectbox("Select Target Language", ["Select Language"] + list(language.values()))
if target_lang != "Select Language":
      target_code = language_reverse[target_lang]

text_input = st.text_area("Enter text to translate:")

# Translate
translated_text = ""
if st.button("Translate"):
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        try:
            source_code = language_reverse[source_lang]
            target_code = language_reverse[target_lang]
            result = translator.translate(text_input, src=source_code, dest=target_code)
            translated_text = result.text
            st.success(f"Translated to {target_lang}:")
            st.write(f"**Input:** {text_input}")
            st.write(f"**Translation:** {translated_text}")
        except Exception as e:
            st.error(f"❌ Error: {e}")


# Footer
st.markdown("---")
