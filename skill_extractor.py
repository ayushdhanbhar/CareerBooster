"""
Skill Extraction and Analysis Module
Identifies skills from resume text and analyzes against role requirements
"""

import re
from typing import List, Set, Dict, Tuple
from collections import Counter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SkillExtractor:
    """Extract and analyze skills from resume text"""
    
    # Common technical and professional skills database
    TECHNICAL_SKILLS = {
        'python', 'java', 'javascript', 'c++', 'c#', 'sql', 'r', 'php', 'ruby',
        'golang', 'swift', 'kotlin', 'scala', 'perl', 'matlab', 'bash', 'shell',
        'html', 'css', 'react', 'angular', 'vue', 'node.js', 'express', 'django',
        'flask', 'spring', 'fastapi', 'tensorflow', 'pytorch', 'keras', 'scikit-learn',
        'pandas', 'numpy', 'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'git',
        'jenkins', 'gitlab', 'github', 'bitbucket', 'jira', 'confluence', 'linux',
        'windows', 'macos', 'sql server', 'mysql', 'postgresql', 'mongodb', 'redis',
        'elasticsearch', 'kafka', 'rabbitmq', 'rest api', 'graphql', 'microservices',
        'api', 'json', 'xml', 'yaml', 'devops', 'ci/cd', 'agile', 'scrum', 'kanban',
        'jira', 'asana', 'tableau', 'power bi', 'excel', 'vba', 'salesforce', 'oracle',
        'sap', 'erp', 'crm', 'bi', 'etl', 'data warehouse', 'data mining', 'nlp',
        'machine learning', 'deep learning', 'computer vision', 'nlp', 'bert', 'gpt',
        'transformer', 'neural network', 'regression', 'classification', 'clustering',
        'iot', 'embedded systems', 'blockchain', 'cryptocurrency', 'web development',
        'mobile development', 'android', 'ios', 'react native', 'flutter', 'xamarin',
        'ux design', 'ui design', 'figma', 'sketch', 'adobe xd', 'adobe photoshop',
        'adobe illustrator', 'graphic design', 'marketing', 'seo', 'sem', 'ppc',
        'email marketing', 'content marketing', 'social media', 'analytics', 'google analytics',
        'financial modeling', 'valuation', 'corporate finance', 'investment banking',
        'hedge fund', 'private equity', 'venture capital', 'accounting', 'auditing',
        'tax', 'compliance', 'gdpr', 'iso', 'Prince2', 'pmp', 'capm', 'cfa',
    }
    
    SOFT_SKILLS = {
        'communication', 'leadership', 'teamwork', 'collaboration', 'problem solving',
        'critical thinking', 'time management', 'organization', 'attention to detail',
        'adaptability', 'flexibility', 'creativity', 'innovation', 'customer service',
        'negotiation', 'presentation', 'public speaking', 'written communication',
        'emotional intelligence', 'interpersonal skills', 'project management',
        'stakeholder management', 'conflict resolution', 'decision making',
        'analytical thinking', 'strategic thinking', 'research', 'planning',
        'delegation', 'coaching', 'mentoring', 'training', 'multi-tasking',
        'learning', 'professional development', 'networking', 'relationship building'
    }
    
    # Role-specific skill mappings
    ROLE_SKILL_PROFILES = {
        'ACCOUNTANT': {
            'core': ['accounting', 'tax', 'auditing', 'financial reporting', 'gaap',
                    'ifrs', 'journal entries', 'general ledger', 'reconciliation',
                    'accounts receivable', 'accounts payable', 'payroll'],
            'tools': ['excel', 'quickbooks', 'sap', 'oracle', 'dynamics', 'xero',
                     'wave', 'zoho', 'sql', 'tableau', 'power bi'],
            'soft': ['attention to detail', 'communication', 'analytical thinking',
                    'time management', 'problem solving']
        },
        'ADVOCATE': {
            'core': ['legal research', 'contract drafting', 'litigation', 'case law',
                    'legal writing', 'negotiation', 'client counseling', 'court procedure'],
            'tools': ['westlaw', 'lexisnexis', 'legal precedent', 'pleadings',
                     'discovery', 'legal database', 'contract management'],
            'soft': ['communication', 'critical thinking', 'analytical skills',
                    'persuasion', 'negotiation', 'attention to detail']
        },
        'ENGINEER': {
            'core': ['programming', 'software design', 'system architecture', 'debugging',
                    'testing', 'version control', 'code review', 'optimization'],
            'tools': ['python', 'java', 'c++', 'git', 'jenkins', 'docker', 'kubernetes',
                     'aws', 'azure', 'databases'],
            'soft': ['problem solving', 'teamwork', 'communication', 'analytical thinking',
                    'creativity', 'documentation']
        },
        'DATA ANALYST': {
            'core': ['data analysis', 'statistical analysis', 'data visualization',
                    'database querying', 'data cleaning', 'predictive modeling'],
            'tools': ['sql', 'python', 'r', 'tableau', 'power bi', 'excel', 'pandas',
                     'numpy', 'scikit-learn', 'matplotlib'],
            'soft': ['analytical thinking', 'communication', 'attention to detail',
                    'problem solving', 'business acumen']
        },
        'CONSULTANT': {
            'core': ['business analysis', 'problem solving', 'strategic planning',
                    'process improvement', 'change management', 'business modeling'],
            'tools': ['microsoft office', 'powerpoint', 'excel', 'statistical software',
                     'project management tools', 'data analysis'],
            'soft': ['communication', 'leadership', 'presentation', 'negotiation',
                    'client management', 'strategic thinking']
        },
        'DESIGNER': {
            'core': ['ui design', 'ux design', 'design thinking', 'wireframing',
                    'prototyping', 'user research', 'information architecture'],
            'tools': ['figma', 'sketch', 'adobe xd', 'photoshop', 'illustrator',
                     'prototyping tools', 'usability testing'],
            'soft': ['creativity', 'communication', 'collaboration', 'problem solving',
                    'attention to detail', 'user empathy']
        },
        'SALES': {
            'core': ['sales', 'lead generation', 'customer relationship', 'negotiation',
                    'closing', 'pipeline management', 'territory management'],
            'tools': ['salesforce', 'crm', 'linkedin', 'email marketing', 'sales analytics'],
            'soft': ['communication', 'persuasion', 'relationship building', 'negotiation',
                    'customer service', 'persistence']
        },
        'MARKETING': {
            'core': ['marketing strategy', 'digital marketing', 'seo', 'sem', 'social media',
                    'content marketing', 'brand management', 'market research'],
            'tools': ['google analytics', 'facebook ads', 'mailchimp', 'hubspot',
                     'canva', 'adobe suite', 'seo tools'],
            'soft': ['creativity', 'communication', 'analytical thinking', 'storytelling',
                    'strategic thinking', 'leadership']
        },
        'HR': {
            'core': ['recruitment', 'employee relations', 'payroll', 'training',
                    'performance management', 'compliance', 'compensation'],
            'tools': ['workday', 'peoplesoft', 'ats', 'hr information system',
                     'excel', 'hrms'],
            'soft': ['communication', 'interpersonal skills', 'conflict resolution',
                    'leadership', 'organization', 'problem solving']
        }
    }
    
    @staticmethod
    def extract_skills(text: str) -> Dict[str, List[str]]:
        """
        Extract technical and soft skills from resume text
        
        Args:
            text: Resume text content
            
        Returns:
            Dictionary with technical and soft skills found
        """
        text_lower = text.lower()
        
        technical_found = set()
        soft_found = set()
        
        # Find technical skills
        for skill in SkillExtractor.TECHNICAL_SKILLS:
            if re.search(r'\b' + re.escape(skill) + r'\b', text_lower):
                technical_found.add(skill)
        
        # Find soft skills
        for skill in SkillExtractor.SOFT_SKILLS:
            if re.search(r'\b' + re.escape(skill) + r'\b', text_lower):
                soft_found.add(skill)
        
        return {
            'technical': sorted(list(technical_found)),
            'soft': sorted(list(soft_found))
        }
    
    @staticmethod
    def get_role_profile(role: str) -> Dict[str, List[str]]:
        """
        Get skill profile for a specific role
        
        Args:
            role: Role name (e.g., 'ACCOUNTANT')
            
        Returns:
            Dictionary with core, tool, and soft skills for the role
        """
        role_upper = role.upper().replace('-', ' ')
        
        # Try to find exact match or partial match
        for key, profile in SkillExtractor.ROLE_SKILL_PROFILES.items():
            if key in role_upper or role_upper in key:
                return profile
        
        # Default profile if not found
        return {
            'core': [],
            'tools': [],
            'soft': ['communication', 'problem solving', 'teamwork']
        }
    
    @staticmethod
    def analyze_skills(resume_skills: Dict[str, List[str]], 
                      role: str) -> Dict[str, any]:
        """
        Analyze resume skills against role requirements
        
        Args:
            resume_skills: Skills extracted from resume
            role: Target role
            
        Returns:
            Dictionary with strengths, weaknesses, and overlap analysis
        """
        role_profile = SkillExtractor.get_role_profile(role)
        
        resume_all = set(resume_skills['technical'] + resume_skills['soft'])
        role_all = set(role_profile.get('core', []) + 
                      role_profile.get('tools', []) + 
                      role_profile.get('soft', []))
        
        strengths = list(resume_all.intersection(role_all))
        weaknesses = list(role_all - resume_all)
        
        overlap_percentage = (len(strengths) / len(role_all) * 100) if role_all else 0
        
        return {
            'strengths': strengths,
            'weaknesses': weaknesses,
            'skill_overlap_percentage': overlap_percentage,
            'resume_skills': resume_skills,
            'role_profile': role_profile
        }
