import os
import json
from datetime import datetime
from app.ranker import rank_sections
from app.summarizer import extract_subsection_info
from app.utils import load_persona_job
from app.extractor import extract_sections_from_pdf


def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    persona, job = load_persona_job(input_dir)
    files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

    all_sections = []
    for file in files:
        path = os.path.join(input_dir, file)
        all_sections.extend(extract_sections_from_pdf(path, file))

    top_sections = rank_sections(all_sections, persona, job)
    subsections = [extract_subsection_info(s) for s in top_sections]

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

    with open(os.path.join(output_dir, "output.json"), "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    main()
