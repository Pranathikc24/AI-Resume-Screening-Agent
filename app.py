import streamlit as st
from pathlib import Path
import tempfile
import json
import pandas as pd

from src.screening import screen_multiple_resumes


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .main-header {
        padding: 1.5rem;
        border-radius: 15px;
        background: linear-gradient(
            135deg,
            #1e3a8a,
            #2563eb
        );
        color: white;
        margin-bottom: 1.5rem;
    }

    .main-header h1 {
        margin-bottom: 0.3rem;
        font-size: 2.2rem;
    }

    .main-header p {
        margin: 0;
        font-size: 1.05rem;
        opacity: 0.9;
    }

    .info-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        background-color: #ffffff;
        margin-bottom: 1rem;
    }

    .score-card {
        padding: 1.2rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        text-align: center;
        background-color: #f8fafc;
    }

    .score-value {
        font-size: 2rem;
        font-weight: bold;
    }

    .candidate-card {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        margin-bottom: 1rem;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="main-header">
        <h1>🤖 AI Resume Screening Agent</h1>
        <p>
        Intelligent candidate screening, scoring and ranking system
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Screening Settings")

    st.markdown(
        """
        This system analyzes candidate resumes against a
        given job description.
        """
    )

    st.divider()

    st.subheader("📊 Scoring Weights")

    st.write("Skill Match: **40%**")
    st.write("Semantic Similarity: **40%**")
    st.write("Experience: **10%**")
    st.write("Education: **10%**")

    st.divider()

    st.subheader("🧠 AI Components")

    st.write("✓ Resume Parser")
    st.write("✓ Skill Extraction")
    st.write("✓ Skill Matching")
    st.write("✓ Semantic Similarity")
    st.write("✓ Experience Matching")
    st.write("✓ Education Matching")
    st.write("✓ Candidate Ranking")


# ============================================================
# JOB DESCRIPTION SECTION
# ============================================================

st.header("📋 1. Job Description")

job_description = st.text_area(
    "Enter the Job Description",
    height=250,
    placeholder=(
        "Example:\n\n"
        "We are looking for a Python Developer...\n\n"
        "Required skills:\n"
        "Python\n"
        "Django\n"
        "REST API\n"
        "MySQL\n"
        "Git\n\n"
        "Minimum 2 years of experience."
    )
)


# ============================================================
# JOB ROLE
# ============================================================

job_role = st.text_input(
    "Job Role",
    placeholder="Example: Python Developer"
)


# ============================================================
# RESUME UPLOAD
# ============================================================

st.header("📄 2. Upload Candidate Resumes")

uploaded_files = st.file_uploader(
    "Upload candidate resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True,
    help="Upload one or more PDF or DOCX resumes."
)


# ============================================================
# DISPLAY UPLOADED FILES
# ============================================================

if uploaded_files:

    st.success(
        f"{len(uploaded_files)} resume(s) uploaded successfully."
    )

    if len(uploaded_files) >= 10:
        st.success(
            "🎯 10+ resumes uploaded. Batch screening requirement satisfied."
        )

    with st.expander("📁 Uploaded Resumes", expanded=True):

        for file in uploaded_files:
            st.write(f"📄 **{file.name}**")


# ============================================================
# SCREEN BUTTON
# ============================================================

st.header("🔍 3. Screen Candidates")

screen_button = st.button(
    "🚀 Start Resume Screening",
    type="primary",
    use_container_width=True
)


# ============================================================
# HELPER FUNCTION — SCREENING REASONING
# ============================================================

def generate_reasoning(result):

    reasons = []

    skill_score = float(
        result.get("skill_score", 0)
    )

    semantic_score = float(
        result.get("semantic_score", 0)
    )

    experience_score = float(
        result.get("experience_score", 0)
    )

    education_score = float(
        result.get("education_score", 0)
    )

    matched_skills = result.get(
        "matched_skills",
        []
    )

    missing_skills = result.get(
        "missing_skills",
        []
    )

    # Skill reasoning
    if skill_score >= 80:
        reasons.append(
            "Strong alignment with the required skills."
        )

    elif skill_score >= 50:
        reasons.append(
            "Moderate alignment with the required skills."
        )

    else:
        reasons.append(
            "Limited alignment with the required skills."
        )

    # Semantic reasoning
    if semantic_score >= 70:
        reasons.append(
            "Resume content is highly relevant to the job description."
        )

    elif semantic_score >= 50:
        reasons.append(
            "Resume content has moderate relevance to the job description."
        )

    else:
        reasons.append(
            "Resume content has relatively low semantic relevance to the job description."
        )

    # Experience reasoning
    if experience_score >= 100:
        reasons.append(
            "Candidate meets the required experience."
        )

    elif experience_score > 0:
        reasons.append(
            "Candidate partially meets the required experience."
        )

    else:
        reasons.append(
            "Candidate does not meet the required experience."
        )

    # Education reasoning
    if education_score >= 100:
        reasons.append(
            "Candidate meets the required education level."
        )

    else:
        reasons.append(
            "Candidate does not fully meet the required education requirement."
        )

    # Skills reasoning
    if matched_skills:
        reasons.append(
            f"Matched {len(matched_skills)} required skill(s)."
        )

    if missing_skills:
        reasons.append(
            f"Missing {len(missing_skills)} required skill(s)."
        )

    return reasons


# ============================================================
# SCREENING PROCESS
# ============================================================

if screen_button:

    # --------------------------------------------------------
    # Validate Job Description
    # --------------------------------------------------------

    if not job_description.strip():

        st.error(
            "Please enter a Job Description."
        )

        st.stop()


    # --------------------------------------------------------
    # Validate Resume Upload
    # --------------------------------------------------------

    if not uploaded_files:

        st.error(
            "Please upload at least one candidate resume."
        )

        st.stop()


    # --------------------------------------------------------
    # Default Job Role
    # --------------------------------------------------------

    if not job_role.strip():

        job_role = "Resume Screening"


    # --------------------------------------------------------
    # Temporary Directory
    # --------------------------------------------------------

    temp_directory = Path(
        tempfile.mkdtemp(
            prefix="resume_screening_"
        )
    )

    resume_paths = []


    # --------------------------------------------------------
    # Save Uploaded Files
    # --------------------------------------------------------

    for uploaded_file in uploaded_files:

        file_path = (
            temp_directory /
            uploaded_file.name
        )

        with open(
            file_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        resume_paths.append(
            str(file_path)
        )


    # --------------------------------------------------------
    # Run Screening
    # --------------------------------------------------------

    with st.spinner(
        "🤖 AI is analyzing and ranking candidates..."
    ):

        try:

            results = screen_multiple_resumes(
                resume_paths=resume_paths,
                job_description=job_description
            )

        except Exception as e:

            st.error(
                "An error occurred while screening the resumes."
            )

            st.exception(e)

            st.stop()


    # --------------------------------------------------------
    # Check Results
    # --------------------------------------------------------

    if not results:

        st.warning(
            "No screening results were generated."
        )

        st.stop()


    # ========================================================
    # RESULTS
    # ========================================================

    st.success(
        f"Screening completed for {len(results)} candidate(s)."
    )

    st.header("🏆 Screening Results")


    # ========================================================
    # SUMMARY METRICS
    # ========================================================

    strong_matches = 0
    good_matches = 0
    potential_matches = 0
    low_matches = 0

    for result in results:

        recommendation = str(
            result.get(
                "recommendation",
                ""
            )
        ).lower()

        if "strong" in recommendation:

            strong_matches += 1

        elif "good" in recommendation:

            good_matches += 1

        elif "potential" in recommendation:

            potential_matches += 1

        elif "low" in recommendation:

            low_matches += 1


    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "👥 Candidates",
            len(results)
        )

    with col2:

        st.metric(
            "🟢 Strong Match",
            strong_matches
        )

    with col3:

        st.metric(
            "🟡 Potential/Good",
            good_matches + potential_matches
        )

    with col4:

        st.metric(
            "🔴 Low Match",
            low_matches
        )


    st.divider()


    # ========================================================
    # RANKING TABLE
    # ========================================================

    st.subheader("📊 Candidate Ranking")

    ranking_data = []

    for result in results:

        ranking_data.append(
            {
                "Rank": result.get(
                    "rank",
                    "-"
                ),

                "Candidate": result.get(
                    "candidate_name",
                    "Unknown"
                ),

                "Skill Match": f"{result.get('skill_score', 0):.2f}%",

                "Semantic Similarity":
                    f"{result.get('semantic_score', 0):.2f}%",

                "Experience":
                    f"{result.get('experience_score', 0):.2f}%",

                "Education":
                    f"{result.get('education_score', 0):.2f}%",

                "Final Score":
                    f"{result.get('final_score', 0):.2f}%",

                "Recommendation":
                    result.get(
                        "recommendation",
                        "Unknown"
                    )
            }
        )


    st.dataframe(
        ranking_data,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # DOWNLOAD RESULTS
    # ========================================================

    st.divider()

    st.subheader("📥 Download Screening Results")

    # Create clean export data
    export_data = []

    for result in results:

        export_data.append(
            {
                "Rank": result.get(
                    "rank",
                    "-"
                ),

                "Candidate": result.get(
                    "candidate_name",
                    "Unknown"
                ),

                "Skill Match (%)": round(
                    float(
                        result.get(
                            "skill_score",
                            0
                        )
                    ),
                    2
                ),

                "Semantic Similarity (%)": round(
                    float(
                        result.get(
                            "semantic_score",
                            0
                        )
                    ),
                    2
                ),

                "Experience Match (%)": round(
                    float(
                        result.get(
                            "experience_score",
                            0
                        )
                    ),
                    2
                ),

                "Education Match (%)": round(
                    float(
                        result.get(
                            "education_score",
                            0
                        )
                    ),
                    2
                ),

                "Final Score (%)": round(
                    float(
                        result.get(
                            "final_score",
                            0
                        )
                    ),
                    2
                ),

                "Recommendation":
                    result.get(
                        "recommendation",
                        "Unknown"
                    ),

                "Matched Skills":
                    ", ".join(
                        result.get(
                            "matched_skills",
                            []
                        )
                    ),

                "Missing Skills":
                    ", ".join(
                        result.get(
                            "missing_skills",
                            []
                        )
                    )
            }
        )


    export_df = pd.DataFrame(
        export_data
    )


    csv_data = export_df.to_csv(
        index=False
    )


    json_data = json.dumps(
        export_data,
        indent=4,
        default=str
    )


    download_col1, download_col2 = st.columns(2)


    with download_col1:

        st.download_button(
            label="📊 Download CSV",
            data=csv_data,
            file_name="screening_results.csv",
            mime="text/csv",
            use_container_width=True
        )


    with download_col2:

        st.download_button(
            label="📄 Download JSON",
            data=json_data,
            file_name="screening_results.json",
            mime="application/json",
            use_container_width=True
        )


    # ========================================================
    # INDIVIDUAL CANDIDATE DETAILS
    # ========================================================

    st.divider()

    st.subheader("👤 Candidate Details")


    for index, result in enumerate(results):

        candidate_name = result.get(
            "candidate_name",
            f"Candidate {index + 1}"
        )

        final_score = float(
            result.get(
                "final_score",
                0
            )
        )

        recommendation = result.get(
            "recommendation",
            "Unknown"
        )


        with st.expander(
            f"#{result.get('rank', index + 1)} "
            f"— {candidate_name} "
            f"— {final_score:.2f}% "
            f"— {recommendation}"
        ):


            # ------------------------------------------------
            # Score Cards
            # ------------------------------------------------

            col1, col2, col3, col4, col5 = st.columns(5)


            with col1:

                st.metric(
                    "Final Score",
                    f"{final_score:.2f}%"
                )


            with col2:

                st.metric(
                    "Skill Match",
                    f"{result.get('skill_score', 0):.2f}%"
                )


            with col3:

                st.metric(
                    "Semantic",
                    f"{result.get('semantic_score', 0):.2f}%"
                )


            with col4:

                st.metric(
                    "Experience",
                    f"{result.get('experience_score', 0):.2f}%"
                )


            with col5:

                st.metric(
                    "Education",
                    f"{result.get('education_score', 0):.2f}%"
                )


            # ------------------------------------------------
            # Recommendation
            # ------------------------------------------------

            st.markdown(
                "### 🎯 Recommendation"
            )


            if "strong" in recommendation.lower():

                st.success(
                    f"🟢 {recommendation}"
                )

            elif (
                "good" in recommendation.lower()
                or "potential" in recommendation.lower()
            ):

                st.warning(
                    f"🟡 {recommendation}"
                )

            else:

                st.error(
                    f"🔴 {recommendation}"
                )


            # ------------------------------------------------
            # Screening Reasoning
            # ------------------------------------------------

            st.markdown(
                "### 🧠 Screening Reasoning"
            )


            reasoning = generate_reasoning(
                result
            )


            for reason in reasoning:

                st.write(
                    f"✓ {reason}"
                )


            # ------------------------------------------------
            # Skills
            # ------------------------------------------------

            st.markdown(
                "### 🛠️ Skill Analysis"
            )


            matched_skills = result.get(
                "matched_skills",
                []
            )

            missing_skills = result.get(
                "missing_skills",
                []
            )


            skill_col1, skill_col2 = st.columns(2)


            with skill_col1:

                st.markdown(
                    "#### ✅ Matched Skills"
                )

                if matched_skills:

                    for skill in matched_skills:

                        st.write(
                            f"✓ {skill}"
                        )

                else:

                    st.write(
                        "No matched skills."
                    )


            with skill_col2:

                st.markdown(
                    "#### ❌ Missing Skills"
                )

                if missing_skills:

                    for skill in missing_skills:

                        st.write(
                            f"✗ {skill}"
                        )

                else:

                    st.write(
                        "No missing required skills 🎉"
                    )


            # ------------------------------------------------
            # Experience
            # ------------------------------------------------

            st.markdown(
                "### 💼 Experience"
            )


            required_experience = result.get(
                "required_experience",
                0
            )

            candidate_experience = result.get(
                "candidate_experience",
                0
            )


            exp_col1, exp_col2 = st.columns(2)


            with exp_col1:

                st.write(
                    f"**Required:** "
                    f"{required_experience} years"
                )


            with exp_col2:

                st.write(
                    f"**Candidate:** "
                    f"{candidate_experience} years"
                )


            # ------------------------------------------------
            # Education
            # ------------------------------------------------

            st.markdown(
                "### 🎓 Education"
            )


            required_education = result.get(
                "required_education",
                "-"
            )

            candidate_education = result.get(
                "candidate_education",
                "-"
            )


            edu_col1, edu_col2 = st.columns(2)


            with edu_col1:

                st.write(
                    f"**Required:** "
                    f"{required_education}"
                )


            with edu_col2:

                st.write(
                    f"**Candidate:** "
                    f"{candidate_education}"
                )


    # ========================================================
    # BATCH SCREENING STATUS
    # ========================================================

    if len(results) >= 10:

        st.success(
            "✅ Batch screening successfully processed 10 or more candidates."
        )

    else:

        st.info(
            f"ℹ️ Currently processed {len(results)} candidate(s). "
            "For the assignment demonstration, test with 10+ resumes."
        )


# ============================================================
# INFORMATION SECTION
# ============================================================

st.divider()

with st.expander(
    "ℹ️ How does the AI Resume Screening Agent work?"
):

    st.markdown(
        """
        ### Screening Pipeline

        **1. Job Description**

        HR enters the job description and requirements.

        **2. Resume Upload**

        HR uploads one or more candidate resumes.

        **3. Resume Parsing**

        The system extracts text from PDF/DOCX files.

        **4. Skill Extraction**

        Relevant candidate skills are identified.

        **5. Skill Matching**

        Candidate skills are compared with required job skills.

        **6. Semantic Similarity**

        The system compares the meaning of the resume
        with the job description using sentence embeddings.

        **7. Profile Matching**

        Experience and education requirements are evaluated.

        **8. Final Score**

        The current scoring system uses:

        - Skill Match — 40%
        - Semantic Similarity — 40%
        - Experience — 10%
        - Education — 10%

        **9. Candidate Ranking**

        Candidates are sorted from highest to lowest score.

        **10. Recommendation**

        Candidates are classified as Strong Match,
        Good Match, Potential Match, or Low Match.

        **11. Screening Reasoning**

        The system explains the major reasons behind
        the candidate's recommendation using the calculated
        screening scores and matched/missing skills.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div style="text-align:center; padding:20px; color:#6b7280;">
        🤖 AI Resume Screening Agent
        <br>
        Automated Resume Analysis • Skill Matching • Candidate Ranking
    </div>
    """,
    unsafe_allow_html=True
)