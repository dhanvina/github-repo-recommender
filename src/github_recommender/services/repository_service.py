from abc import ABC, abstractmethod
from github import Github, RateLimitExceededException
from typing import List, Optional
import time
from ..models import RepositoryInfo
from loguru import logger

class RepositoryService(ABC):
    """Abstract base class for repository search services."""
    
    @abstractmethod
    def search_repositories(self, query: str, limit: int) -> List[RepositoryInfo]:
        """Search for repositories based on query."""
        pass

class GitHubService(RepositoryService):
    """GitHub implementation of repository service."""
    
    def __init__(self, token: Optional[str] = None):
        self.client = Github(token if token else None)
    
    def _handle_rate_limit(self) -> bool:
        """Handle GitHub API rate limiting."""
        rate_limit = self.client.get_rate_limit()
        if rate_limit.search.remaining == 0:
            reset_timestamp = rate_limit.search.reset.timestamp()
            current_timestamp = time.time()
            sleep_time = reset_timestamp - current_timestamp
            if sleep_time > 0:
                logger.warning(f"Rate limit exceeded. Waiting {int(sleep_time)} seconds.")
                time.sleep(min(sleep_time, 60))
                return True
        return False
    
    def search_repositories(self, query: str, limit: int) -> List[RepositoryInfo]:
        """Search GitHub repositories."""
        try:
            if self._handle_rate_limit():
                logger.info("Retrying search after rate limit wait...")
            
            repos = self.client.search_repositories(query=query, sort="stars")
            total_count = min(repos.totalCount, 30)
            
            if total_count == 0:
                logger.info("No repositories found for the query.")
                return []
            
            result = []
            for repo in repos[:min(total_count, limit * 2)]:
                try:
                    repo_info = RepositoryInfo(
                        name=repo.full_name,
                        description=repo.description or "",
                        stars=repo.stargazers_count,
                        url=repo.html_url,
                        relevance_score=0.0,  # Will be updated later
                        created_at=repo.created_at,
                        language=repo.language
                    )
                    result.append(repo_info)
                except Exception as e:
                    logger.warning(f"Error processing repository {repo.full_name}: {str(e)}")
                    continue
                    
            return result
            
        except RateLimitExceededException:
            logger.error("GitHub API rate limit exceeded.")
            raise
        except Exception as e:
            logger.error(f"Error searching repositories: {str(e)}")
            raise