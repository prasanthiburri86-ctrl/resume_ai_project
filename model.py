from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_similarity(resume_text, job_desc):
    emb1 = model.encode([resume_text])
    emb2 = model.encode([job_desc])
    score = np.dot(emb1, emb2.T)
    return float(score[0][0])