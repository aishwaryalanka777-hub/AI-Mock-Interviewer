def generate_questions(resume_text):

    questions = []

    resume_lower = resume_text.lower()

    # HR Questions
    questions.append("1. Tell me about yourself.")
    questions.append("2. Why should we hire you?")
    questions.append("3. Describe a challenge you faced.")

    # Skill-Based Questions

    if "python" in resume_lower:
        questions.append("4. Explain your experience with Python.")

    if "machine learning" in resume_lower:
        questions.append("5. Explain a machine learning algorithm you used.")

    if "streamlit" in resume_lower:
        questions.append("6. Why did you choose Streamlit for your project?")

    if "opencv" in resume_lower:
        questions.append("7. Explain how OpenCV works in your project.")

    if "tensorflow" in resume_lower:
        questions.append("8. Explain TensorFlow and its usage.")

    if "nlp" in resume_lower:
        questions.append("9. Explain your NLP workflow.")

    # Project Questions

    questions.append("10. Explain one project from your resume.")
    questions.append("11. What improvements would you make to your projects?")
    questions.append("12. What was the hardest bug you faced?")

    return "\n\n".join(questions)