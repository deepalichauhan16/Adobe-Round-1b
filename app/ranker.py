from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("./models/all-MiniLM-L6-v2")

def rank_sections(sections, persona, job):
    job_context = f"{persona}. Task: {job}"
    job_embedding = model.encode(job_context)

    for section in sections:
        section_embedding = model.encode(section["text"])
        score = cosine_similarity([job_embedding], [section_embedding])[0][0]
        section["similarity"] = score

    ranked = sorted(sections, key=lambda x: x["similarity"], reverse=True)
    for i, section in enumerate(ranked):
        section["importance_rank"] = i + 1
    return ranked[:10]
