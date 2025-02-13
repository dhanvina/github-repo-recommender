"""
GitHub Repository Recommender Package
A semantic search-based GitHub repository recommendation system.
"""

from .recommender import GithubRepoRecommender
from .models import RepositoryInfo, SearchResponse

__version__ = "1.0.0"
__all__ = ["GithubRepoRecommender", "RepositoryInfo", "SearchResponse"]