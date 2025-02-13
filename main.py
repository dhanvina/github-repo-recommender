from fastapi import FastAPI, HTTPException
from sentence_transformers import SentenceTransformer
from github import Github
from typing import List
import os
from dotenv import load_dotenv

app = FastAPI()
# Initialize the sentence transformer model (all-MiniLM-L6-v2 is a lightweight, fast model)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize GitHub client (no token needed for public repo search)
g = Github()

@app.get("/search/{topic}")
async def search_repos(topic: str, limit: int = 10):
    try:
        # Search for repositories
        repos = g.search_repositories(query=topic, sort="stars")
        
        # Get top repositories
        top_repos = []
        topic_embedding = model.encode([topic])
        
        # Collect repo information and calculate relevance
        for repo in repos[:min(30, limit * 2)]:  # Fetch extra to filter by relevance
            description = repo.description or ""
            desc_embedding = model.encode([description])
            
            # Calculate similarity between topic and description
            similarity = float(model.util.cos_sim(topic_embedding, desc_embedding)[0][0])
            
            repo_info = {
                "name": repo.full_name,
                "description": description,
                "stars": repo.stargazers_count,
                "url": repo.html_url,
                "relevance_score": similarity
            }
            top_repos.append(repo_info)
        
        # Sort by relevance and return top results
        top_repos.sort(key=lambda x: x["relevance_score"], reverse=True)
        return {"repositories": top_repos[:limit]}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)