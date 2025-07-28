def extract_subsection_info(section):
    # If the section text is long, trim it to the first 300 characters***
    summary = section["text"][:300] + "..." if len(section["text"]) > 300 else section["text"]

    # Return the key details with the trimmed text***
    return {
        "document": section["document"],
        "page_number": section["page_number"],
        "refined_text": summary
    }
