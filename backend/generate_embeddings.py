import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer

df = pd.read_csv("data/proverbs.csv")
texts = (df["proverb_telugu"] + " " + df["meaning"]).tolist()

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
embeddings = model.encode(texts)

with open("data/embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)
