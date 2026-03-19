# 🏗️ ResumeBooster - System Architecture & Design

## System Overview

ResumeBooster is a multi-layered AI system that combines NLP, deep learning embeddings, and skill-based analysis to provide comprehensive resume evaluation.

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
    ┌────▼────────────┴────────────┴──────────┴──┐
    │          Data & Knowledge Layer             │
    │  (PDF files, Skill Database, Role Data)    │
    └──────────────────────────────────────────┘
```

## Module Architecture

### 1. **Core Modules**

#### document_processor.py
```
DocumentProcessor
├── extract_text_from_pdf(path) → str
├── extract_text_from_bytes(bytes) → str
└── clean_text(text) → str
```

**Responsibilities:**
- PDF text extraction using pdfplumber
- Text cleaning and normalization
- Error handling for corrupted files

**Key Features:**
- Multi-page PDF handling
- Automatic whitespace normalization
- Robust error recovery

---

#### skill_extractor.py
```
SkillExtractor
├── TECHNICAL_SKILLS (Set[str])
├── SOFT_SKILLS (Set[str])
├── ROLE_SKILL_PROFILES (Dict[role] → skills)
├── extract_skills(text) → Dict[technical, soft]
├── get_role_profile(role) → Dict
├── analyze_skills(resume_skills, role) → Dict
```

**Responsibilities:**
- Identify technical and soft skills
- Maintain comprehensive skill database
- Role-specific skill mapping
- Strength/weakness comparison

**Features:**
- 100+ technical skill patterns
- 30+ soft skill patterns
- Role-specific skill profiles
- Overlap calculation

---

#### bert_embedder.py
```
BertEmbedder
├── model (SentenceTransformer)
├── get_embedding(text) → np.ndarray
├── get_embeddings_batch(texts) → np.ndarray
├── cosine_similarity(vec1, vec2) → float
├── compare_documents(text1, text2) → Dict
├── get_chunk_embeddings(text) → Tuple
└── get_sectional_similarity(resume, profile) → Dict
```

**Responsibilities:**
- BERT embedding generation
- Semantic similarity calculation
- Document comparison
- Section-by-section analysis

**Model Details:**
- Model: sentence-transformers/all-MiniLM-L6-v2
- Dimensions: 384
- Speed: Optimized for real-time use
- Accuracy: 90%+ semantic understanding

---

#### role_profile_builder.py
```
RoleProfileBuilder
├── data_dir (path)
├── role_profiles (Dict)
├── _get_available_roles() → Dict
├── get_available_roles() → List[str]
├── build_role_profile(role, sample_size) → Dict
├── get_role_profile(role) → Dict
└── get_all_profiles() → Dict
```

**Responsibilities:**
- Discover roles from data directory
- Extract skill patterns from samples
- Build role benchmark profiles
- Cache profile results

**Process:**
1. Scan data/ directory for role subdirectories
2. Read 10 sample resumes per role
3. Extract skills from samples
4. Identify most common skills
5. Create role profile with top skills

---

#### resume_analyzer.py
```
ResumeAnalyzer
├── embedder (BertEmbedder)
├── profile_builder (RoleProfileBuilder)
├── analyze_resume(resume_text, role) → Dict
├── _build_role_description(profile) → str
├── _calculate_score(sim, sectional, overlap, skills) → float
├── _generate_suggestions(analysis, role, text, skills) → List
└── get_available_roles() → List[str]
```

**Responsibilities:**
- Orchestrate complete analysis
- Multi-factor scoring
- Suggestion generation
- Result compilation

**Analysis Pipeline:**
1. Extract skills from resume
2. Get role profile
3. Calculate skill overlap
4. Generate BERT embeddings
5. Compute semantic similarity
6. Perform sectional analysis
7. Calculate composite score
8. Generate personalized suggestions

---

### 2. **Utility Modules**

#### utils.py
```
ReportGenerator
├── generate_json_report(result, filename=None) → str
├── generate_csv_report(results, filename) → None
└── generate_html_report(result, filename=None) → str

BatchAnalyzer
├── analyze_multiple_roles(analyzer, resume, roles=None) → Dict
└── find_best_matching_role(analyzer, resume) → str

