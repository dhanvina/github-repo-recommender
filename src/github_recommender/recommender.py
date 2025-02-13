from typing import List, Optional
from datetime import datetime
import time
from loguru import logger
from .models import RepositoryInfo, SearchResponse
from .services.embedding_service import EmbeddingService, SentenceTransformerService
from .services.repository_service import RepositoryService, GitHubService

class GithubRepoRecommender:
    """Main class for repository recommendations."""
    
    def __init__(
        self,
        embedding_service: Optional[EmbeddingService] = None,
        repository_service: Optional[RepositoryService] = None,
        github_token: Optional[str] = None
    ):
        self.embedding_service = embedding_service or SentenceTransformerService()
        self.repository_service = repository_service or GitHubService(token=github_token)
    
    def _calculate_relevance_scores(
        self,
        topic: str,
        repositories: List[RepositoryInfo]
    ) -> List[RepositoryInfo]:
        """Calculate relevance scores for repositories based on topic similarity."""
        if not repositories:
            return []
            
        topic_embedding = self.embedding_service.encode([topic])
        
        for repo in repositories:
            description = repo.description or ""
            desc_embedding = self.embedding_service.encode([description])
            repo.relevance_score = self.embedding_service.compute_similarity(
                topic_embedding,
                desc_embedding
            )
        
        return sorted(repositories, key=lambda x: x.relevance_score, reverse=True)
    
    def search(self, topic: str, limit: int = 10) -> SearchResponse:
        """
        Search for repositories and rank them by relevance.
        
        Args:
            topic: Search query or topic
            limit: Maximum number of results to return
            
        Returns:
            SearchResponse object containing ranked repositories
        """
        try:
            start_time = time.time()
            
            # Search for repositories
            repositories = self.repository_service.search_repositories(
                query=topic,
                limit=limit
            )
            
            # Calculate relevance scores and sort
            ranked_repos = self._calculate_relevance_scores(topic, repositories)
            
            # Prepare response
            search_time = time.time() - start_time
            return SearchResponse(
                repositories=ranked_repos[:limit],
                total_count=len(ranked_repos),
                search_time=search_time,
                query=topic
            )
            
        except Exception as e:
            logger.error(f"Error in repository search: {str(e)}")
            raise