from setuptools import setup, find_packages

setup(
    name="github-repo-recommender",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "streamlit>=1.32.0",
        "sentence-transformers>=2.2.2",
        "PyGithub>=2.1.1",
        "python-dotenv>=1.0.0",
        "pydantic>=2.5.2",
        "loguru>=0.7.2",
        "huggingface-hub>=0.18.0,<0.19.0",
        "torch>=1.6.0",
        "transformers>=4.6.0,<5.0.0",
        "numpy>=1.19.5",
        "scikit-learn>=0.24.1",
        "tqdm>=4.41.0"
    ]
)