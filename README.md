# 🚀 ResumeBooster - AI-Powered Resume Analysis Engine

## Overview

**ResumeBooster** is an intelligent resume analysis application that uses advanced **BERT-based Natural Language Processing** and **Deep Learning** to evaluate how well a candidate's resume aligns with a selected job role. The system provides detailed insights including resume scoring, skill analysis, strengths/weaknesses identification, and personalized improvement suggestions.

## 🎯 Key Features

### 1. **Role-Based Analysis**
- Select from 24+ job categories (Accountant, Advocate, Engineer, Designer, etc.)
- Profiles learned from 100s of real resumes in each category
- Dynamic role requirement extraction from actual resume datasets

### 2. **Resume Upload & Processing**
- Upload resumes in PDF format
- Automatic text extraction using advanced PDF processing
- Handling of complex PDF layouts and formatting

### 3. **BERT-Powered Semantic Analysis**
- Uses state-of-the-art sentence-transformers (DistilBERT)
- Converts resume and role descriptions into semantic embeddings
- Measures semantic similarity through cosine distance
- Chunk-based analysis for comprehensive content evaluation

### 4. **Comprehensive Scoring System**
- **10-point scale** reflecting overall suitability
- Multi-factor scoring:
  - Semantic similarity (35%)
  - Sectional content relevance (25%)
  - Skill overlap analysis (30%)
  - Resume completeness (10%)

### 5. **Detailed Skill Analysis**
- **Strengths**: Matching skills with role requirements
- **Weaknesses**: Missing or underrepresented competencies
- **Technical vs Soft Skills**: Separate tracking of different skill types
- Database of 100+ technical and soft skills

### 6. **Personalized Improvement Suggestions**
- Context-aware recommendations
- Missing keyword suggestions
- Tool and technology recommendations
- Formatting and content enhancement tips

### 7. **Interactive Streamlit Dashboard**
- Clean, modern UI
- Real-time analysis
- Tabbed interface for organized results
- Visual metrics and progress indicators
- Downloadable analysis reports (JSON)

## 📋 Available Job Roles

The system analyzes resumes against these job categories:

- **ACCOUNTANT** - Tax, auditing, financial reporting
- **ADVOCATE** - Legal research, litigation, contract drafting
- **AGRICULTURE** - Farming, agricultural management
- **APPAREL** - Fashion, textile design
- **ARTS** - Creative fields, artistic pursuits
- **AUTOMOBILE** - Automotive engineering, mechanics
- **AVIATION** - Pilot, aircraft maintenance
- **BANKING** - Commercial banking, finance
- **BPO** - Business process outsourcing
- **BUSINESS-DEVELOPMENT** - Sales, market expansion
- **CHEF** - Culinary arts, food service
- **CONSTRUCTION** - Building, project management
- **CONSULTANT** - Business consulting, strategy
- **DESIGNER** - UI/UX, graphic design
- **DIGITAL-MEDIA** - Social media, content creation
- **ENGINEERING** - Software, civil, mechanical engineering
- **FINANCE** - Financial analysis, investment
- **FITNESS** - Personal training, wellness
- **HEALTHCARE** - Medicine, nursing, health
- **HR** - Human resources, recruitment
- **INFORMATION-TECHNOLOGY** - IT, software development
- **PUBLIC-RELATIONS** - PR, communications
- **SALES** - Sales, business development
- **TEACHER** - Education, curriculum design

## 🛠️ System Architecture

### Core Modules

#### 1. **document_processor.py**
Handles PDF extraction and text processing
- `extract_text_from_pdf()` - Extract text from PDF files
- `extract_text_from_bytes()` - Process PDF bytes
- `clean_text()` - Normalize and clean extracted text

#### 2. **skill_extractor.py**
Extracts and analyzes skills from resume text
- `extract_skills()` - Find technical and soft skills
- `get_role_profile()` - Get skill requirements for roles
- `analyze_skills()` - Compare resume with role requirements
- Database of 100+ technical and 30+ soft skills

#### 3. **bert_embedder.py**
Generates semantic embeddings using BERT
- Uses `sentence-transformers/all-MiniLM-L6-v2`
- `get_embedding()` - Single text embedding
- `get_embeddings_batch()` - Batch processing
- `cosine_similarity()` - Semantic comparison
- `get_chunk_embeddings()` - Section-by-section analysis

#### 4. **role_profile_builder.py**
Builds role profiles from sample resumes
- Discovers available roles from data directory
- Analyzes 10+ sample resumes per role
- Extracts common skills and tools
- Creates benchmark profiles for comparison

#### 5. **resume_analyzer.py**
Main analysis engine combining all components
- `analyze_resume()` - Complete analysis workflow
- Multi-factor scoring calculation
- Suggestion generation
- Result aggregation and formatting

