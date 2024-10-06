
import streamlit as st
import PyPDF2
import openai
import os


# Set your OpenAI API key
# Create your openAI key from the openAI website and input it to use the API.
openai.api_key = 'INPUT_YOUR_KEY_HERE'

# This function takes in a file and extracts the data from the file
def extract_text_from_pdf(pdf_file):
    text = ""
    reader = PyPDF2.PdfReader(pdf_file)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# This function compares the answers of the professor and the student
def compare_answers(student_answer, professor_answer, total_points):
    # Correct method to use the ChatCompletion API for GPT-3.5-turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                # Change the "content" if you would like exact answers or how you want gpt to check the answers
                "content": f"Grade the following student's answer based on this professor's questions and answers:\n\nProfessors Question and Answers: \n{professor_answer}\n\nStudents Answer: {student_answer}.Format the answer in three sections each on a NEW LINE namely: Grade (in the format \"number\" / {total_points}), Lost points, Question number where they lost points, and Feedback.\n"

            }
        ]
    )

    # Accessing the response correctly for chat models
    return response['choices'][0]['message']['content']

#CSS style to change colors in streamlit
custom_css ="""
<style>
    .stApp {
        background-color: #22333B;  
        color: #EAE0D5;  
    }
    h1 {
        font-family: 'Times New Roman';
        color: #EAE0D5;
    }
    h2, h3 {
        font-family: 'Times New Roman';
        color: #EAE0D5;
    }
    /* You can add more custom styles here */
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
# Streamlit app
st.title("Grading Buddy")

# Upload Professor's PDF
st.subheader("Upload Professor's Questions and Answers")
professor_pdf = st.file_uploader("Upload Professor's PDF", type='pdf')

# Upload Student's PDFs
st.subheader("Upload Student's Answer PDF(s)")
students_pdfs = st.file_uploader("Upload Student's PDF(s)", type='pdf', accept_multiple_files=True)

total_points = st.text_input("How much is it to be graded out of?", 100)
# Button to grade answers
if st.button("Grade Answers"):
    if professor_pdf is not None and students_pdfs:
        # Extract answers from the professor's PDF
        professor_answers = extract_text_from_pdf(professor_pdf)

        results = []
        request_count = 0

        for student_pdf in students_pdfs:
            # Extract answers from the student's PDF
            student_answer = extract_text_from_pdf(student_pdf)

            # Compare and grade answers
            try:
                grade = compare_answers(student_answer, professor_answers,total_points)
                results.append({
                    'student_name': student_pdf.name,
                    'grade': grade
                })

                #If using free version of ChatGPT you will require a

            except Exception as e:
                st.error(f"Error processing {student_pdf.name}: {e}")

        # Display results
        st.subheader("Grading Results")
        for result in results:
            st.write(f"**Student Name**: {result['student_name']}")
            st.write(result['grade'])
    else:
        st.error("Please upload both the professor's PDF and at least one student's PDF.")