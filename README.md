# 🚀 CareerBooster - AI-Powered Resume Analysis & Career Recommendation System

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [File-by-File Explanation](#file-by-file-explanation)
- [System Architecture](#system-architecture)
- [How It Works](#how-it-works)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)

---

## 🎯 Project Overview

**CareerBooster** is an AI-powered resume analysis and career recommendation system built with Python, BERT embeddings, and NLP. It analyzes your resume against various job roles, provides detailed scoring, identifies skill gaps, and recommends personalized learning resources to help you land your dream job.

### Purpose
CareerBooster helps job seekers by:
- ✅ Analyzing resumes against 24+ different professional roles
- ✅ Providing detailed skill gap analysis
- ✅ Generating personalized learning recommendations
- ✅ Scoring resume effectiveness for target roles
- ✅ Offering semantic similarity matching using BERT embeddings

---

## ⭐ Key Features

1. **Multi-Format Resume Processing**
   - PDF document extraction
   - Text cleaning and normalization
   - Support for various resume formats

2. **AI-Powered Resume Scoring**
   - Semantic similarity analysis using BERT
   - Sectional analysis (summary, experience, skills)
   - Overall resume effectiveness score (0-100)

3. **Comprehensive Skill Analysis**
   - Extracts 100+ technical skills
   - Identifies 30+ soft skills
   - Maps skills to specific job roles
   - Highlights strengths and weaknesses

4. **Role-Based Profiling**
   - 24 professional categories (IT, Finance, Healthcare, etc.)
   - Sample resume analysis from each category
   - Role-specific skill requirements

5. **Personalized Learning Recommendations**
   - Identifies skill gaps
   - Recommends courses from Coursera, Udemy
   - Suggests YouTube tutorials
   - Creates personalized learning paths

6. **Interactive Web Interface**
   - Built with Streamlit
   - Real-time resume upload and analysis
   - Visual presentation of results

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Interactive web interface |
| **NLP & Embeddings** | BERT (sentence-transformers) | Semantic text understanding |
| **Document Processing** | pdfplumber, PyPDF2 | PDF text extraction |
| **Data Processing** | Pandas, NumPy | Data manipulation |
| **ML Framework** | Scikit-learn, PyTorch | Machine learning operations |
| **Web Framework** | Flask/FastAPI (optional) | Backend API support |
| **Database** | CSV files | Sample resumes storage |
| **Version Control** | Git | Code management |

---

## 📁 Project Structure

```
CareerBooster/
├── README.md                              # Main project documentation (this file)
├── app.py                                 # Main Streamlit application
├── requirements.txt                       # Python dependencies
├── runtime.txt                            # Python version specification
├── Resume.csv                             # Sample resume dataset
│
├── 🔧 Core Processing Modules:
├── document_processor.py                  # PDF extraction and text cleaning
├── bert_embedder.py                       # BERT embeddings & similarity
├── skill_extractor.py                     # Skill identification & analysis
├── role_profile_builder.py                # Role profile creation
├── resume_analyzer.py                     # Main analysis orchestrator
│
├── 🎓 Learning & Recommendations:
├── learning_resources_recommender.py      # Learning path generation
├── learning_resources_examples.py         # Resource example demonstrations
│
├── ⚙️ Utilities & Configuration:
├── config.py                              # Global configuration settings
├── utils.py                               # Helper functions
├── examples.py                            # Usage examples
│
├── 📊 Data Directory:
├── data/
│   ├── ACCOUNTANT/                        # Sample resumes by role
│   ├── ADVOCATE/
│   ├── AGRICULTURE/
│   ├── APPAREL/
│   ├── ARTS/
│   ├── AUTOMOBILE/
│   ├── AVIATION/
│   ├── BANKING/
│   ├── BPO/
│   ├── BUSINESS-DEVELOPMENT/
│   ├── CHEF/
│   ├── CONSTRUCTION/
│   ├── CONSULTANT/
│   ├── DESIGNER/
│   ├── DIGITAL-MEDIA/
│   ├── ENGINEERING/
│   ├── FINANCE/
│   ├── FITNESS/
│   ├── HEALTHCARE/
│   ├── HR/
│   ├── INFORMATION-TECHNOLOGY/
│   ├── PUBLIC-RELATIONS/
│   ├── SALES/
│   └── TEACHER/
│
└── 📚 Documentation:
    └── readme_files/
        ├── ARCHITECTURE.md                # Detailed system architecture
        ├── ENHANCEMENT_SUMMARY.md         # Feature enhancements
        ├── MODELS_AND_EMBEDDINGS.md       # ML model documentation
        └── FILE_STRUCTURE_GUIDE.md        # File structure details
```

---

## 📄 File-by-File Explanation

### 🚀 Main Application Files

#### **app.py**
**Purpose:** Main Streamlit web application interface
**What it does:**
- Creates interactive web UI for resume upload
- Displays analysis results with visualizations
- Handles user interactions (file upload, role selection)
- Shows scoring breakdown and recommendations

**Key Features:**
- Sidebar for configuration
- Real-time resume analysis
- Visual score displays
- Strength/weakness highlighting
- Learning resource recommendations display

---

#### **config.py**
**Purpose:** Centralized configuration and constants
**What it does:**
- Defines application settings
- Sets BERT model parameters
- Configures scoring weights
- Specifies paths and data directories

**Key Settings:**
- `APP_NAME`: "ResumeBooster"
- `BERT_MODEL`: 'sentence-transformers/all-MiniLM-L6-v2'
- `EMBEDDING_DIMENSION`: 384
- `SCORING_WEIGHTS`: Weight distribution for different scoring metrics

---

### 📄 Document Processing Modules

#### **document_processor.py**
**Purpose:** Extract and clean resume text from various document formats
**What it does:**
- Reads PDF files using pdfplumber
- Handles multi-page documents
- Cleans extracted text (removes extra whitespace, normalizes formatting)
- Error handling for corrupted or invalid files

**Key Methods:**
- `extract_text_from_pdf(path)`: Extract text from PDF file
- `extract_text_from_bytes(bytes)`: Extract from file bytes
- `clean_text(text)`: Normalize and clean extracted text

**Supported Formats:**
- PDF files (.pdf)
- Byte streams from file uploads

---

### 🧠 Machine Learning Modules

#### **bert_embedder.py**
**Purpose:** Generate semantic embeddings and calculate document similarity
**What it does:**
- Loads pretrained BERT model from sentence-transformers
- Converts text into 384-dimensional embeddings
- Calculates cosine similarity between documents
- Performs section-by-section comparison

**Key Methods:**
- `get_embedding(text)`: Generate embedding for single text
- `get_embeddings_batch(texts)`: Batch generate embeddings
- `cosine_similarity(vec1, vec2)`: Calculate similarity score
- `compare_documents(text1, text2)`: Compare two documents
- `get_sectional_similarity(resume, profile)`: Compare by sections

**Model Used:**
- **Model:** sentence-transformers/all-MiniLM-L6-v2
- **Dimensions:** 384
- **Speed:** Optimized for real-time analysis
- **Advantage:** Balanced accuracy and performance

---

#### **skill_extractor.py**
**Purpose:** Extract and analyze skills from resume text
**What it does:**
- Identifies technical skills (programming, tools, frameworks)
- Detects soft skills (communication, leadership, etc.)
- Matches extracted skills against role requirements
- Calculates skill overlap percentages

**Skill Database:**
- **100+ Technical Skills:** Python, Java, AWS, Docker, React, Machine Learning, etc.
- **30+ Soft Skills:** Leadership, Communication, Problem-solving, Teamwork, etc.
- **Role Profiles:** Maps skills to 24 different job categories

**Key Methods:**
- `extract_skills(text)`: Extract all skills from text
- `get_role_profile(role)`: Get required skills for a role
- `analyze_skills(resume_skills, role)`: Compare resume vs role skills

---

#### **role_profile_builder.py**
**Purpose:** Build comprehensive profiles for each job role
**What it does:**
- Scans data directory for sample resumes in each role category
- Extracts skills from sample resumes
- Creates aggregate role profiles
- Identifies most common skills for each role
- Stores role metadata and requirements

**Key Methods:**
- `_get_available_roles()`: Discover all roles from data directory
- `get_role_profile(role)`: Retrieve complete role profile
- `analyze_role_samples(role)`: Analyze all sample resumes for a role

**Supported Roles:**
24 professional categories: Accountant, Advocate, Agriculture, Apparel, Arts, Automobile, Aviation, Banking, BPO, Business Development, Chef, Construction, Consultant, Designer, Digital Media, Engineering, Finance, Fitness, Healthcare, HR, IT, Public Relations, Sales, Teacher

---

#### **resume_analyzer.py**
**Purpose:** Main orchestrator that performs complete resume analysis
**What it does:**
- Combines all analysis modules (document processor, embedder, skill extractor, role builder)
- Executes complete resume evaluation pipeline
- Generates comprehensive scoring and analysis results
- Creates detailed recommendations

**Analysis Pipeline:**
1. Extract text from resume
2. Extract skills from resume
3. Get target role profile
4. Analyze semantic similarity
5. Calculate skill overlap
6. Generate overall score
7. Identify skill gaps

**Key Methods:**
- `analyze_resume(resume_text, role)`: Perform complete analysis
- `generate_score(analysis_data)`: Calculate final score
- `get_recommendations(gaps)`: Generate improvement recommendations

**Output:**
```python
{
    'overall_score': 75.5,
    'semantic_similarity': 0.82,
    'skill_overlap': 0.70,
    'matching_skills': ['Python', 'AWS', 'Docker'],
    'missing_skills': ['Kubernetes', 'GraphQL'],
    'strengths': ['Strong technical foundation'],
    'weaknesses': ['Limited DevOps experience'],
    'recommendations': []
}
```

---

### 🎓 Learning Recommendation Modules

#### **learning_resources_recommender.py**
**Purpose:** Generate personalized learning recommendations for skill gaps
**What it does:**
- Maintains database of 100+ skills with learning resources
- Recommends courses from Coursera, Udemy
- Suggests free YouTube tutorials
- Creates personalized learning paths
- Assesses skill difficulty levels

**Resource Database Includes:**
- **Programming Languages:** Python, Java, JavaScript, C++, C#, SQL, R, etc.
- **Web Development:** React, Angular, Vue, Node.js, Django, Flask, etc.
- **Cloud & DevOps:** AWS, Azure, GCP, Docker, Kubernetes, CI/CD, etc.
- **Data & AI:** Machine Learning, TensorFlow, PyTorch, Data Analysis, etc.
- **Databases:** MySQL, PostgreSQL, MongoDB, Redis, Elasticsearch, etc.
- **Soft Skills:** Communication, Leadership, Project Management, etc.

**Resource Types per Skill:**
- Coursera courses (university-backed, structured)
- Udemy courses (flexible, on-demand)
- YouTube tutorials (free video learning)

**Key Methods:**
- `get_recommendations(missing_skills, num_resources=3)`: Get top resources
- `create_personalized_learning_path(missing_skills, role)`: Build learning plan
- `get_skill_difficulty_level(skill)`: Assess difficulty (Beginner/Intermediate/Advanced)

---

#### **learning_resources_examples.py**
**Purpose:** Demonstrates learning resources feature
**What it does:**
- Provides example usage of the recommender
- Shows how to generate recommendations
- Demonstrates learning path creation
- Useful for testing and understanding the feature

---

### 🔧 Utility Modules

#### **utils.py**
**Purpose:** Helper functions and utilities
**What it does:**
- Provides common utility functions
- Text processing helpers
- File I/O operations
- Data validation functions

---

#### **examples.py**
**Purpose:** Usage examples and demonstrations
**What it does:**
- Shows how to use all major components
- Demonstrates analysis pipeline
- Provides code snippets for integration

---

### 📊 Data Files

#### **Resume.csv**
**Purpose:** Dataset of sample resumes
**Contains:**
- Cleaned resume text examples
- Role labels/categories
- Additional metadata

---

#### **requirements.txt**
**Purpose:** Python package dependencies
**Key Packages:**
- `streamlit`: Web UI framework
- `sentence-transformers`: BERT embeddings
- `torch`: Deep learning framework
- `pdfplumber`: PDF text extraction
- `pandas`: Data processing
- `numpy`: Numerical operations
- `scikit-learn`: ML utilities

---

#### **runtime.txt**
**Purpose:** Specifies Python version for deployment
**Default:** Python 3.9 or later

---

### 📚 Documentation Files

#### **readme_files/ARCHITECTURE.md**
System architecture and module relationships

#### **readme_files/MODELS_AND_EMBEDDINGS.md**
Technical details about BERT models and embeddings

#### **readme_files/ENHANCEMENT_SUMMARY.md**
Summary of learning resources feature enhancements

#### **readme_files/FILE_STRUCTURE_GUIDE.md**
Detailed file structure documentation

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Streamlit Frontend                 │
│         (Web UI, File Upload, Results Display)      │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│              Resume Analysis Engine                 │
│           (resume_analyzer.py)                      │
│    Orchestrator for all analysis components        │
└──────────┬──────────┬──────────┬───────────┬────────┘
           │          │          │           │
    ┌──────▼──┐  ┌───▼─────┐ ┌──▼──────┐ ┌─▼──────┐
    │Document │  │   BERT  │ │  Skill  │ │  Role  │
    │Processor│  │Embedder │ │Extractor│ │Profile│
    └─────────┘  └─────────┘ └─────────┘ └───────┘
         │           │            │          │
    ┌────▼────────────┴────────────┴──────────┴──────────┐
    │           Learning Resources Recommender          │
    │      (learning_resources_recommender.py)          │
    └──────────────────────────────────────────────────┘
         │           │            │          │
    ┌────▼────────────┴────────────┴──────────┴──────────┐
    │          Data & Knowledge Layer                    │
    │  (PDF files, Skill DB, Role Data, Resources)      │
    └──────────────────────────────────────────────────┘
```

---

## 🔄 How It Works

### Step 1: Resume Input
User uploads a resume (PDF) through the Streamlit interface

### Step 2: Document Processing
```python
# document_processor.py
→ Extract text from PDF
→ Clean and normalize text
→ Remove special characters and extra whitespace
```

### Step 3: Skill Extraction
```python
# skill_extractor.py
→ Extract technical skills (Python, AWS, Docker, etc.)
→ Extract soft skills (Leadership, Communication, etc.)
→ Create skill profile from resume
```

### Step 4: Role Selection
User selects target job role (IT, Finance, Healthcare, etc.)

### Step 5: Role Profile Building
```python
# role_profile_builder.py
→ Load sample resumes for selected role
→ Extract skills from sample resumes
→ Build aggregated role skill profile
→ Identify key requirements
```

### Step 6: Semantic Analysis
```python
# bert_embedder.py
→ Generate BERT embeddings for resume
→ Generate BERT embeddings for role profile
→ Calculate cosine similarity (0-1 scale)
→ Perform section-by-section comparison
```

### Step 7: Skill Analysis
```python
# skill_extractor.py
→ Compare resume skills vs role requirements
→ Calculate skill overlap percentage
→ Identify matching skills
→ Identify missing skills (gaps)
```

### Step 8: Scoring & Analysis
```python
# resume_analyzer.py
→ Combine semantic similarity (35%)
→ Combine sectional similarity (25%)
→ Combine skill overlap (30%)
→ Combine additional factors (10%)
→ Generate final score (0-100)
```

### Step 9: Learning Recommendations
```python
# learning_resources_recommender.py
→ Identify missing skills (gaps)
→ Look up learning resources for each gap
→ Select top 3-5 resources per skill
→ Rank by difficulty and time commitment
→ Create personalized learning path
```

### Step 10: Results Display
Display comprehensive analysis:
- Overall score
- Scoring breakdown
- Matching skills (strengths)
- Missing skills (areas for improvement)
- Personalized learning recommendations

---

## 💻 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Git (optional)

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/CareerBooster.git
cd CareerBooster
```

### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Download BERT Model (optional, auto-downloads on first run)
```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"
```

---

## 🚀 Usage Guide

### Running the Application

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

### Web Interface Usage

1. **Upload Resume**: Click "Upload your resume" button
2. **Select Role**: Choose target job role from dropdown
3. **Analyze**: Click "Analyze Resume" button
4. **View Results**:
   - Overall score with color indicator
   - Semantic similarity details
   - Skill analysis breakdown
   - Personalized learning recommendations

### Programmatic Usage

```python
from document_processor import DocumentProcessor
from resume_analyzer import ResumeAnalyzer

# Initialize analyzer
analyzer = ResumeAnalyzer(data_dir='./data')

# Extract resume text
processor = DocumentProcessor()
resume_text = processor.extract_text_from_pdf('resume.pdf')

# Analyze for specific role
analysis = analyzer.analyze_resume(resume_text, role='INFORMATION-TECHNOLOGY')

# Print results
print(f"Score: {analysis['overall_score']}")
print(f"Matching Skills: {analysis['matching_skills']}")
print(f"Missing Skills: {analysis['missing_skills']}")
print(f"Recommendations: {analysis['recommendations']}")
```

### Using Learning Recommendations

```python
from learning_resources_recommender import LearningResourcesRecommender

recommender = LearningResourcesRecommender()

# Get recommendations for skill gaps
missing_skills = ['Docker', 'Kubernetes', 'GraphQL']
resources = recommender.get_recommendations(missing_skills, num_resources=3)

# Create personalized learning path
path = recommender.create_personalized_learning_path(missing_skills, role='IT')
```

---

## 📊 Scoring Methodology

The final score (0-100) is calculated as:

```
Final Score = (
    Semantic Similarity × 0.35 +
    Sectional Similarity × 0.25 +
    Skill Overlap × 0.30 +
    Other Factors × 0.10
) × 100
```

### Score Interpretation
- **85-100**: Excellent match - Ready to apply
- **70-84**: Good match - Some improvements needed
- **55-69**: Fair match - Significant skill gaps
- **40-54**: Poor match - Requires major upskilling
- **Below 40**: Not suitable - Consider different roles

---

## 🔒 Data Privacy

- Resumes are processed locally (not stored on external servers)
- No personal data is logged
- Analysis results are displayed but not permanently stored
- User uploads are temporary (cleared after session)

---

## 🚧 Future Enhancements

- [ ] LinkedIn profile integration
- [ ] Cover letter generator
- [ ] Interview preparation guide
- [ ] Salary insights by role and location
- [ ] Job market trend analysis
- [ ] Resume optimization suggestions
- [ ] Multi-language support
- [ ] Advanced analytics dashboard

---

## 📞 Support & Contributions

For issues, suggestions, or contributions:
1. Open an issue on GitHub
2. Submit pull requests with improvements
3. Share feedback and feature requests

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details

---

## 👨‍💻 Author & Credits

Built with ❤️ using Python, BERT, and modern NLP techniques

**Key Technologies:**
- BERT (Bidirectional Encoder Representations from Transformers)
- Streamlit for web interface
- PyTorch for deep learning
- Sentence Transformers for embeddings

---

## 📈 Project Statistics

- **24 Professional Roles** analyzed
- **100+ Technical Skills** identified
- **30+ Soft Skills** evaluated
- **BERT Model Size**: 384 dimensions
- **Processing Speed**: ~2-3 seconds per resume
- **Accuracy**: Continuously improved through feedback

---

## 🎓 Learning Resources

- BERT Paper: [Attention Is All You Need](https://arxiv.org/abs/1810.04805)
- Sentence Transformers: [Documentation](https://www.sbert.net/)
- Streamlit: [Official Docs](https://docs.streamlit.io/)
- PyTorch: [Official Docs](https://pytorch.org/docs/)

---

**Last Updated:** April 2026  
**Version:** 1.0.0  
**Status:** Active Development