#### 6. **app.py**
Streamlit web interface
- Role selection interface
- PDF upload and processing
- Real-time analysis display
- Tabbed results interface
- Report generation and download

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- ~2GB disk space for models

### Step 1: Install Dependencies

```bash
# Navigate to project directory
cd d:\CareerBooster

# Install required packages
pip install -r requirements.txt

# Download BERT model (one-time)
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"
```

### Step 2: Run the Application

```bash
# Start Streamlit app
streamlit run app.py

# The app will open in your default browser at http://localhost:8501
```

### Step 3: Use the Application

1. **Select a Role** - Choose from the dropdown in the sidebar
2. **Upload Resume** - Click "Browse Files" and select your PDF resume
3. **Click Analyze** - Press the "🔍 Analyze Resume" button
4. **Review Results** - Explore the detailed analysis in the tabs:
   - Overview: Summary and key metrics
   - Strengths: Matching skills
   - Weaknesses: Missing skills
   - Suggestions: Improvement recommendations
   - Detailed Metrics: Advanced analytics

## 🔍 How It Works

### Analysis Workflow

```
1. User Selects Role
   ↓
2. User Uploads Resume (PDF)
   ↓
3. System Extracts Text from PDF
   ↓
4. Skill Extraction (Technical & Soft)
   ↓
5. Role Profile Generation from Dataset
   ↓
6. BERT Embedding Generation
   ↓
7. Semantic Similarity Calculation
   ↓
8. Skill Overlap Analysis
   ↓
9. Multi-Factor Scoring (0-10)
   ↓
10. Suggestion Generation
    ↓
11. Results Display in Dashboard
```

### Scoring Methodology

The resume score (0-10) is calculated using:

**Score = (0.35 × Semantic Similarity) + (0.25 × Sectional Relevance) + (0.30 × Skill Overlap) + (0.10 × Completeness) × 10**

Where:
- **Semantic Similarity**: Measures linguistic alignment between resume and role requirements using cosine distance of BERT embeddings
- **Sectional Relevance**: Evaluates content relevance by analyzing resume sections independently
- **Skill Overlap**: Percentage of required skills present in the resume
- **Completeness**: Measure of resume detail and skill count (expects 20+ distinct skills)

### Score Interpretation

- **9.0 - 10.0**: Excellent match - Highly qualified for the role
- **7.5 - 8.9**: Good match - Strong candidate with minor gaps
- **6.0 - 7.4**: Fair match - Qualified with some skill gaps
- **4.5 - 5.9**: Weak match - Significant gaps in requirements
- **Below 4.5**: Poor match - Major skill and experience gaps

## 📊 Results Interpretation

### Strengths
Skills and experiences present in your resume that directly match the role's requirements. These are your competitive advantages.

### Weaknesses
Skills that are commonly required for the role but missing or underrepresented in your resume. Prioritize these for improvement.

### Suggestions
Personalized, actionable recommendations to enhance your resume:
- Add specific technical skills or tools
- Highlight soft skills with concrete examples
- Improve keyword density for ATS matching
- Add more detail about achievements
- Include industry-specific terminology

## 💡 Tips for Better Results

### Resume Preparation
1. **Use Standard Format** - Clear structure with distinct sections
2. **Use Relevant Keywords** - Include industry-specific terminology
3. **Quantify Achievements** - Use numbers, metrics, and results
4. **Highlight Relevant Experience** - Emphasize role-related projects
5. **Include Skills Section** - Explicitly list technical and soft skills

### Maximizing Your Score
1. **Match Keywords** - Follow suggestions to add recommended terms
2. **Depth Over Breadth** - Detail relevant skills thoroughly
3. **Show Growth** - Demonstrate progression and continuous learning
4. **Use Industry Tools** - Mention specific tools and technologies
5. **Soft Skills Matter** - Include leadership, communication, teamwork

## 📈 Example Analysis Output

### Resume Score
**8.2 / 10** - Good Match (82%)

### Score Breakdown
- Semantic Similarity: 78.5%
- Sectional Relevance: 75.2%
- Skill Overlap: 82.3%
- Resume Completeness: 95%

### Top Strengths (Found)
- Python Programming
- Machine Learning
- Data Analysis
- Problem Solving
- Communication Skills

### Top Weaknesses (Missing)
- TensorFlow Framework
- Cloud Computing (AWS/GCP)
- Statistical Analysis
- Project Management
- Leadership Experience

### Suggestions
1. "Add expertise in: TensorFlow, PyTorch, and deep learning frameworks..."
2. "Highlight or gain experience with: AWS, Google Cloud Platform..."
3. "Emphasize soft skills such as: project management, leadership..."
4. "Add more detail about your achievements, projects, and relevant..."

## 🔧 Customization

### Adding New Job Roles
1. Add new directory in `data/` folder with role name
2. Place resume PDFs in the new directory
3. Restart the application
4. New role will appear in the selection dropdown

