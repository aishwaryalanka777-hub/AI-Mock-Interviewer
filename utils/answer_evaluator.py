def evaluate_answer(answer):

    score = 0
    feedback = []

    word_count = len(answer.split())

    if word_count > 20:
        score += 4
        feedback.append("Good detailed answer.")
    else:
        feedback.append("Answer is too short.")

    if "project" in answer.lower():
        score += 2
        feedback.append("Good use of project explanation.")

    if "python" in answer.lower():
        score += 2
        feedback.append("Technical skill mentioned.")

    if "experience" in answer.lower():
        score += 2
        feedback.append("Good communication of experience.")

    return score, feedback