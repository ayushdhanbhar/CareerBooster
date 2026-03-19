"""
ResumeBooster - AI-Powered Resume Analysis Application
Main Streamlit interface for resume analysis using BERT and NLP
"""

import streamlit as st
import os
from pathlib import Path
import json
from datetime import datetime
import logging

from document_processor import DocumentProcessor
from resume_analyzer import ResumeAnalyzer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Streamlit page
st.set_page_config(
    page_title="ResumeBooster - AI Resume Analyzer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #FF6B6B;
        margin-bottom: 30px;
    }
    .score-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 20px 0;
    }
    .score-value {
        font-size: 48px;
        font-weight: bold;
        margin: 10px 0;
    }
    .strength-box {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
    }
    .weakness-box {
        background-color: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
    }
    .suggestion-box {
        background-color: #cce5ff;
        border-left: 4px solid #004085;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        border: 1px solid #dee2e6;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'analyzer' not in st.session_state:
    st.session_state.analyzer = None
    st.session_state.resume_content = None
    st.session_state.analysis_result = None
    st.session_state.selected_role = None

def init_analyzer():
    """Initialize the resume analyzer"""
    data_dir = Path(__file__).parent / "data"
    
    if not data_dir.exists():
        st.error(f"Data directory not found: {data_dir}")
        return None
    
    try:
        analyzer = ResumeAnalyzer(str(data_dir))
        return analyzer
    except Exception as e:
        logger.error(f"Error initializing analyzer: {str(e)}")
        st.error(f"Error initializing analyzer: {str(e)}")
        return None

def display_header():
    """Display application header"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
            <div class='main-header'>
                <h1>🚀 ResumeBooster</h1>
                <h3>AI-Powered Resume Analysis Engine</h3>
                <p>Powered by BERT | Deep Learning | Natural Language Processing</p>
            </div>
        """, unsafe_allow_html=True)

