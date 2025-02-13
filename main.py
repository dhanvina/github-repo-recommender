import streamlit as st
from sentence_transformers import SentenceTransformer
from github import Github
import os
from dotenv import load_dotenv

# Page configuration
st.set_page_config(
    page_title="GitHub Repo Recommender",
    page_icon="🔍",
    layout="wide"
)

# Initialize the sentence transformer model
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

# Initialize GitHub client
@st.cache_resource
def init_github():
    return Github()

def search_repos(topic: str, limit: int = 10):
    try:
        model = load_model()
        g = init_github()
        
        # Search for repositories
        repos = g.search_repositories(query=topic, sort="stars")
        
        # Get top repositories
        top_repos = []
        topic_embedding = model.encode([topic])
        
        # Show progress bar
        progress_text = "Analyzing repositories..."
        progress_bar = st.progress(0)
        
        # Collect repo information and calculate relevance
        total_repos = min(30, limit * 2)
        for idx, repo in enumerate(repos[:total_repos]):
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
            
            # Update progress bar
            progress = (idx + 1) / total_repos
            progress_bar.progress(progress)
        
        # Sort by relevance and return top results
        top_repos.sort(key=lambda x: x["relevance_score"], reverse=True)
        return top_repos[:limit]
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return []

def main():
    # Title and description
    st.title("🔍 GitHub Repository Recommender")
    st.markdown("""
    Find the most relevant GitHub repositories for any topic using AI-powered semantic search.
    This tool uses transformer models to understand the context and meaning of your search.
    """)
    
    # Input section
    st.subheader("Enter Your Search")
    col1, col2 = st.columns([3, 1])
    with col1:
        topic = st.text_input("Topic or keywords:", placeholder="e.g., machine learning, web development, data visualization")
    with col2:
        limit = st.number_input("Number of results:", min_value=1, max_value=20, value=10)
    
    # Search button
    if st.button("🔎 Search Repositories"):
        if topic:
            with st.spinner("Searching for repositories..."):
                results = search_repos(topic, limit)
                
            if results:
                st.subheader("📚 Found Repositories")
                for idx, repo in enumerate(results, 1):
                    with st.container():
                        col1, col2 = st.columns([4, 1])
                        with col1:
                            st.markdown(f"### [{repo['name']}]({repo['url']})")
                            st.markdown(f"_{repo['description']}_" if repo['description'] else "_No description available_")
                        with col2:
                            st.metric("Stars", f"⭐ {repo['stars']:,}")
                            st.metric("Relevance", f"{repo['relevance_score']:.2%}")
                        st.divider()
        else:
            st.warning("Please enter a topic to search for repositories.")

if __name__ == "__main__":
    main()