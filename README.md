# 🎓 Advanced Exam Generator

Advanced Exam Generator is a Python-based project that automatically creates professional exam PDFs and answer sheets from a question bank stored inside a PDF file.

The system supports:
- Question difficulty levels
- Random question selection
- Question range filtering
- Automatic PDF generation

---

# 🚀 Features

✅ Read questions directly from PDF files  
✅ Support multiple difficulty levels:
- Easy
- Medium
- Hard

✅ Randomly generate exams  
✅ Generate separate answer sheets  
✅ Filter questions using custom ranges  
✅ Clean and organized PDF output  

---

# 🛠️ Technologies Used

- Python
- PyPDF2
- ReportLab
- Random Module
- OS Module

---

# 📦 Requirements

Install the required libraries before running the project:

```bash
pip install PyPDF2 reportlab
```

---

# 📁 Project Structure

```text
project/
│
├── exam_generator.py
├── README.md
├── questions.pdf
├── exam.pdf
└── answers.pdf
```

---

# 📝 Question Format

The PDF file must contain questions using the following format:

```text
[LEVEL: easy]
Q: What is 2 + 2?
A) 3
B) 4
C) 5
D) 6
ANSWER: B

[LEVEL: medium]
Q: What is the capital of Egypt?
A) Cairo
B) Giza
C) Alexandria
D) Luxor
ANSWER: A
```

---

# ▶️ How To Run

Run the program using:

```bash
python exam_generator.py
```

---

# ⚙️ Program Workflow

1. Enter the PDF file path
2. Questions are extracted from the PDF
3. Choose whether to use a custom range
4. Select question difficulty level
5. Enter the number of questions
6. The program generates:
   - exam.pdf
   - answers.pdf

---

# 📄 Output Files

## exam.pdf
Contains the generated exam questions.

## answers.pdf
Contains the correct answers for all generated questions.

---

# 💡 Example

```bash
===== Advanced Exam Generator =====

Enter PDF file path:
C:\Users\User\Desktop\questions.pdf

Total questions: 50

Use range? (y/n): y

Start: 1
End: 20

Available Levels:
- easy
- medium
- hard

Enter level: easy

Number of questions: 5

Done! Files created.
```

---

# 👨‍💻 Team Contributions

| Team Member | Contribution |
|-------------|--------------|
| Mohammed Hatem | Project Integration |
| Mohamed Ehab | Question Parsing |
| Mahmoud Ali | Filtering & Selection |
| Feras Nofal | PDF Generation |
| Abdelrhman Magdi | PDF Reading & Main Logic |

---

# ⚠️ Notes

- The PDF file must not be empty.
- Invalid questions are skipped automatically.
- Questions must follow the required format exactly.

---

# 📜 License

This project is made for educational purposes.