### Modifying Skill Database
Edit `skill_extractor.py`:
```python
TECHNICAL_SKILLS = {
    'your-new-skill',
    # ... other skills
}

SOFT_SKILLS = {
    'another-new-skill',
    # ... other skills
}
```

### Adjusting Scoring Weights
Edit `resume_analyzer.py` in `_calculate_score()` method:
```python
weights = {
    'semantic': 0.35,      # Adjust these values
    'sectional': 0.25,     # Sum must equal 1.0
    'skill_overlap': 0.30,
    'resume_completeness': 0.10
}
```

## 📁 Project Structure

```
d:\CareerBooster\
├── app.py                      # Main Streamlit application
├── document_processor.py       # PDF extraction module
├── skill_extractor.py          # Skill analysis module
├── bert_embedder.py            # BERT embedding module
├── role_profile_builder.py     # Role profile builder
├── resume_analyzer.py          # Main analysis engine
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── data/                       # Resume datasets
│   ├── ACCOUNTANT/
│   ├── ADVOCATE/
│   ├── ENGINEER/
│   ├── CONSULTANT/
│   ├── DESIGNER/
│   ├── SALES/
│   ├── HR/
│   ├── MARKETING/
│   └── ... (24+ categories)
└── Resume.csv                  # Resume metadata
```

## 🐛 Troubleshooting

### Issue: "Data directory not found"
- Ensure `data/` folder exists in the same directory as `app.py`
- Check that role subfolders are present

### Issue: Model loading takes too long
- First run downloads the BERT model (~50MB)
- Subsequent runs will use cached model
- Ensure stable internet connection for first initialization

### Issue: PDF extraction returns empty text
- Some PDFs have image-based text or are scanned documents
- Try re-saving PDF with text layer
- Ensure PDF is not encrypted or password-protected

### Issue: Low resume score even with relevant skills
- Add more explicit keywords matching role requirements
- Increase detail and description in resume sections
- Ensure skills are mentioned multiple times
- Check that PDF text extracts correctly

### Issue: Key role not in the list
- Add subdirectory under `data/` with role name
- Add sample PDF resumes to the directory
- Restart the application

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```

### Production Deployment (Streamlit Cloud)
1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Configure `streamlit/config.toml` for production
4. Deploy automatically on push

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 📚 Technical Details

### BERT Model Used
- **Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Dimensions**: 384
- **Parameters**: 22.7M
- **Speed**: Fast inference suitable for real-time analysis
- **Accuracy**: Excellent semantic understanding

### Dependencies
- **streamlit**: Web UI framework
- **transformers**: BERT model loading
- **sentence-transformers**: Efficient embedding generation
- **torch**: Deep learning backend
- **pdfplumber**: Advanced PDF text extraction
- **scikit-learn**: ML utilities
- **numpy/pandas**: Data processing

## 📝 API Reference

### ResumeAnalyzer

```python
from resume_analyzer import ResumeAnalyzer

# Initialize
analyzer = ResumeAnalyzer(data_dir="path/to/data")

# Get available roles
roles = analyzer.get_available_roles()

# Analyze resume
result = analyzer.analyze_resume(
    resume_text="Resume content...",
    role="ENGINEER"
)

# Access results
score = result['resume_score']
strengths = result['strengths']
weaknesses = result['weaknesses']
suggestions = result['suggestions']
```

### BertEmbedder

```python
from bert_embedder import BertEmbedder

embedder = BertEmbedder()

# Get embedding
embedding = embedder.get_embedding("Your text here")

# Compare documents
similarity = embedder.compare_documents(text1, text2)

# Get sectional similarity
detailed = embedder.get_sectional_similarity(resume_text, role_text)
```

### SkillExtractor

```python
from skill_extractor import SkillExtractor

# Extract skills
skills = SkillExtractor.extract_skills("Resume text")

# Get role requirements
profile = SkillExtractor.get_role_profile("ENGINEER")

# Analyze skills
analysis = SkillExtractor.analyze_skills(resume_skills, "ENGINEER")
```

## 🤝 Contributing

To improve the system:

1. Add more sample resumes to role directories
2. Expand skill database in `skill_extractor.py`
3. Improve suggestion generation logic
4. Enhance UI/UX in `app.py`
5. Optimize performance of BERT embeddings

## 📄 License

This project is provided as-is for educational and professional use.

## 🙏 Acknowledgments

- Hugging Face for transformer models
- Streamlit for the web framework
- Sentence-Transformers for embeddings
- All contributors and users

## 📞 Support

For issues, questions, or suggestions:
1. Check the Troubleshooting section
2. Review the How It Works section
3. Examine error logs and console output
4. Ensure all dependencies are correctly installed

---

**Happy Resume Boosting! 🚀**

*Transform your resume and land your dream role with AI-powered insights.*
