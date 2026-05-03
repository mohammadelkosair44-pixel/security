#commit by mohammed hatem
import PyPDF2
import os
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
def read_pdf(file_path):
    file_path = file_path.strip().strip('"').strip("'")

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return ""

    text = ""

    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)

            for page in reader.pages:
                try:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n"
                except Exception as e:
                    print(f"Skipped a page: {e}")

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

    return text
#commit by mohamed ehab
    def parse_questions(text):
    questions = []
    blocks = text.split("[LEVEL:")

    for block in blocks[1:]:
        try:
            lines = block.strip().split("\n")
            level = lines[0].replace("]", "").strip().lower()

            q = ""
            choices = []
            answer = ""

            for line in lines[1:]:
                line = line.strip()

                if line.startswith("Q:"):
                    q = line.replace("Q:", "").strip()

                elif line.startswith(("A)", "B)", "C)", "D)")):
                    choices.append(line)

                elif line.startswith("ANSWER:"):
                    answer = line.replace("ANSWER:", "").strip()

            if q and len(choices) >= 2:
                questions.append({
                    "question": q,
                    "choices": choices,
                    "answer": answer if answer else "N/A",
                    "level": level
                })

        except Exception:
            continue

    return questions
    #commit by Mahmoud Ali
    \import random

def filter_by_range(questions, start, end):
    if start < 1 or end > len(questions) or start > end:
        print("Invalid range!")
        return []
    return questions[start-1:end]


def select_questions(questions, level, num):
    filtered = [q for q in questions if q["level"] == level]

    if not filtered:
        print("No questions found for this level!")
        return []

    num = min(num, len(filtered))
    return random.sample(filtered, num)
