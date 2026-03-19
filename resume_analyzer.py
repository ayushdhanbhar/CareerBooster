"""
Resume Analyzer and Scoring Module
Main logic for analyzing resumes against job roles
"""

from typing import Dict, Tuple, List
import logging
from document_processor import DocumentProcessor
from skill_extractor import SkillExtractor
from bert_embedder import BertEmbedder
from role_profile_builder import RoleProfileBuilder

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ResumeAnalyzer:
    """Analyze resume and generate detailed evaluation"""
    
    def __init__(self, data_dir: str):
        """
        Initialize the resume analyzer
        
        Args:
            data_dir: Path to data directory with role subdirectories
        """
        self.embedder = BertEmbedder()
        self.profile_builder = RoleProfileBuilder(data_dir)
    
    def analyze_resume(self, resume_text: str, role: str) -> Dict[str, any]:
        """
        Perform complete resume analysis for a role
        
        Args:
            resume_text: Extracted resume text
            role: Target job role
            
        Returns:
            Comprehensive analysis dictionary
        """
        try:
            # Extract skills from resume
            resume_skills = SkillExtractor.extract_skills(resume_text)
            
            # Get role profile
            role_profile = self.profile_builder.get_role_profile(role)
            
            # Analyze skills
            skill_analysis = SkillExtractor.analyze_skills(resume_skills, role)
            
            # Calculate semantic similarity
            role_description = self._build_role_description(role_profile)
            similarity_metrics = self.embedder.compare_documents(
                resume_text, 
                role_description,
                method='cosine'
            )
            
            # Enhanced similarity with chunking
            sectional_similarity = self.embedder.get_sectional_similarity(
                resume_text,
                role_description
            )
            
            # Calculate overall score (0-10)
            score = self._calculate_score(
                similarity_metrics['similarity_score'],
                sectional_similarity['average_similarity'],
                skill_analysis['skill_overlap_percentage'],
                resume_skills
            )
            
            # Generate personalized suggestions
            suggestions = self._generate_suggestions(
                skill_analysis,
                role,
                resume_text,
                resume_skills
            )
            
            analysis = {
                'role': role,
                'resume_score': score,
                'score_breakdown': {
                    'semantic_similarity': similarity_metrics['similarity_score'],
                    'sectional_similarity': sectional_similarity['average_similarity'],
                    'skill_overlap_percentage': skill_analysis['skill_overlap_percentage'],
                    'max_section_match': sectional_similarity['max_match'],
                    'min_section_match': sectional_similarity['min_match']
                },
                'strengths': skill_analysis['strengths'][:10],  # Top 10
                'weaknesses': skill_analysis['weaknesses'][:10],  # Top 10
                'resume_skills': resume_skills,
                'role_profile': {
                    'core_skills': role_profile.get('core_skills', []),
                    'soft_skills': role_profile.get('soft_skills', []),
                    'tools': role_profile.get('tools', []),
                    'samples_analyzed': role_profile.get('sample_count', 0)
                },
                'suggestions': suggestions,
                'detailed_metrics': {
                    'technical_skill_match': len([s for s in skill_analysis['strengths'] if s in resume_skills['technical']]),
                    'soft_skill_match': len([s for s in skill_analysis['strengths'] if s in resume_skills['soft']]),
                    'total_resume_skills': len(resume_skills['technical']) + len(resume_skills['soft']),
                    'role_requirement_coverage': skill_analysis['skill_overlap_percentage']
                }
            }
            
            return analysis
            
        except Exception as e:
            logger.error(f"Error analyzing resume: {str(e)}")
            raise
    
    def _build_role_description(self, role_profile: Dict) -> str:
        """
        Build a comprehensive role description from profile
        
        Args:
            role_profile: Role profile dictionary
            
        Returns:
            Role description text
        """
        parts = [
            f"Role: {role_profile.get('role', 'Unknown')}",
            "Core Skills: " + ", ".join(role_profile.get('core_skills', [])),
            "Soft Skills: " + ", ".join(role_profile.get('soft_skills', [])),
            "Tools and Technologies: " + ", ".join(role_profile.get('tools', []))
        ]
        
        # Add sample text if available
        if role_profile.get('combined_text'):
            parts.append(role_profile['combined_text'])
        
        return " ".join(parts)
    
    def _calculate_score(self, semantic_sim: float, sectional_sim: float, 
                         skill_overlap: float, resume_skills: Dict) -> float:
        """
        Calculate overall resume score (0-10)
        
        Args:
            semantic_sim: Semantic similarity score (0-1)
            sectional_sim: Sectional similarity score (0-1)
            skill_overlap: Skill overlap percentage (0-100)
            resume_skills: Extracted resume skills
            
        Returns:
            Score between 0 and 10
        """
        # Weights for different factors
        weights = {
            'semantic': 0.35,
            'sectional': 0.25,
            'skill_overlap': 0.30,
            'resume_completeness': 0.10
        }
        
        # Normalize skill overlap to 0-1
        skill_overlap_normalized = skill_overlap / 100
        
        # Calculate completeness based on number of skills
        total_skills = len(resume_skills['technical']) + len(resume_skills['soft'])
        completeness = min(1.0, total_skills / 20)  # Expect at least 20 skills
        
        # Calculate weighted score
        weighted_score = (
            semantic_sim * weights['semantic'] +
            sectional_sim * weights['sectional'] +
            skill_overlap_normalized * weights['skill_overlap'] +
            completeness * weights['resume_completeness']
        )
        
        # Scale to 0-10
        score = weighted_score * 10
        
        # Apply some smoothing to avoid extreme outliers
        score = min(10, max(0, score))
        
        return round(score, 2)
    
    def _generate_suggestions(self, skill_analysis: Dict, role: str,
                            resume_text: str, resume_skills: Dict) -> List[str]:
        """
        Generate personalized improvement suggestions
        
        Args:
            skill_analysis: Results from skill analysis
            role: Target role
            resume_text: Original resume text
            resume_skills: Extracted resume skills
            
        Returns:
            List of suggestion strings
        """
        suggestions = []
        
        # Missing critical skills
        weaknesses = skill_analysis['weaknesses']
        if weaknesses:
            top_missing = weaknesses[:5]
            skills_str = ", ".join(top_missing)
            suggestions.append(
                f"Add expertise in key skills: {skills_str}. Consider taking courses "
                f"or highlighting related experience."
            )
        
        # Low skill overlap
        if skill_analysis['skill_overlap_percentage'] < 50:
            suggestions.append(
                "Your resume lacks several skills required for this role. Focus on "
                "identifying and highlighting transferable skills and experiences."
            )
        elif skill_analysis['skill_overlap_percentage'] < 75:
            suggestions.append(
                "You have most required skills but are missing some important ones. "
                "Consider developing or highlighting these missing competencies."
            )
        
        # Enhance descriptions with keywords
        role_profile = skill_analysis['role_profile']
        role_tools = role_profile.get('tools', [])
        missing_tools = [t for t in role_tools if t not in resume_skills['technical']]
        
        if missing_tools:
            top_tools = missing_tools[:3]
            tools_str = ", ".join(top_tools)
            suggestions.append(
                f"Highlight or gain experience with these tools: {tools_str}. "
                f"These are commonly used in {role} positions."
            )
        
        # Soft skills recommendations
        role_soft = role_profile.get('soft_skills', [])
        missing_soft = [s for s in role_soft if s not in resume_skills['soft']]
        
        if missing_soft:
            suggestions.append(
                f"Emphasize soft skills such as {', '.join(missing_soft[:3])} "
                f"through concrete examples and achievements."
            )
        
        # General content recommendations
        if len(resume_text) < 1000:
            suggestions.append(
                "Your resume seems brief. Add more detail about your achievements, "
                "projects, and relevant experience to better showcase your qualifications."
            )
        
        # Engagement recommendations
        role_keywords = role_profile.get('core_skills', [])
        missing_keywords = [k for k in role_keywords if k not in resume_text.lower()]
        
        if missing_keywords and len(missing_keywords) > 5:
            top_keywords = missing_keywords[:5]
            suggestions.append(
                f"Incorporate industry keywords: {', '.join(top_keywords)}. "
                f"These help with keyword matching in applicant tracking systems."
            )
        
        # Action-oriented recommendations
        suggestions.append(
            f"Consider adding a summary or objective statement at the top that clearly "
            f"mentions your interest and qualifications for {role} roles."
        )
        
        return suggestions
    
    def get_available_roles(self) -> List[str]:
        """Get list of available roles for analysis"""
        return self.profile_builder.get_available_roles()
