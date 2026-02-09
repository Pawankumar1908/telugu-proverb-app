from fastapi import APIRouter
from api.nlp_engine import keyword_search, semantic_search

router = APIRouter()

@router.post("/chat")
def chat(message: str):
    if len(message.split()) <= 3:
        results = keyword_search(message)
    else:
        results = semantic_search(message)

    return [
        {
            "proverb_telugu": p["proverb_telugu"],
            "proverb_english": p["proverb_english"],
            "meaning": p["meaning"]
        }
        for p in results
    ]