def display_score(score: float, max_score: float = 10):
    """Display resume score with visual indicator"""
    percentage = (score / max_score) * 100
    
    # Color based on score
    if score >= 7.5:
        color = "green"
        rating = "Excellent"
    elif score >= 6.0:
        color = "blue"
        rating = "Good"
    elif score >= 4.5:
        color = "orange"
        rating = "Fair"
    else:
        color = "red"
        rating = "Needs Improvement"
    
    st.markdown(f"""
        <div class='score-container'>
            <div>Resume Match Score</div>
            <div class='score-value'>{score}/10</div>
            <div>{rating}</div>
            <div style='margin-top: 10px; font-size: 14px;'>{percentage:.1f}% Match</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Progress bar
    st.progress(min(score / 10, 1.0))

def display_strengths(strengths: list):
    """Display resume strengths"""
    st.markdown("### ✅ Strengths")
    st.markdown("*Skills and expertise that match the role requirements*")
    
    if strengths:
        for strength in strengths:
            st.markdown(f"""
                <div class='strength-box'>
                    <strong>{strength}</strong>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No matching strengths found. Review your resume content.")

def display_weaknesses(weaknesses: list):
    """Display resume weaknesses"""
    st.markdown("### ⚠️ Weaknesses")
    st.markdown("*Missing or underrepresented skills*")
    
    if weaknesses:
        for weakness in weaknesses[:10]:  # Show top 10
            st.markdown(f"""
                <div class='weakness-box'>
                    <strong>{weakness}</strong>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.success("No significant skill gaps detected!")

def display_suggestions(suggestions: list):
    """Display improvement suggestions"""
    st.markdown("### 💡 Improvement Suggestions")
    st.markdown("*Personalized recommendations to enhance your resume*")
    
    if suggestions:
        for i, suggestion in enumerate(suggestions, 1):
            st.markdown(f"""
                <div class='suggestion-box'>
                    <strong>Suggestion {i}:</strong> {suggestion}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No suggestions at this time - your resume is well-optimized!")

def display_metrics(metrics: dict, role_profile: dict):
    """Display detailed analysis metrics"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class='metric-card'>
                <div style='color: #666; font-size: 12px;'>Semantic Similarity</div>
                <div style='font-size: 24px; font-weight: bold; color: #667eea;'>
                    {:.1%}
                </div>
            </div>
        """.format(metrics.get('semantic_similarity', 0)), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='metric-card'>
                <div style='color: #666; font-size: 12px;'>Skill Overlap</div>
                <div style='font-size: 24px; font-weight: bold; color: #764ba2;'>
                    {:.1f}%
                </div>
            </div>
        """.format(metrics.get('skill_overlap_percentage', 0)), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class='metric-card'>
                <div style='color: #666; font-size: 12px;'>Tech Skills Matched</div>
                <div style='font-size: 24px; font-weight: bold; color: #28a745;'>
                    {}
                </div>
            </div>
        """.format(metrics.get('technical_skill_match', 0)), unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div class='metric-card'>
                <div style='color: #666; font-size: 12px;'>Samples Analyzed</div>
                <div style='font-size: 24px; font-weight: bold; color: #ffc107;'>
                    {}
                </div>
            </div>
        """.format(role_profile.get('samples_analyzed', 0)), unsafe_allow_html=True)

def display_skill_breakdown(resume_skills: dict, role_skills: dict):
    """Display skill breakdown comparison"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Your Skills")
        
        if resume_skills['technical']:
            st.markdown("**Technical Skills:**")
            for skill in resume_skills['technical'][:10]:
                st.markdown(f"- {skill}")
        
        if resume_skills['soft']:
            st.markdown("**Soft Skills:**")
            for skill in resume_skills['soft'][:10]:
                st.markdown(f"- {skill}")
    
    with col2:
        st.markdown("#### Role Requirements")
        
        if role_skills.get('core_skills'):
            st.markdown("**Core Skills:**")
            for skill in role_skills['core_skills'][:8]:
                st.markdown(f"- {skill}")
        
        if role_skills.get('soft_skills'):
            st.markdown("**Soft Skills Needed:**")
            for skill in role_skills['soft_skills'][:8]:
                st.markdown(f"- {skill}")

def display_learning_resources(learning_resources: dict, learning_path: dict):
    """Display personalized learning resource recommendations"""
    st.markdown("### 🎓 Personalized Learning Resources")
    st.markdown("*Learn skills required for your target role through curated online courses and tutorials*")
    
    if not learning_resources:
        st.info("No skill gaps detected - your resume already covers required competencies!")
        return
    
    # Display learning path overview
    st.markdown("#### 📚 Your Learning Path")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Skills to Learn",
            learning_path.get('total_skills_to_learn', 0)
        )
    
    with col2:
        st.metric(
            "Estimated Hours",
            f"{learning_path.get('estimated_total_hours', 0)}+ hours"
        )
    
    with col3:
        st.metric(
            "Target Role",
            learning_path.get('role', 'Unknown')
        )
    
    # Display learning strategy
    st.markdown("#### 🎯 Recommended Learning Strategy")
    for strategy in learning_path.get('learning_strategy', []):
        st.markdown(f"- {strategy}")
    
    st.markdown("---")
    
    # Display skills and resources
    st.markdown("#### 📖 Learning Resources by Skill")
    
    for skill, resources in learning_resources.items():
        with st.expander(f"📚 {skill.title()}", expanded=False):
            # Display courses
            st.markdown(f"**🎓 Online Courses**")
            
            courses = resources.get('courses', [])
            if courses:
                for i, course in enumerate(courses, 1):
                    st.markdown(f"""
                    **{i}. {course['title']}**
                    - Platform: {course.get('platform', 'Unknown')}
                    - Duration: {course.get('duration', 'Self-paced')}
                    - Level: {course.get('level', 'Varies')}
                    - Rating: ⭐ {course.get('rating', 'N/A')}
                    - [View Course]({course.get('url', '#')})
                    """)
            else:
                st.info("No specific courses found. Search on Coursera or Udemy.")
            
            st.markdown("---")
            
            # Display YouTube tutorials
            st.markdown(f"**🎬 YouTube Tutorials**")
            
            tutorials = resources.get('youtube_tutorials', [])
            if tutorials:
                for i, tutorial in enumerate(tutorials, 1):
                    st.markdown(f"""
                    **{i}. {tutorial['title']}**
                    - Channel: {tutorial.get('channel', 'Unknown')}
                    - Duration: {tutorial.get('duration', 'Varies')}
                    - Level: {tutorial.get('level', 'Varies')}
                    
                    Search on YouTube: "{tutorial['title']}" or visit the {tutorial.get('channel', 'channel')} channel
                    """)
            else:
                st.info("No tutorials found. Search YouTube directly.")
    
    st.markdown("---")
    
    # Learning tips
    st.markdown("#### 💡 Learning Tips")
    st.markdown("""
    1. **Start with Fundamentals**: Begin with beginner-level courses before advancing
    2. **Mix Theory & Practice**: Combine video courses with hands-on projects
    3. **Consistent Learning**: Dedicate 30 minutes daily for better retention
    4. **Build Projects**: Create projects to demonstrate your new skills
    5. **Update Resume**: Add newly acquired skills to your resume
    6. **Join Communities**: Engage with online communities for peer support
    """)
    
    # Export learning plan option
    if st.button("📥 Export Learning Plan"):
        plan_text = f"""
PERSONALIZED LEARNING PLAN FOR {learning_path.get('role', 'UNKNOWN').upper()} ROLE
{'=' * 70}

SKILLS TO DEVELOP:
{chr(10).join([f"- {skill}" for skill in learning_resources.keys()])}

ESTIMATED TIME: {learning_path.get('estimated_total_hours', 0)}+ hours

LEARNING STRATEGY:
{chr(10).join(learning_path.get('learning_strategy', []))}

DETAILED RESOURCES:
{chr(10).join([
    f"""
{skill.upper()}:
Courses:
{chr(10).join([f'  - {c["title"]} ({c.get("duration", "N/A")})' for c in learning_resources[skill].get('courses', [])])}
YouTube Tutorials:
{chr(10).join([f'  - {t["title"]} ({t.get("channel", "Unknown")})' for t in learning_resources[skill].get('youtube_tutorials', [])])}
"""
    for skill in learning_resources.keys()
])}
"""
        st.download_button(
            label="Export Learning Plan as Text",
            data=plan_text,
            file_name=f"learning_plan_{learning_path.get('role', 'role')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

def main():
    """Main application logic"""
    
    # Display header
    display_header()
    
    # Sidebar configuration
    with st.sidebar:
        st.markdown("### 📋 Configuration")
        
        # Initialize analyzer
        if st.session_state.analyzer is None:
            st.session_state.analyzer = init_analyzer()
        
        if st.session_state.analyzer is None:
            st.error("Failed to initialize analyzer. Please check your data directory.")
            return
        
        # Get available roles
        available_roles = st.session_state.analyzer.get_available_roles()
        
        if not available_roles:
            st.error("No roles found in data directory")
            return
        
        st.markdown("#### Step 1: Select Target Role")
        selected_role = st.selectbox(
            "Choose a job role:",
            available_roles,
            help="Select the role you want to analyze your resume against"
        )
        
        st.session_state.selected_role = selected_role
        
        st.markdown("---")
        st.markdown("#### Step 2: Upload Resume")
        
        uploaded_file = st.file_uploader(
            "Upload your resume (PDF)",
            type=['pdf'],
            help="Upload your resume in PDF format for analysis"
        )
        
        analyze_button = st.button(
            "🔍 Analyze Resume",
            use_container_width=True,
            help="Click to analyze your resume against the selected role"
        )
        
        if analyze_button and uploaded_file:
            with st.spinner("Processing your resume..."):
                try:
                    # Extract text from uploaded PDF
                    resume_bytes = uploaded_file.read()
                    resume_text = DocumentProcessor.extract_text_from_bytes(resume_bytes)
                    
                    if not resume_text:
                        st.error("Could not extract text from PDF. Please try another file.")
                        return
                    
                    st.session_state.resume_content = resume_text
                    
                    # Analyze resume
                    analysis = st.session_state.analyzer.analyze_resume(
                        resume_text,
                        selected_role
                    )
                    
                    st.session_state.analysis_result = analysis
                    st.success("Resume analyzed successfully!")
                    
                except Exception as e:
                    logger.error(f"Analysis error: {str(e)}")
                    st.error(f"Error analyzing resume: {str(e)}")
    
    # Main content area
    if st.session_state.analysis_result:
        analysis = st.session_state.analysis_result
        
        st.markdown(f"### Analysis Results for **{analysis['role']}** Role")
        st.markdown("---")
        
        # Display score
        display_score(analysis['resume_score'])
        
        # Create tabs for different sections
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "📊 Overview",
            "✅ Strengths",
            "⚠️ Weaknesses",
            "💡 Suggestions",
            "🎓 Learning Resources",
            "📈 Detailed Metrics"
        ])
        
        with tab1:
            st.markdown("#### Resume Match Analysis")
            st.markdown(f"""
            Your resume shows a **{analysis['resume_score']}/10** alignment with the **{analysis['role']}** role.
            
            This score is based on:
            - **Semantic similarity** between your resume and role requirements
            - **Skill overlap** with the role's core competencies
            - **Content relevance** and keyword matching
            - **Professional completeness** of your resume
            """)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Score Breakdown")
                for key, value in analysis['score_breakdown'].items():
                    if 'percentage' in key:
                        st.metric(key.replace('_', ' ').title(), f"{value:.1f}%")
                    else:
                        st.metric(key.replace('_', ' ').title(), f"{value:.2%}")
            
            with col2:
                st.markdown("#### Role Profile")
                profile = analysis['role_profile']
                st.metric("Samples Analyzed", f"{profile.get('samples_analyzed', 0)} resumes")
                st.markdown(f"**Top Tools Used:** {', '.join([t.title() for t in profile.get('tools', [])[:5]])}")
        
        with tab2:
            display_strengths(analysis['strengths'])
        
        with tab3:
            display_weaknesses(analysis['weaknesses'])
        
        with tab4:
            display_suggestions(analysis['suggestions'])
        
        with tab5:
            display_learning_resources(
                analysis.get('learning_resources', {}),
                analysis.get('learning_path', {})
            )
        
        with tab6:
            st.markdown("#### Detailed Analysis Metrics")
            display_metrics(analysis['score_breakdown'], analysis['role_profile'])
            
            st.markdown("---")
            
            st.markdown("#### Skill Comparison")
            display_skill_breakdown(
                analysis['resume_skills'],
                analysis['role_profile']
            )
            
            st.markdown("---")
            
            st.markdown("#### Advanced Metrics")
            detailed = analysis['detailed_metrics']
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Technical Skills Matched", detailed.get('technical_skill_match', 0))
            with col2:
                st.metric("Soft Skills Matched", detailed.get('soft_skill_match', 0))
            with col3:
                st.metric("Total Resume Skills", detailed.get('total_resume_skills', 0))
            with col4:
                st.metric("Role Coverage", f"{detailed.get('role_requirement_coverage', 0):.1f}%")
        
        # Download report button
        st.markdown("---")
        st.markdown("### 📥 Download Your Complete Report")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📄 Download PDF Report", use_container_width=True):
                try:
                    from utils import ReportGenerator
                    
                    # Generate PDF
                    pdf_bytes = ReportGenerator.generate_pdf_report(analysis)
                    
                    st.download_button(
                        label="📥 Save PDF Report",
                        data=pdf_bytes,
                        file_name=f"resume_analysis_{analysis['role']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                        mime="application/pdf",
                        key="pdf_download"
                    )
                except ImportError:
                    st.error("❌ PDF export requires reportlab. Install with: pip install reportlab Pillow")
                except Exception as e:
                    st.error(f"Error generating PDF: {str(e)}")
        
        with col2:
            if st.button("📋 Download JSON Report", use_container_width=True):
                report = {
                    'timestamp': datetime.now().isoformat(),
                    'role': analysis['role'],
                    'resume_score': analysis['resume_score'],
                    'strengths': analysis['strengths'],
                    'weaknesses': analysis['weaknesses'],
                    'suggestions': analysis['suggestions'],
                    'metrics': analysis['detailed_metrics']
                }
                
                report_json = json.dumps(report, indent=2)
                st.download_button(
                    label="📥 Save JSON Report",
                    data=report_json,
                    file_name=f"resume_analysis_{analysis['role']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json",
                    key="json_download"
                )
        
        with col3:
            if st.button("📊 Download Learning Plan", use_container_width=True):
                learning_path = analysis.get('learning_path', {})
                learning_resources = analysis.get('learning_resources', {})
                
                if learning_resources:
                    plan_text = f"""PERSONALIZED LEARNING PLAN FOR {learning_path.get('role', 'UNKNOWN').upper()} ROLE
{'=' * 80}

GENERATED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

OVERVIEW:
- Target Role: {learning_path.get('role', 'Unknown')}
- Skills to Learn: {learning_path.get('total_skills_to_learn', 0)}
- Estimated Learning Time: {learning_path.get('estimated_total_hours', 0)}+ hours
- Resume Score: {analysis.get('resume_score', 0)}/10

LEARNING STRATEGY:
{chr(10).join([f"{i}. {step}" for i, step in enumerate(learning_path.get('learning_strategy', []), 1)])}

RECOMMENDED RESOURCES BY SKILL:
{'=' * 80}
"""
                    for skill, resources in learning_resources.items():
                        plan_text += f"\n{skill.upper()}\n{'-' * 40}\n"
                        
                        courses = resources.get('courses', [])
                        if courses:
                            plan_text += "ONLINE COURSES:\n"
                            for i, course in enumerate(courses, 1):
                                plan_text += f"  {i}. {course.get('title', 'Unknown')}\n"
                                plan_text += f"     Platform: {course.get('platform', 'Unknown')}\n"
                                plan_text += f"     Duration: {course.get('duration', 'N/A')}\n"
                                plan_text += f"     Level: {course.get('level', 'N/A')}\n"
                                if course.get('rating'):
                                    plan_text += f"     Rating: ⭐ {course['rating']}/5\n"
                                plan_text += "\n"
                        
                        tutorials = resources.get('youtube_tutorials', [])
                        if tutorials:
                            plan_text += "YOUTUBE TUTORIALS:\n"
                            for i, tutorial in enumerate(tutorials, 1):
                                plan_text += f"  {i}. {tutorial.get('title', 'Unknown')}\n"
                                plan_text += f"     Channel: {tutorial.get('channel', 'Unknown')}\n"
                                plan_text += f"     Duration: {tutorial.get('duration', 'N/A')}\n"
                                plan_text += f"     Level: {tutorial.get('level', 'N/A')}\n\n"
                    
                    st.download_button(
                        label="📥 Save Learning Plan",
                        data=plan_text,
                        file_name=f"learning_plan_{analysis['role']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain",
                        key="learning_download"
                    )
                else:
                    st.info("No learning resources found for this analysis.")
    
    else:
        # Welcome message
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            st.markdown("""
            ### 👋 Welcome to ResumeBooster!
            
            **How it works:**
            
            1. **Select a Role** - Choose from various job categories in the sidebar
            2. **Upload Your Resume** - Submit your resume in PDF format
            3. **Get Analysis** - Our AI analyzes your resume using advanced NLP and BERT embeddings
            4. **Review Results** - Get detailed insights on strengths, weaknesses, and improvement suggestions
            
            ---
            
            ### 🎯 What You'll Get:
            
            ✅ **Resume Score (0-10)** - Overall match percentage
            
            ✅ **Strengths** - Skills you have that match the role
            
            ✅ **Weaknesses** - Missing skills and competencies
            
            ✅ **Suggestions** - Personalized recommendations to improve
            
            ✅ **Detailed Metrics** - In-depth analysis with multiple scoring factors
            
            ---
            
            ### 🚀 Get Started:
            
            👉 Use the sidebar to select a role and upload your resume!
            """)

if __name__ == "__main__":
    main()
