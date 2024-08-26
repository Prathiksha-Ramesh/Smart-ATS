import os
import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
from PyPDF2 import PdfReader

from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
#gemini pro response:
def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=PdfReader(uploaded_file)
    text=''
    for page_num in range(len(reader.pages)):
        page=reader.pages[page_num]
        text+=str(page.extract_text())
    return text

#prompt template

input_prompt="""
Hey act like a skilled or very experience ATS(Application Tracking system) with a deep 
understanding of tech field,software engineering,data science,data analyst and big data engineer.
Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide best 
assistance for improving the resume.Assign the percentage matching based on Jd and the 
missing keywords with high accuracy.Analyse the portfolio if any in the resume and give the results 
based on it"
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{'JD Match':'%',Missingkeywords:[]','Profile summary':''}}"""


st.title('Smart ATS')
st.text('Improve Your Resume ATS')
jd=st.text_area("Paste the job description")
uploaded_file=st.file_uploader('Upload your resume',type='pdf',help='Please upload the pdf')

submit=st.button('submit')
                       
if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)
        

