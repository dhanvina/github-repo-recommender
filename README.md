# GitHub Repository Recommender

An AI-powered GitHub repository recommender that uses semantic search to find the most relevant repositories based on your topic of interest. This project uses open-source models and is completely free to use.

## Features

- Semantic search using Sentence Transformers (all-MiniLM-L6-v2)
- GitHub API integration for repository search
- Streamlit interface for easy interaction
- Relevance scoring based on topic similarity

## Requirements

- Python 3.9+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/github-repo-recommender.git
cd github-repo-recommender
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run main.py
```

The app will open in your default web browser at `http://localhost:8501`

## Deployment

This app can be deployed for free using [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push your code to GitHub
2. Sign up for [Streamlit Community Cloud](https://streamlit.io/cloud)
3. Create a new app and connect it to your GitHub repository
4. Select main.py as your entry point
5. Click "Deploy"

## Technology Stack

- Streamlit - Web interface
- Sentence Transformers - Semantic search
- PyGithub - GitHub API integration
- Python-dotenv - Environment configuration

## License

MIT License - See LICENSE file for details