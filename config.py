"""
Configuration settings for ResumeBooster
"""

import os
from pathlib import Path

# Application Settings
APP_NAME = "ResumeBooster"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "AI-Powered Resume Analysis Engine using BERT and NLP"

# Paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
LOGS_DIR = PROJECT_ROOT / "logs"

# BERT Model Configuration
BERT_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
EMBEDDING_DIMENSION = 384

# Analysis Configuration
SAMPLE_RESUMES_PER_ROLE = 10  # Number of samples to analyze for role profiles
CHUNK_SIZE = 200  # Words per chunk for sectional analysis

# Scoring Configuration
SCORING_WEIGHTS = {
    'semantic_similarity': 0.35,
    'sectional_similarity': 0.25,
    'skill_overlap': 0.30,
    'resume_completeness': 0.10
}

# Skill Database Configuration
MIN_SKILL_FREQUENCY = 1  # Minimum occurrences to consider as a skill
TOP_SKILLS_TO_SHOW = 10

# UI Configuration
STREAMLIT_CONFIG = {
    'page_title': 'ResumeBooster - AI Resume Analyzer',
    'page_icon': '🚀',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded'
}

# PDF Processing Configuration
PDF_MAX_SIZE_MB = 50
PDF_TIMEOUT_SECONDS = 30

# Score Thresholds
SCORE_THRESHOLDS = {
    'excellent': 7.5,
    'good': 6.0,
    'fair': 4.5,
    'weak': 0.0
}

# Resume Validation
MIN_RESUME_LENGTH = 200
MAX_RESUME_LENGTH = 50000

# Logging Configuration
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Available Roles (Auto-discovered, but can be overridden)
AVAILABLE_ROLES = [
    'ACCOUNTANT',
    'ADVOCATE',
    'AGRICULTURE',
    'APPAREL',
    'ARTS',
    'AUTOMOBILE',
    'AVIATION',
    'BANKING',
    'BPO',
    'BUSINESS-DEVELOPMENT',
    'CHEF',
    'CONSTRUCTION',
    'CONSULTANT',
    'DESIGNER',
    'DIGITAL-MEDIA',
    'ENGINEERING',
    'FINANCE',
    'FITNESS',
    'HEALTHCARE',
    'HR',
    'INFORMATION-TECHNOLOGY',
    'PUBLIC-RELATIONS',
    'SALES',
    'TEACHER'
]

# Create necessary directories
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
