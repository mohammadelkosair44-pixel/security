#Commit by Mohammed Hatem

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
    
#Commit by Mohamed Ehab
    
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
    
 #Commit by Mahmoud Ali

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
    
#Commit by Feras Nofal 

def create_exam_pdf(questions, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph("<b>Final Exam</b>", styles['Title']))
    content.append(Spacer(1, 20))

    for i, q in enumerate(questions, 1):
        content.append(Paragraph(f"Q{i}: {q['question']}", styles['Normal']))
        content.append(Spacer(1, 10))

        for choice in q["choices"]:
            content.append(Paragraph(choice, styles['Normal']))
            content.append(Spacer(1, 5))

        content.append(Spacer(1, 15))

    doc.build(content)


def create_answer_pdf(questions, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph("<b>Answer Sheet</b>", styles['Title']))
    content.append(Spacer(1, 20))

    for i, q in enumerate(questions, 1):
        content.append(Paragraph(f"Q{i}: {q['answer']}", styles['Normal']))
        content.append(Spacer(1, 10))

    doc.build(content)
    
#Commit by Abdelrhman Magdi

def main():
    print("===== Advanced Exam Generator =====")

    file_path = input("Enter PDF file path: ")
    pdf_text = read_pdf(file_path)

    if not pdf_text.strip():
        print("Empty or unreadable PDF!")
        return

    questions = parse_questions(pdf_text)

    if not questions:
        print("No valid questions found!")
        return

    print(f"Total questions: {len(questions)}")

    use_range = input("Use range? (y/n): ").lower()

    if use_range == 'y':
        try:
            start = int(input("Start: "))
            end = int(input("End: "))
            questions = filter_by_range(questions, start, end)

            if not questions:
                return
        except:
            print("Invalid input!")
            return

    levels = sorted(set(q["level"] for q in questions))

    print("\nAvailable Levels:")
    for lvl in levels:
        print(f"- {lvl}")

    level = input("\nEnter level: ").strip().lower()

    if level not in levels:
        print("Invalid level!")
        return

    try:
        num = int(input("Number of questions: "))
    except:
        print("Invalid number!")
        return

    selected = select_questions(questions, level, num)

    if not selected:
        return

    random.shuffle(selected)

    create_exam_pdf(selected, "exam.pdf")
    create_answer_pdf(selected, "answers.pdf")

    print("\nDone! Files created.")

if _name_ == "_main_":
    main()