ResumeProcessor
├── validate_resume(resume_text) → Dict
└── get_resume_stats(resume_text) → Dict
```

---

#### config.py
```
Configuration Settings:
├── APP_NAME, VERSION, DESCRIPTION
├── PATHS (PROJECT_ROOT, DATA_DIR, LOGS_DIR)
├── BERT Configuration
├── Analysis Parameters
├── Scoring Weights
├── Skill Database Settings
├── UI Configuration
└── Resume Validation Rules
```

---

### 3. **Frontend Module**

#### app.py
```
Streamlit Application
├── display_header()
├── display_score(score, max_score)
├── display_strengths(strengths)
├── display_weaknesses(weaknesses)
├── display_suggestions(suggestions)
├── display_metrics(metrics, role_profile)
├── display_skill_breakdown(resume_skills, role_skills)
└── main()
```

**Interface Flow:**
1. Header display
2. Sidebar config panel
3. Role selection
4. Resume upload
5. Analysis button
6. Multi-tab results display
7. Download report option

## Data Flow

### Analysis Workflow

```
User Input
    │
    ├─ PDF Resume Upload
    │
    ▼
PDF Text Extraction
    │
    ├─ DocumentProcessor.extract_text_from_pdf()
    │
    ▼
Text Cleaning
    │
    ├─ DocumentProcessor.clean_text()
    │
    ▼
Skill Extraction
    │
    ├─ SkillExtractor.extract_skills()
    │
    ▼
Role Profile Building
    │
    ├─ RoleProfileBuilder.build_role_profile()
    │
    ▼
BERT Embedding Generation
    │
    ├─ BertEmbedder.get_embedding()
    │
    ▼
Skill Analysis
    │
    ├─ SkillExtractor.analyze_skills()
    │
    ▼
Semantic Similarity Calculation
    │
    ├─ BertEmbedder.compare_documents()
    ├─ BertEmbedder.get_sectional_similarity()
    │
    ▼
Score Calculation
    │
    ├─ ResumeAnalyzer._calculate_score()
    │
    ▼
Suggestion Generation
    │
    ├─ ResumeAnalyzer._generate_suggestions()
    │
    ▼
Results Display
    │
    └─ Streamlit Dashboard
```

## Scoring Algorithm

### Multi-Factor Scoring System

```
Final Score = (W1 × S1) + (W2 × S2) + (W3 × S3) + (W4 × S4) × 10

Where:
  S1 = Semantic Similarity Score (0-1)
  S2 = Sectional Relevance Score (0-1)
  S3 = Skill Overlap Percentage / 100
  S4 = Resume Completeness Score (0-1)
  
  W1 = 0.35 (Semantic Similarity Weight)
  W2 = 0.25 (Sectional Relevance Weight)
  W3 = 0.30 (Skill Overlap Weight)
  W4 = 0.10 (Resume Completeness Weight)
  
  Sum of weights = 1.00
