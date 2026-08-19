from src.scoring import (
    calculate_final_score,
    get_recommendation,
    create_screening_result,
    rank_candidates
)


# ============================================================
# TEST 1 — SINGLE CANDIDATE
# ============================================================

skill_score = 100.0
semantic_score = 79.63
experience_score = 50.0
education_score = 100.0


final_score = calculate_final_score(
    skill_score,
    semantic_score,
    experience_score,
    education_score
)


print("=" * 70)
print("FINAL SCORE TEST")
print("=" * 70)

print(
    f"\nSkill Match: "
    f"{skill_score}%"
)

print(
    f"Semantic Similarity: "
    f"{semantic_score}%"
)

print(
    f"Experience Match: "
    f"{experience_score}%"
)

print(
    f"Education Match: "
    f"{education_score}%"
)

print(
    f"\nFINAL SCORE: "
    f"{final_score}%"
)

print(
    f"RECOMMENDATION: "
    f"{get_recommendation(final_score)}"
)


# ============================================================
# TEST 2 — CREATE CANDIDATE RESULT
# ============================================================

candidate_a = create_screening_result(
    "Candidate A",
    100.0,
    79.63,
    50.0,
    100.0
)


candidate_b = create_screening_result(
    "Candidate B",
    80.0,
    75.0,
    100.0,
    100.0
)


candidate_c = create_screening_result(
    "Candidate C",
    60.0,
    70.0,
    50.0,
    100.0
)


# ============================================================
# TEST 3 — RANK CANDIDATES
# ============================================================

candidates = [
    candidate_a,
    candidate_b,
    candidate_c
]


ranked_candidates = rank_candidates(
    candidates
)


print("\n" + "=" * 70)
print("CANDIDATE RANKING")
print("=" * 70)


for position, candidate in enumerate(
    ranked_candidates,
    start=1
):

    print(
        f"\n{position}. "
        f"{candidate['candidate_name']}"
    )

    print(
        f"   Skill Match: "
        f"{candidate['skill_score']}%"
    )

    print(
        f"   Semantic Similarity: "
        f"{candidate['semantic_score']}%"
    )

    print(
        f"   Experience Match: "
        f"{candidate['experience_score']}%"
    )

    print(
        f"   Education Match: "
        f"{candidate['education_score']}%"
    )

    print(
        f"   FINAL SCORE: "
        f"{candidate['final_score']}%"
    )

    print(
        f"   Recommendation: "
        f"{candidate['recommendation']}"
    )