from abc import ABC, abstractmethod
from sentence_transformers import SentenceTransformer, util
import numpy as np
from typing import List

class EmbeddingService(ABC):
    """Abstract base class for text embedding services."""
    
    @abstractmethod
    def encode(self, texts: List[str]) -> np.ndarray:
        """Encode texts into embeddings."""
        pass
    
    @abstractmethod
    def compute_similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        """Compute similarity between two embeddings."""
        pass

class SentenceTransformerService(EmbeddingService):
    """Concrete implementation of embedding service using SentenceTransformers."""
    
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
    
    def encode(self, texts: List[str]) -> np.ndarray:
        return self.model.encode(texts)
    
    def compute_similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        return float(util.cos_sim(embedding1, embedding2)[0][0])