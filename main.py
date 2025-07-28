import os
import json
from datetime import datetime
from app.ranker import rank_sections
from app.summarizer import extract_subsection_info
from app.utils import load_persona_job
from app.extractor import extract_sections_from_pdf

def main():
    # Define the folders for input PDFs and output results***
    input_dir = "/app/input"
    output_dir = "/app/output"

    # Load the persona and job-to-be-done from input***
    persona, job = load_persona_job(input_dir)

    # Get a list of all PDF files in the input directory**
    files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

    all_sections = []
    for file in files:
        path = os.path.join(input_dir, file)
        # Extract all text sections from the current PDF***
        all_sections.extend(extract_sections_from_pdf(path, file))

    # Rank the sections based on how relevant they are to the persona and job***
    top_sections = rank_sections(all_sections, persona, job)

    # Further extract insights from the top-ranked sections***
    subsections = [extract_subsection_info(s) for s in top_sections]

    # Package everything into a structured output JSON***
    output = {
        "metadata": {
            "input_documents": files,
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [{
            "document": s["document"],
            "section_title": s["text"][:60],
            "importance_rank": s["importance_rank"],
            "page_number": s["page_number"]
        } for s in top_sections],
        "subsection_analysis": subsections
    }

    # Save the output to a JSON file in the output folder***
    with open(os.path.join(output_dir, "output.json"), "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()
