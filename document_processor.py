"""
PDF and Document Text Extraction Module
Handles extraction of text from various resume formats
"""

import pdfplumber
from typing import Optional, Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DocumentProcessor:
    """Process PDF documents and extract text content"""
    
    @staticmethod
    def extract_text_from_pdf(file_path: str) -> str:
        """
        Extract text from PDF file using pdfplumber
        
        Args:
            file_path: Path to the PDF file
            
        Returns:
            Extracted text content
        """
        try:
            text = ""
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            
            if not text.strip():
                logger.warning(f"No text extracted from {file_path}")
                return ""
            
            logger.info(f"Successfully extracted text from {file_path}")
            return text
            
        except Exception as e:
            logger.error(f"Error extracting PDF from {file_path}: {str(e)}")
            return ""
    
    @staticmethod
    def extract_text_from_bytes(file_bytes: bytes) -> str:
        """
        Extract text from PDF bytes
        
        Args:
            file_bytes: PDF file in bytes format
            
        Returns:
            Extracted text content
        """
        try:
            import io
            text = ""
            with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            
            return text
            
        except Exception as e:
            logger.error(f"Error extracting PDF from bytes: {str(e)}")
            return ""
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean and normalize extracted text
        
        Args:
            text: Raw extracted text
            
        Returns:
            Cleaned text
        """
        # Remove extra whitespace
        text = " ".join(text.split())
        # Convert to lowercase for processing
        text = text.lower()
        return text
