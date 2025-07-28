from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-downloaded sentence transformer model***
model = SentenceTransformer("./models/all-MiniLM-L6-v2")

def rank_sections(sections, persona, job):
    # Combine persona and task into a single context string***
    job_context = f"{persona}. Task: {job}"
    
    # Generate an embedding for the persona + job description**
    job_embedding = model.encode(job_context)

    # Compute similarity score for each section compared to the job context**
    for section in sections:
        section_embedding = model.encode(section["text"])
        score = cosine_similarity([job_embedding], [section_embedding])[0][0]
        section["similarity"] = score

    # Sort sections by similarity in descending order***
    ranked = sorted(sections, key=lambda x: x["similarity"], reverse=True)

    # Assign a rank to each section based on its similarity score***
    for i, section in enumerate(ranked):
        section["importance_rank"] = i + 1

    # Return the top 10 most relevant sections***
    return ranked[:10]
