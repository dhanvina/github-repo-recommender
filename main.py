import os
import sys

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__)))

import streamlit as st
from src.github_recommender.recommender import GithubRepoRecommender
from src.github_recommender.models import SearchResponse
from dotenv import load_dotenv
import time
from loguru import logger

# Load environment variables
load_dotenv()

# Configure logger
logger.add("app.log", rotation="500 MB")

# Page configuration
st.set_page_config(
    page_title="GitHub Repo Recommender",
    page_icon="🔍",
    layout="wide"
)

@st.cache_resource(show_spinner=True)
def initialize_recommender() -> GithubRepoRecommender:
    """Initialize and cache the recommender instance."""
    try:
        # Try to get token from Streamlit secrets first (for production)
        token = None
        if hasattr(st, 'secrets') and 'github_token' in st.secrets:
            token = st.secrets.github_token
        # Fallback to environment variable (for local development)
        if not token:
            token = os.getenv('GITHUB_TOKEN')
            
        return GithubRepoRecommender(github_token=token)
    except Exception as e:
        st.error(f"Error initializing recommender: {str(e)}")
        logger.error(f"Recommender initialization failed: {str(e)}")
        return None

def render_repository_card(repo):
    """Render a single repository card in the UI."""
    with st.container():
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"### [{repo.name}]({repo.url})")
            st.markdown(f"_{repo.description}_" if repo.description else "_No description available_")
            if repo.language:
                st.markdown(f"**Language:** {repo.language}")
        with col2:
            st.metric("Stars", f"⭐ {repo.stars:,}")
            st.metric("Relevance", f"{repo.relevance_score:.2%}")
        st.divider()

def main():
    # Title and description
    st.title("🔍 GitHub Repository Recommender")
    st.markdown("""
    Find the most relevant GitHub repositories for any topic using AI-powered semantic search.
    This tool uses transformer models to understand the context and meaning of your search.
    """)
    
    # Optional GitHub token input
    with st.expander("⚙️ Settings"):
        github_token = st.text_input(
            "GitHub Token (optional):", 
            type="password",
            help="Enter your GitHub token to increase API rate limits. Create one at https://github.com/settings/tokens"
        )
    
    # Initialize recommender
    recommender = initialize_recommender()
    
    if recommender is None:
        st.error("Failed to initialize the recommender. Please refresh the page.")
        return
    
    # Input section
    st.subheader("Enter Your Search")
    col1, col2 = st.columns([3, 1])
    with col1:
        topic = st.text_input(
            "Topic or keywords:", 
            placeholder="e.g., machine learning, web development, data visualization",
            help="Enter keywords or a description of what you're looking for"
        )
    with col2:
        limit = st.number_input(
            "Number of results:", 
            min_value=1, 
            max_value=20, 
            value=10,
            help="Maximum number of repositories to display"
        )
    
    # Search button
    if st.button("🔎 Search Repositories", type="primary"):
        if topic:
            try:
                with st.spinner("Searching for repositories..."):
                    result: SearchResponse = recommender.search(topic, limit)
                
                if result and result.repositories:
                    st.subheader(f"📚 Found {result.total_count} Repositories")
                    st.markdown(f"_Search completed in {result.search_time:.2f} seconds_")
                    
                    for repo in result.repositories:
                        render_repository_card(repo)
                else:
                    st.info("No repositories found for your search query.")
            except Exception as e:
                logger.error(f"Search failed: {str(e)}")
                st.error(f"An error occurred during the search. Please try again later.")
        else:
            st.warning("Please enter a topic to search for repositories.")

if __name__ == "__main__":
    main()