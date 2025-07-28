def extract_subsection_info(section):
    summary = section["text"][:300] + "..." if len(section["text"]) > 300 else section["text"]
    return {
        "document": section["document"],
        "page_number": section["page_number"],
        "refined_text": summary
    }
