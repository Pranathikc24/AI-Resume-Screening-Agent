from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# LOAD MODEL
# ============================================================

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


# ============================================================
# CREATE EMBEDDING
# ============================================================

def create_embedding(text):
    """
    Convert text into a numerical embedding.
    """

    if not text or not text.strip():
        return None

    embedding = model.encode(
        text,
        convert_to_numpy=True
    )

    return embedding


# ============================================================
# CALCULATE SIMILARITY
# ============================================================

def calculate_similarity(text1, text2):
    """
    Calculate semantic similarity between two texts.

    Returns a score between 0 and 1.
    """

    if not text1 or not text2:
        return 0.0

    embedding1 = create_embedding(text1)

    embedding2 = create_embedding(text2)

    similarity = cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

    return round(float(similarity), 4)


# ============================================================
# CONVERT TO PERCENTAGE
# ============================================================

def similarity_percentage(text1, text2):
    """
    Convert similarity score into percentage.
    """

    score = calculate_similarity(
        text1,
        text2
    )

    return round(score * 100, 2)