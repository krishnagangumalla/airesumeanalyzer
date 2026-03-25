import streamlit as st
from analyze import analyzer
job_des=st.text_area("Enter the job description")
res_skil=st.text_area("Enter the resume skills")
if st.button("Analyze"):
    if(job_des and res_skil):
        res=analyzer(job_des, res_skil)
        st.write(res)
    else:
        st.write(" enter the job description and resume  skills")