```

### Scoring Factors

#### 1. Semantic Similarity (35% weight)
- **Metric**: Cosine similarity of BERT embeddings
- **Range**: 0.0 - 1.0
- **Meaning**: How well does resume content align with role semantically?
- **Calculation**: Cosine distance between resume embedding and role profile embedding

#### 2. Sectional Similarity (25% weight)
- **Metric**: Average max similarity across resume chunks vs role requirements
- **Range**: 0.0 - 1.0
- **Meaning**: How relevant are different sections of the resume?
- **Calculation**: Resume divided into chunks, each compared to role profile

#### 3. Skill Overlap (30% weight)
- **Metric**: Percentage of required skills present in resume
- **Range**: 0% - 100% (normalized to 0.0 - 1.0)
- **Meaning**: What percentage of required skills does candidate have?
- **Calculation**: (Count of matching skills / Total required skills) × 100

#### 4. Resume Completeness (10% weight)
- **Metric**: Presence and depth of skills
- **Range**: 0.0 - 1.0
- **Meaning**: How comprehensive is the resume?
- **Calculation**: min(1.0, total_skills / 20)

### Score Interpretation

| Score | Rating | Interpretation | Recommendation |
|-------|--------|----------------|----------------|
| 9.0-10.0 | Excellent | Exceptional match | Apply with confidence |
| 8.0-8.9 | Very Good | Strong candidate | Minor improvements recommended |
| 7.0-7.9 | Good | Qualified candidate | Address major gaps |
| 6.0-6.9 | Fair | Moderate fit | Significant skill development |
| 5.0-5.9 | Weak | Limited alignment | Major skill gaps |
| 0.0-4.9 | Poor | Poor fit | Consider different roles |

## Technology Stack

### Backend
- **Python 3.8+**: Core language
- **Transformers (Hugging Face)**: BERT model loading
- **Sentence-Transformers**: Efficient embeddings
- **PyTorch**: Deep learning backend
- **PyPDF/pdfplumber**: PDF processing
- **NumPy**: Numerical operations
- **Scikit-learn**: ML utilities

### Frontend
- **Streamlit**: Web interface framework
- **HTML/CSS**: Custom styling
- **Markdown**: Content formatting

### Infrastructure
- **File System**: Local data storage
- **JSON**: Result serialization
- **CSV**: Report export

## Performance Characteristics

### Time Complexity
- **PDF Extraction**: O(p) where p = number of pages
- **Skill Extraction**: O(t × s) where t = tokens, s = skills
- **BERT Embedding**: O(t) where t = tokens
- **Similarity Calculation**: O(1) cosine distance
- **Overall Analysis**: O(t + s) ≈ O(t)

### Space Complexity
- **BERT Model**: ~50MB on disk, ~100MB in memory
- **Embeddings Per Resume**: 384 × 8 bytes = ~3KB
- **Role Profiles**: ~500KB each × 24 roles = ~12MB

### Typical Performance
- **PDF Extraction**: 1-5 seconds (depends on page count)
- **Text Processing**: <1 second
- **BERT Embedding**: 2-5 seconds
- **Analysis Complete**: 5-10 seconds total
- **Memory Usage**: 1-2GB typical

## Security & Privacy

### Design Principles
1. **Local Processing**: All analysis happens locally, no cloud upload
2. **No Data Persistence**: Resumes not stored after analysis
3. **No Tracking**: No user behavior tracking
4. **PDF Validation**: Input validation for uploaded files

### Best Practices
1. User full control over data
2. No external API calls for analysis
3. Optional report download
4. Clean separation between UI and logic

## Extensibility Points

### Easy to Extend
1. **Add New Roles**: Place PDFs in `data/` subdirectory
2. **Update Skills**: Modify lists in `skill_extractor.py`
3. **Custom Reports**: Add methods to `utils.py`
4. **New Analysis Methods**: Extend `resume_analyzer.py`

### Integration Points
1. **API Access**: All modules have public methods
2. **Batch Processing**: `BatchAnalyzer` for multiple resumes
3. **Report Export**: JSON, CSV, HTML formats
4. **Custom UI**: Replace Streamlit with Flask/FastAPI

## Testing Strategy

### Unit Tests
- PDF extraction correctness
- Skill extraction patterns
- Embedding generation
- Score calculation validation

### Integration Tests
- End-to-end analysis workflow
- Multiple role analysis
- Report generation
- UI interactions

### Validation
- Sample resume benchmarks
- Score consistency checks
- Skill database accuracy
- Performance benchmarks

## Future Enhancements

### Planned Features
1. **Resume Optimization Engine**: Auto-suggest resume rewrites
2. **Skill Development Paths**: Training recommendations
3. **Job Market Analysis**: Trending skills by role
4. **Interview Preparation**: Role-specific tips
5. **Portfolio Integration**: Link to GitHub/portfolio
6. **Real-time Feedback**: As-you-type resume scoring
7. **Multi-language Support**: Support multiple languages
8. **API Backend**: RESTful API for integrations

### Potential Improvements
- Fine-tune BERT for specific domains
- Add resume template recommendations
- Implement collaborative filtering
- Add salary expectations
- Integration with job boards
- ATS (Applicant Tracking System) simulation

---

*Architecture Documentation - ResumeBooster v1.0.0*
