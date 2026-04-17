# 📁 ResumeBooster - File Structure Guide

## Quick Overview

This document explains the role of each file in the ResumeBooster project and whether it belongs to **Frontend** or **Backend**.

---

## 🎨 Frontend Files

| File | Role | Purpose |
|------|------|---------|
| **app.py**  | Main UI Interface | Streamlit web application for user interaction, resume upload, and results display |
|      |      |         |
---

## ⚙️ Backend Files

| File | Role | Purpose |
|------|------|---------|
| **resume_analyzer.py** | Main Orchestrator | Coordinates all analysis components and generates comprehensive scores |
| **bert_embedder.py** | Embedding Engine | BERT model for generating embeddings and calculating semantic similarity |
| **skill_extractor.py** | Skill Detection | Extracts technical and soft skills from resume text using pattern matching |
| **role_profile_builder.py** | Role Benchmarking | Builds role profiles by analyzing sample resumes from data directory |
| **document_processor.py** | PDF Processing | Extracts and cleans text from PDF files |
| **learning_resources_recommender.py** | Learning Path Generator | Recommends courses and tutorials based on skill gaps |
| **utils.py** | Utility Functions | Helper functions for reporting, batch analysis, and data processing |
| **config.py** | Configuration | Central configuration management for all settings and parameters |

---

## 📚 Example & Testing Files

| File | Purpose |
|------|---------|
| **examples.py** | Demonstrates how to use the resume analyzer |
| **learning_resources_examples.py** | Shows learning resources recommendation feature in action |

---

## 📊 Data Files

| File/Folder | Purpose |
|-------------|---------|
| **Resume.csv** | Sample resume dataset for testing and analysis |
| **data/** | Contains role subdirectories with sample resumes for profile building |
| &nbsp;&nbsp;├── ACCOUNTANT/ | Sample accountant resumes |
| &nbsp;&nbsp;├── ENGINEER/ | Sample engineer resumes |
| &nbsp;&nbsp;├── DATA ANALYST/ | Sample data analyst resumes |
| &nbsp;&nbsp;└── ... (24+ roles) | Other role categories |

---

## ⚙️ Configuration & Deployment

| File | Purpose |
|------|---------|
| **requirements.txt** | Python dependencies (BERT, Streamlit, PyTorch, etc.) |
| **runtime.txt** | Python version specification for deployment |

---

## 🏗️ Data Flow: How Files Work Together

```
User Upload Resume (app.py)
          ↓
 ┌────────────────────────┐
 │ document_processor.py  │ → Extract text from PDF
 └─────────────┬──────────┘
               ↓
 ┌────────────────────────┐
 │ resume_analyzer.py     │ → Main orchestrator
 └──────────┬─────────────┘
            │
    ┌───────┼────────┬──────────────┐
    ↓       ↓        ↓              ↓
 skill_   bert_   role_profile_  learning_
extract  embedder  builder        recommender
    ↓       ↓        ↓              ↓
    └───────┴────────┴──────────────┘
               ↓
        Generate Results
               ↓
       Display in app.py (Frontend)
```

---

## 🚀 Quick Start - File Usage

### To Run the Application:
```bash
streamlit run app.py
```

### To Test Analysis:
```bash
python examples.py
```

### To Test Learning Resources:
```bash
python learning_resources_examples.py
```

---

## 📋 Summary Table

| Category | Files | Function |
|----------|-------|----------|
| **Frontend** | app.py | User Interface |
| **Backend Core** | resume_analyzer.py | Orchestration |
| **Backend AI/ML** | bert_embedder.py, skill_extractor.py, role_profile_builder.py | Analysis Engines |
| **Backend Support** | document_processor.py, learning_resources_recommender.py, utils.py, config.py | Support Services |
| **Examples** | examples.py, learning_resources_examples.py | Documentation & Testing |
| **Data** | Resume.csv, data/ | Training & Test Data |
| **Config** | requirements.txt, runtime.txt | Environment Setup |

---

## 🔗 File Dependencies

```
app.py (Frontend)
├── resume_analyzer.py (Backend Core)
│   ├── bert_embedder.py
│   ├── skill_extractor.py
│   ├── role_profile_builder.py
│   ├── learning_resources_recommender.py
│   └── document_processor.py
├── document_processor.py
└── config.py

Backend Files
├── config.py (shared configuration)
└── utils.py (shared utilities)
```

---

## 📝 File Responsibilities

**Frontend (User Facing):**
- Handles user input and file uploads
- Displays results and visualizations
- Manages user interface interactions

**Backend (Processing):**
- Processes resume data
- Runs AI/ML models
- Calculates scores and metrics
- Generates recommendations
- Manages data and configurations

---

**Version**: 1.0  
**Last Updated**: April 2026
