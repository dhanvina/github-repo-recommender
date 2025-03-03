from setuptools import setup, find_packages

setup(
    name="github-repo-recommender",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    dependency_links=[
        "https://download.pytorch.org/whl/cpu"
    ],
    install_requires=[
        "streamlit==1.32.0",
        "sentence-transformers==2.2.2",
        "PyGithub==2.1.1",
        "python-dotenv==1.0.0",
        "pydantic==2.5.2",
        "loguru==0.7.2",
        "torch==2.2.1+cpu",
        "torchvision==0.17.1+cpu",
        "transformers==4.37.2",
        "tokenizers>=0.15.0",
        "numpy>=1.24.3",
        "scikit-learn>=1.3.2",
        "huggingface-hub>=0.20.3",
        "tqdm>=4.66.1",
        "typing-extensions>=4.9.0",
        "filelock>=3.13.1"
    ]
)