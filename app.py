import streamlit as st
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter

with st.sidebar:
    st.title('GetAnswers.io')
    st.markdown('''
    The web app is an LLM-powered chatbot built using:
    -[Streamlit]
    -[LangChain]
    -[OpenAI] ''')

    add_vertical_space(5)
    st.write('Made by KnowBrainer.Co')

def main():
    st.header('Get your Answers')
       #upload your question paper pdf file 
    pdf=st.file_uploader("Upload your PYQ pdf",type='pdf')

    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        text=""
        for page in pdf_reader.pages:
            text+=page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=20,
            length_function=len
        ) 
        chunks=text_splitter.split_text(text=text)
        st.write(chunks)   

        #st.write(text)    
    

if __name__=='__main__':
    main()    