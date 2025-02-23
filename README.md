
# 📚 Grading Buddy: AI-Powered PDF Grading App

Grading Buddy is an AI-powered web application built using **Streamlit**, **OpenAI's GPT-3.5-turbo**, and **PyPDF2** that automates the process of grading student answers based on a professor's answer key. This tool streamlines the evaluation process by reading PDFs of both professor-provided answers and student responses, providing detailed feedback, grades, and lost points.

---

## 🛠️ Features

- **PDF Parsing**: Extracts text from uploaded PDFs using `PyPDF2`.
- **AI-Powered Grading**: Leverages OpenAI's GPT-3.5-turbo model to compare student answers with professor-provided answers.
- **User-Friendly Interface**: Built with Streamlit, the app provides an easy-to-use interface for professors to upload their questions/answers and student responses.
- **Customizable Grading**: Professors can set the total points, and the app provides detailed feedback, grades, and areas where students lost points.
- **Custom Styling**: Includes CSS customization for a clean and professional look.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- [OpenAI API Key](https://beta.openai.com/signup/)
- Libraries: `streamlit`, `PyPDF2`, `openai`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/grading-buddy.git
    cd grading-buddy
    ```
2. Install the required packages

3. Set your OpenAI API key:
    - In the code, replace `INPUT_YOUR_KEY_HERE` with your actual OpenAI API key.

### Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the app in your browser at `http://localhost:8501` or let it automatically open up in your browser

3. Upload the professor's questions/answers in PDF format and student answers in PDF format.

4. Set the total grading points, and click the "Grade Answers" button to get the results.

---

## 💻 Code Overview

### Key Functions

- **`extract_text_from_pdf(pdf_file)`**: Extracts text from a given PDF file using `PyPDF2`.
- **`compare_answers(student_answer, professor_answer, total_points)`**: Uses OpenAI's GPT-3.5-turbo model to compare the student's answer with the professor's answer, providing a grade, lost points, and feedback.

### Streamlit App
- The app provides an intuitive interface for uploading PDFs and setting grading parameters.
- Custom CSS is used to give the app a clean and professional look.

---

## 🎨 Custom Styling

The app includes custom CSS to enhance the visual appeal of the Streamlit interface. You can modify the colors and styles in the `custom_css` section of the code.


---

## 🌟 Acknowledgements

- [OpenAI](https://openai.com) for providing the GPT-3.5-turbo model.
- [Streamlit](https://streamlit.io) for the easy-to-use web framework.
- [PyPDF2](https://pypdf2.readthedocs.io/) for handling PDF extraction.

---

## 📧 Contact

For questions or support, reach out at jartaresbizz@gmail.com.

---

Feel free to modify the sections, especially the repo link and contact information, before publishing it to GitHub!
