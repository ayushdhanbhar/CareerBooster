"""
BERT Embedding and Semantic Similarity Module
Uses transformer-based BERT model for embedding generation and comparison
"""

import numpy as np
from typing import List, Tuple, Dict
import logging
from sentence_transformers import SentenceTransformer
import torch

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BertEmbedder:
    """Generate embeddings and compute semantic similarity using BERT"""
    
    # Using sentence-transformers distilbert model for efficiency
    DEFAULT_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
    
    def __init__(self, model_name: str = DEFAULT_MODEL):
        """
        Initialize BERT embedder with pretrained model
        
        Args:
            model_name: Name of the pretrained model to use
        """
        try:
            logger.info(f"Loading BERT model: {model_name}")
            self.model = SentenceTransformer(model_name)
            self.model_name = model_name
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise
    
    def get_embedding(self, text: str) -> np.ndarray:
        """
        Generate embedding for a single text
        
        Args:
            text: Input text to embed
            
        Returns:
            Embedding vector as numpy array
        """
        try:
            # Clean and validate input
            if not text or not isinstance(text, str):
                logger.warning("Invalid text input")
                return np.zeros(384)  # Default dimension for all-MiniLM-L6-v2
            
            text_clean = text.strip()[:512]  # Truncate to reasonable length
            
            embedding = self.model.encode(text_clean, convert_to_numpy=True)
            return embedding
            
        except Exception as e:
            logger.error(f"Error generating embedding: {str(e)}")
            return np.zeros(384)
    
    def get_embeddings_batch(self, texts: List[str]) -> np.ndarray:
        """
        Generate embeddings for multiple texts
        
        Args:
            texts: List of texts to embed
            
        Returns:
            Array of embedding vectors
        """
        try:
            # Clean texts
            clean_texts = [t.strip()[:512] if t else "" for t in texts]
            
            embeddings = self.model.encode(clean_texts, convert_to_numpy=True)
            return embeddings
            
        except Exception as e:
            logger.error(f"Error generating batch embeddings: {str(e)}")
            return np.zeros((len(texts), 384))
    
    @staticmethod
    def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
        """
        Calculate cosine similarity between two vectors
        
        Args:
            vec1: First vector
            vec2: Second vector
            
        Returns:
            Similarity score between 0 and 1
        """
        if vec1.size == 0 or vec2.size == 0:
            return 0.0
        
        try:
            dot_product = np.dot(vec1, vec2)
            norm1 = np.linalg.norm(vec1)
            norm2 = np.linalg.norm(vec2)
            
            if norm1 == 0 or norm2 == 0:
                return 0.0
            
            similarity = dot_product / (norm1 * norm2)
            # Ensure value is between 0 and 1
            return max(0.0, min(1.0, float(similarity)))
            
        except Exception as e:
            logger.error(f"Error computing cosine similarity: {str(e)}")
            return 0.0
    
    @staticmethod
    def euclidean_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
        """
        Calculate Euclidean distance and convert to similarity (0-1 scale)
        
        Args:
            vec1: First vector
            vec2: Second vector
            
        Returns:
            Similarity score between 0 and 1
        """
        try:
            distance = np.linalg.norm(vec1 - vec2)
            # Convert distance to similarity (normalized)
            similarity = 1 / (1 + distance)
            return float(similarity)
            
        except Exception as e:
            logger.error(f"Error computing euclidean similarity: {str(e)}")
            return 0.0
    
    def compare_documents(self, text1: str, text2: str, 
                         method: str = 'cosine') -> Dict[str, float]:
        """
        Compare two documents and compute multiple similarity metrics
        
        Args:
            text1: First document text
            text2: Second document text
            method: Similarity method ('cosine' or 'euclidean')
            
        Returns:
            Dictionary with similarity scores
        """
        embedding1 = self.get_embedding(text1)
        embedding2 = self.get_embedding(text2)
        
        if method == 'cosine':
            similarity = self.cosine_similarity(embedding1, embedding2)
        else:
            similarity = self.euclidean_similarity(embedding1, embedding2)
        
        return {
            'similarity_score': similarity,
            'embedding1_dim': len(embedding1),
            'embedding2_dim': len(embedding2),
            'method': method
        }
    
    def get_chunk_embeddings(self, text: str, chunk_size: int = 200) -> Tuple[List[str], np.ndarray]:
        """
        Split text into chunks and generate embeddings for each
        This helps capture different aspects of the resume
        
        Args:
            text: Input text
            chunk_size: Number of words per chunk
            
        Returns:
            Tuple of (chunks list, embeddings array)
        """
        words = text.split()
        chunks = []
        
        for i in range(0, len(words), chunk_size):
            chunk = ' '.join(words[i:i + chunk_size])
            chunks.append(chunk)
        
        embeddings = self.get_embeddings_batch(chunks)
        return chunks, embeddings
    
    def get_sectional_similarity(self, resume_text: str, role_profile_text: str) -> Dict[str, float]:
        """
        Calculate similarity using multiple chunks for more detailed comparison
        
        Args:
            resume_text: Resume content
            role_profile_text: Role profile description
            
        Returns:
            Dictionary with detailed similarity metrics
        """
        _, resume_embeddings = self.get_chunk_embeddings(resume_text)
        _, profile_embeddings = self.get_chunk_embeddings(role_profile_text)
        
        # Calculate average similarity across all chunk pairs
        similarities = []
        
        for resume_emb in resume_embeddings:
            max_similarity = 0
            for profile_emb in profile_embeddings:
                sim = self.cosine_similarity(resume_emb, profile_emb)
                max_similarity = max(max_similarity, sim)
            similarities.append(max_similarity)
        
        avg_similarity = np.mean(similarities) if similarities else 0.0
        max_match = np.max(similarities) if similarities else 0.0
        min_match = np.min(similarities) if similarities else 0.0
        
        return {
            'average_similarity': float(avg_similarity),
            'max_match': float(max_match),
            'min_match': float(min_match),
            'num_chunks': len(similarities)
        }
