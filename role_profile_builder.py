"""
Role Profile Builder Module
Builds skill and content profiles from sample resumes in each category
"""

import os
from typing import Dict, List, Set
import logging
from document_processor import DocumentProcessor
from skill_extractor import SkillExtractor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RoleProfileBuilder:
    """Build role profiles from sample resume dataset"""
    
    def __init__(self, data_dir: str):
        """
        Initialize role profile builder
        
        Args:
            data_dir: Path to the data directory containing role subdirectories
        """
        self.data_dir = data_dir
        self.role_profiles = {}
        self.roles_available = self._get_available_roles()
    
    def _get_available_roles(self) -> Dict[str, str]:
        """
        Discover all available roles from data directory
        
        Returns:
            Dictionary mapping role names to role directory paths
        """
        roles = {}
        
        try:
            if not os.path.exists(self.data_dir):
                logger.warning(f"Data directory not found: {self.data_dir}")
                return roles
            
            for item in os.listdir(self.data_dir):
                item_path = os.path.join(self.data_dir, item)
                if os.path.isdir(item_path) and item != '.DS_Store' and not item.startswith('.'):
                    # Clean up role name
                    role_name = item.replace('-', ' ').replace('_', ' ').upper()
                    roles[role_name] = item_path
            
            logger.info(f"Found {len(roles)} available roles")
            return roles
            
        except Exception as e:
            logger.error(f"Error discovering roles: {str(e)}")
            return roles
    
    def get_available_roles(self) -> List[str]:
        """
        Get list of available roles
        
        Returns:
            List of role names
        """
        return sorted(list(self.roles_available.keys()))
    
    def build_role_profile(self, role: str, sample_size: int = 10) -> Dict[str, any]:
        """
        Build a profile for a specific role from sample resumes
        
        Args:
            role: Role name
            sample_size: Number of sample resumes to analyze
            
        Returns:
            Dictionary containing role profile
        """
        role_upper = role.upper().replace('-', ' ')
        
        # Find matching role directory
        role_path = None
        for available_role, path in self.roles_available.items():
            if available_role == role_upper or role_upper in available_role:
                role_path = path
                break
        
        if not role_path:
            logger.warning(f"Role not found: {role}")
            return self._get_default_profile(role)
        
        try:
            # Get sample PDFs from role directory
            pdfs = [f for f in os.listdir(role_path) if f.endswith('.pdf')]
            pdfs = pdfs[:sample_size]  # Limit to sample size
            
            all_skills = {'technical': [], 'soft': []}
            all_text = ""
            sample_count = 0
            
            for pdf_file in pdfs:
                pdf_path = os.path.join(role_path, pdf_file)
                try:
                    # Extract text
                    text = DocumentProcessor.extract_text_from_pdf(pdf_path)
                    if text:
                        all_text += text + " "
                        
                        # Extract skills
                        skills = SkillExtractor.extract_skills(text)
                        all_skills['technical'].extend(skills['technical'])
                        all_skills['soft'].extend(skills['soft'])
                        sample_count += 1
                        
                except Exception as e:
                    logger.warning(f"Error processing {pdf_file}: {str(e)}")
                    continue
            
            # Get most common skills
            from collections import Counter
            tech_counter = Counter(all_skills['technical'])
            soft_counter = Counter(all_skills['soft'])
            
            top_tech_skills = [skill for skill, _ in tech_counter.most_common(15)]
            top_soft_skills = [skill for skill, _ in soft_counter.most_common(10)]
            top_tools = [skill for skill, _ in tech_counter.most_common(10)]
            
            profile = {
                'role': role_upper,
                'sample_count': sample_count,
                'description': f"Profile built from {sample_count} sample resumes",
                'core_skills': top_tech_skills,
                'soft_skills': top_soft_skills,
                'tools': top_tools,
                'combined_text': all_text[:2000],  # Store sample text
                'all_text': all_text  # Full text for comparison
            }
            
            self.role_profiles[role_upper] = profile
            logger.info(f"Built profile for {role_upper} from {sample_count} samples")
            
            return profile
            
        except Exception as e:
            logger.error(f"Error building profile for {role}: {str(e)}")
            return self._get_default_profile(role)
    
    def _get_default_profile(self, role: str) -> Dict[str, any]:
        """
        Get a default profile when actual profile can't be built
        
        Args:
            role: Role name
            
        Returns:
            Default profile dictionary
        """
        role_upper = role.upper().replace('-', ' ')
        return {
            'role': role_upper,
            'sample_count': 0,
            'description': 'Default profile',
            'core_skills': [],
            'soft_skills': ['communication', 'teamwork', 'problem solving'],
            'tools': [],
            'combined_text': f"This is a {role_upper} position",
            'all_text': f"This is a {role_upper} position"
        }
    
    def get_role_profile(self, role: str) -> Dict[str, any]:
        """
        Get cached or build profile for a role
        
        Args:
            role: Role name
            
        Returns:
            Role profile dictionary
        """
        role_upper = role.upper().replace('-', ' ')
        
        if role_upper in self.role_profiles:
            return self.role_profiles[role_upper]
        
        return self.build_role_profile(role)
    
    def get_all_profiles(self) -> Dict[str, Dict[str, any]]:
        """
        Get all built profiles
        
        Returns:
            Dictionary of all role profiles
        """
        return self.role_profiles.copy()
