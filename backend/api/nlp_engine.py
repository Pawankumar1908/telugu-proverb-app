import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/proverbs.csv")

proverbs = df.to_dict(orient="records")

for p in proverbs:
    p["keywords"] = [k.strip().lower() for k in p["keywords"].split(",")]

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
embeddings = pickle.load(open("data/embeddings.pkl", "rb"))

def keyword_search(q):
    q = q.lower()
    return [p for p in proverbs if q in p["keywords"]]

def semantic_search(text):
    vec = model.encode([text])
    scores = cosine_similarity(vec, embeddings)[0]
    top = scores.argsort()[-3:][::-1]
    return [proverbs[i] for i in top]
