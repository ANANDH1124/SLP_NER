import streamlit as st
import spacy
import spacy_streamlit as spt
nlp=spacy.load('en_core_web_sm')
st.title('Named Entity Recognition APP')
menu_task=['NER','Tokenizer']
choice=st.sidebar.selectbox('selected',menu_task)


if choice=='Named Entity Recognition':
    st.subheader('Named Entity Recognition APP')
    rawtext=st.text_area("TOKENIZE","ENTER TEXT")
    docs=nlp(rawtext)
    if st.button('Recognize'):
        spt.visualize_ner(docs)
elif choice=='Tokenizer':
    st.subheader('TOKENIZER APP')
    rawtext=st.text_area("NER","ENTER TEXT")
    docs=nlp(rawtext)
    if st.button('ENTITY'):
        spt.visualize_tokens(docs)
