import re


# ============================================================
# GENERAL SKILL DATABASE
# ============================================================

SKILL_DATABASE = {

    # --------------------------------------------------------
    # Programming Languages
    # --------------------------------------------------------

    "python",
    "java",
    "javascript",
    "typescript",
    "c",
    "c++",
    "c#",
    "r",
    "php",
    "ruby",
    "kotlin",
    "swift",
    "go",

    # --------------------------------------------------------
    # Web Development
    # --------------------------------------------------------

    "html",
    "css",
    "bootstrap",
    "tailwind",
    "react",
    "react.js",
    "angular",
    "vue",
    "node.js",
    "node",
    "express",
    "express.js",
    "django",
    "flask",
    "fastapi",
    "spring",
    "spring boot",
    "asp.net",

    # --------------------------------------------------------
    # APIs / Backend
    # --------------------------------------------------------

    "rest api",
    "rest apis",
    "restful api",
    "graphql",
    "microservices",
    "api development",

    # --------------------------------------------------------
    # Data Science / AI / ML
    # --------------------------------------------------------

    "machine learning",
    "deep learning",
    "artificial intelligence",
    "ai",
    "data science",
    "data analysis",
    "natural language processing",
    "nlp",
    "computer vision",
    "generative ai",
    "gen ai",
    "large language models",
    "llm",

    # --------------------------------------------------------
    # Python / ML Libraries
    # --------------------------------------------------------

    "pandas",
    "numpy",
    "scikit-learn",
    "sklearn",
    "tensorflow",
    "pytorch",
    "keras",
    "opencv",
    "matplotlib",
    "seaborn",
    "transformers",

    # --------------------------------------------------------
    # Databases
    # --------------------------------------------------------

    "sql",
    "mysql",
    "postgresql",
    "postgres",
    "mongodb",
    "oracle",
    "sqlite",
    "redis",
    "firebase",

    # --------------------------------------------------------
    # Data / BI / Analytics
    # --------------------------------------------------------

    "power bi",
    "tableau",
    "excel",
    "advanced excel",
    "data visualization",
    "statistics",
    "data analytics",
    "business intelligence",
    "power query",
    "dax",

    # --------------------------------------------------------
    # Cloud
    # --------------------------------------------------------

    "aws",
    "amazon web services",
    "azure",
    "microsoft azure",
    "gcp",
    "google cloud",
    "google cloud platform",

    # --------------------------------------------------------
    # DevOps / Infrastructure
    # --------------------------------------------------------

    "docker",
    "kubernetes",
    "jenkins",
    "ci/cd",
    "terraform",
    "ansible",
    "linux",

    # --------------------------------------------------------
    # Version Control / Tools
    # --------------------------------------------------------

    "git",
    "github",
    "gitlab",
    "bitbucket",
    "jira",
    "postman",

    # --------------------------------------------------------
    # HR / Recruitment
    # --------------------------------------------------------

    "recruitment",
    "talent acquisition",
    "human resources",
    "hr",
    "hrms",
    "employee relations",
    "onboarding",
    "interviewing",
    "candidate screening",
    "performance management",
    "payroll",

    # --------------------------------------------------------
    # Sales / Marketing
    # --------------------------------------------------------

    "sales",
    "business development",
    "lead generation",
    "customer relationship management",
    "crm",
    "digital marketing",
    "social media marketing",
    "content marketing",
    "seo",
    "sem",
    "market research",

    # --------------------------------------------------------
    # Finance / Accounting
    # --------------------------------------------------------

    "accounting",
    "financial analysis",
    "financial reporting",
    "bookkeeping",
    "budgeting",
    "forecasting",
    "taxation",
    "auditing",
    "accounts payable",
    "accounts receivable",

    # --------------------------------------------------------
    # Common Professional Skills
    # --------------------------------------------------------

    "communication",
    "leadership",
    "teamwork",
    "problem solving",
    "problem-solving",
    "critical thinking",
    "time management",
    "negotiation",
    "presentation",
    "project management",
    "analytical skills",
    "decision making",
    "decision-making",
}


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text):
    """
    Convert text into a normalized format.

    Steps:
    1. Convert to lowercase.
    2. Normalize whitespace.
    """

    if not text:
        return ""

    text = text.lower()

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ============================================================
# SKILL EXTRACTION
# ============================================================

def extract_skills(text):
    """
    Extract known skills from any text.

    This function can be used for:
    - Job descriptions
    - Resumes
    - Cover letters
    - Other recruitment documents
    """

    normalized_text = normalize_text(text)

    found_skills = set()

    for skill in SKILL_DATABASE:

        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, normalized_text):

            found_skills.add(skill)

    return sorted(found_skills)


# ============================================================
# SKILL MATCHING
# ============================================================

def calculate_skill_match(required_skills, candidate_skills):
    """
    Calculate how many required JD skills
    are present in the candidate resume.

    Returns:
        Score between 0 and 100.
    """

    if not required_skills:

        return 0.0

    required = {
        skill.lower().strip()
        for skill in required_skills
    }

    candidate = {
        skill.lower().strip()
        for skill in candidate_skills
    }

    matched = required.intersection(candidate)

    score = (
        len(matched) / len(required)
    ) * 100

    return round(score, 2)


# ============================================================
# MATCHED SKILLS
# ============================================================

def get_matched_skills(required_skills, candidate_skills):
    """
    Return skills that appear in both
    the JD and candidate resume.
    """

    required = {
        skill.lower().strip()
        for skill in required_skills
    }

    candidate = {
        skill.lower().strip()
        for skill in candidate_skills
    }

    return sorted(
        required.intersection(candidate)
    )


# ============================================================
# MISSING SKILLS
# ============================================================

def get_missing_skills(required_skills, candidate_skills):
    """
    Return required skills that are not
    found in the candidate resume.
    """

    required = {
        skill.lower().strip()
        for skill in required_skills
    }

    candidate = {
        skill.lower().strip()
        for skill in candidate_skills
    }

    return sorted(
        required - candidate
    )