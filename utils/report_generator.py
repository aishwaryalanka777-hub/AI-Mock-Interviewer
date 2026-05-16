from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_report(filename, questions, answers, scores):

    # Save PDF directly in current directory
    filename = os.path.basename(filename)

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph("AI Mock Interview Report", styles['Title'])

    elements.append(title)

    elements.append(Spacer(1, 20))

    total_score = 0

    for i in range(len(questions)):

        q = Paragraph(
            f"<b>Question:</b> {questions[i]}",
            styles['BodyText']
        )

        a = Paragraph(
            f"<b>Answer:</b> {answers[i]}",
            styles['BodyText']
        )

        s = Paragraph(
            f"<b>Score:</b> {scores[i]}/10",
            styles['BodyText']
        )

        elements.append(q)
        elements.append(a)
        elements.append(s)

        elements.append(Spacer(1, 15))

        total_score += scores[i]

    final_score = Paragraph(
        f"<b>Final Score:</b> {total_score}",
        styles['Heading2']
    )

    elements.append(final_score)

    doc.build(elements)