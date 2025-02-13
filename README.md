# GitHub Repository Recommender

An AI-powered GitHub repository recommender that uses semantic search to find the most relevant repositories based on your topic of interest. This project uses open-source models and is completely free to use.

## Features

- Semantic search using Sentence Transformers (all-MiniLM-L6-v2)
- GitHub API integration for repository search
- FastAPI backend for quick and efficient API responses
- Relevance scoring based on topic similarity

## Requirements

- Python 3.8+
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

1. Start the server:
```bash
python main.py
```

2. The API will be available at `http://localhost:8000`

3. Access the API documentation at `http://localhost:8000/docs`

4. Make a GET request to `/search/{topic}` to find relevant repositories:
```
http://localhost:8000/search/machine-learning
```

Optional query parameter:
- `limit`: Number of repositories to return (default: 10)

## API Response Example

```json
{
  "repositories": [
    {
      "name": "username/repo",
      "description": "Repository description",
      "stars": 1000,
      "url": "https://github.com/username/repo",
      "relevance_score": 0.85
    }
  ]
}
```

## Technology Stack

- FastAPI - Web framework
- Sentence Transformers - Semantic search
- PyGithub - GitHub API integration
- Python-dotenv - Environment configuration

## License

MIT License - See LICENSE file for details