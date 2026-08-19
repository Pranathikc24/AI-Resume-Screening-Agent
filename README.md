# 🤖 AI Resume Screening Agent

An AI-powered resume screening agent that analyzes multiple candidate
resumes against a given job description, evaluates their relevance,
calculates scores, and ranks candidates automatically.

---

## 📌 Project Overview

Recruiters often need to manually review a large number of resumes
for a single job opening.

This project automates the initial resume screening process.

The agent accepts a job description and multiple candidate resumes,
extracts relevant information, compares candidates against the job
requirements, calculates a final score, and produces a ranked list
of candidates.

---

## 🎯 Objective

The main objective is to reduce manual resume screening effort by
automatically identifying candidates who are most relevant to a
given job description.

The system considers:

- Skills
- Semantic relevance
- Experience
- Education

---

## ✨ Features

- Upload multiple PDF/DOCX resumes
- Extract resume text automatically
- Extract candidate skills
- Match candidate skills with job requirements
- Calculate semantic similarity
- Compare candidate experience
- Compare education requirements
- Calculate weighted final score
- Rank candidates
- Generate match recommendations
- Provide screening reasoning
- Export results as CSV
- Export results as JSON
- Process multiple candidates in a single run
- Streamlit web interface

---

## 🏗️ System Architecture

```text
                  JOB DESCRIPTION
                         │
                         ▼
                ┌─────────────────┐
                │ Job Requirements │
                └────────┬────────┘
                         │
                         │
                  CANDIDATE RESUMES
                         │
                         ▼
                ┌─────────────────┐
                │  Resume Parser   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Skill Extraction│
                └────────┬────────┘
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
        Skill Match  Semantic     Profile
                     Similarity    Matching
                         │           │
                         └─────┬─────┘
                               ▼
                       Final Score
                               │
                               ▼
                     Candidate Ranking
                               │
                               ▼
                    Screening Recommendation
                               │
                               ▼
                       CSV / JSON Output