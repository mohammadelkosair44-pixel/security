#commit mohammed hatem
import PyPDF2
import os

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
  
