import streamlit as st
from googletrans import Translator
from constant import LANGUAGES

translator = Translator()

st.title("🌍 Simple AI-Powered Language Translator")

language_options = list(LANGUAGES.values())
language_codes = list(LANGUAGES.keys())

text = st.text_area("Enter text to translate:")
src_lang_name = st.selectbox("Source Language", language_options, index=language_codes.index('en'))
src_lang = language_codes[language_options.index(src_lang_name)]

dest_lang_name = st.selectbox("Target Language", language_options, index=language_codes.index('id'))
dest_lang = language_codes[language_options.index(dest_lang_name)]

if st.button("Translate"):
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text
    st.write("### Translated Text")
    st.success(translated_text)