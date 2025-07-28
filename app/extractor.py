import fitz  # PyMuPDF

def extract_sections_from_pdf(pdf_path, filename):
    doc = fitz.open(pdf_path)
    sections = []
    for i, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                text = " ".join([span["text"] for span in line["spans"]])
                if len(text.strip()) > 10:
                    sections.append({
                        "document": filename,
                        "page_number": i + 1,
                        "text": text.strip()
                    })
    return sections
