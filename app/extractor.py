import fitz  # PyMuPDF

def extract_sections_from_pdf(pdf_path, filename):
    # Open the PDF document using PyMuPDF***
    doc = fitz.open(pdf_path)
    sections = []

    # Go through each page in the PDF***
    for i, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]

        # Loop through all text blocks on the page***
        for block in blocks:
            for line in block.get("lines", []):
                # Combine all text spans into a single line***
                text = " ".join([span["text"] for span in line["spans"]])

                # Skip short or empty lines***
                if len(text.strip()) > 10:
                    sections.append({
                        "document": filename,
                        "page_number": i + 1,
                        "text": text.strip()
                    })

    return sections

