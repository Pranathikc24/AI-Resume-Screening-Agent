from pathlib import Path
import pymupdf
from docx import Document


def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF resume.
    """

    text = []

    document = pymupdf.open(file_path)

    for page in document:
        page_text = page.get_text()

        if page_text:
            text.append(page_text)

    document.close()

    return "\n".join(text)


def extract_text_from_docx(file_path):
    """
    Extract text from a DOCX resume.
    """

    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text)

    return "\n".join(paragraphs)


def extract_text_from_txt(file_path):
    """
    Extract text from a TXT resume.
    """

    return Path(file_path).read_text(
        encoding="utf-8",
        errors="ignore"
    )


def extract_resume_text(file_path):
    """
    Automatically detect the file type
    and extract the resume text.
    """

    file_path = Path(file_path)

    extension = file_path.suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension == ".docx":
        return extract_text_from_docx(file_path)

    elif extension == ".txt":
        return extract_text_from_txt(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )