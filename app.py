import streamlit as st
import google.generativeai as genai


# CONFIGURE GEMINI API

API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


# PAGE SETTINGS

st.set_page_config(
    page_title="AI Study Notes Generator",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Study Notes Generator")
st.write("Generate Notes, Flashcards and Quiz Questions instantly.")


# USER INPUT

topic = st.text_input(
    "Enter a Topic",
    placeholder="Example: Operating Systems"
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)


# GENERATE BUTTON

if st.button("Generate"):

    if topic == "":
        st.warning("Please enter a topic.")
    else:

        with st.spinner("Generating content..."):

            prompt = f"""
            Topic: {topic}

            Difficulty Level: {difficulty}

            Generate:

            1. Detailed study notes
            2. Key concepts
            3. 5 Flashcards (Question → Answer)
            4. 5 Multiple Choice Questions with answers
            5. Quick Revision Summary

            Format everything clearly using headings.
            """

            response = model.generate_content(prompt)

            st.success("Done!")

            st.markdown(response.text)

            st.download_button(label="📥 Download Notes",data=response.text,file_name=f"{topic}_notes.txt",mime="text/plain")

# FOOTER

st.divider()
st.caption("Built using Python, Streamlit and Gemini AI")
