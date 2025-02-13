from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class RepositoryInfo(BaseModel):
    """Data model for repository information."""
    name: str
    description: Optional[str] = None
    stars: int = Field(ge=0)
    url: str
    relevance_score: float = Field(ge=0.0, le=1.0)
    created_at: Optional[datetime] = None
    language: Optional[str] = None

class SearchResponse(BaseModel):
    """Data model for search response."""
    repositories: List[RepositoryInfo]
    total_count: int
    search_time: float
    query: str