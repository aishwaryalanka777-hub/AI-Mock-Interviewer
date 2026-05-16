import streamlit as st

from utils.resume_parser import extract_resume_text
from utils.question_generator import generate_questions
from utils.answer_evaluator import evaluate_answer
from utils.report_generator import generate_report

st.set_page_config(
    page_title="AI Mock Interviewer",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 AI Mock Interviewer")

st.write("Upload your resume and start your AI-powered interview session.")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)

if "questions_generated" not in st.session_state:
    st.session_state.questions_generated = False

if "question_list" not in st.session_state:
    st.session_state.question_list = []

if uploaded_file:

    st.success("Resume uploaded successfully!")

    resume_text = extract_resume_text(uploaded_file)

    st.subheader("Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=250
    )

    if st.button("Generate Interview Questions"):

        questions = generate_questions(resume_text)

        st.session_state.question_list = questions.split("\n\n")

        st.session_state.questions_generated = True

if st.session_state.questions_generated:

    st.subheader("AI Interview Questions")

    total_score = 0

    answers = []

    scores = []

    for i, question in enumerate(st.session_state.question_list):

        st.subheader(question)

        answer = st.text_area(
            f"Your Answer for Question {i+1}",
            key=f"answer_{i}"
        )

        answers.append(answer)

        if answer:

            score, feedback = evaluate_answer(answer)

            scores.append(score)

            total_score += score

            st.success(f"Score: {score}/10")

            st.write("Feedback:")

            for item in feedback:
                st.write(f"- {item}")

        else:
            scores.append(0)

    st.subheader("Final Interview Score")

    st.info(f"Total Score: {total_score}")

    if st.button("Generate Interview Report"):

        filename = "interview_report.pdf"

        generate_report(
            filename,
            st.session_state.question_list,
            answers,
            scores
        )

        st.success("Interview Report Generated!")

        with open(filename, "rb") as pdf_file:

            st.download_button(
                label="Download Report",
                data=pdf_file,
                file_name="AI_Interview_Report.pdf",
                mime="application/pdf"
            )