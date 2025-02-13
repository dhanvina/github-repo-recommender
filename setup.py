from setuptools import setup, find_packages

setup(
    name="github-repo-recommender",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9,<3.10",
    install_requires=[
        "streamlit==1.32.0",
        "sentence-transformers==2.2.2",
        "PyGithub==2.1.1",
        "python-dotenv==1.0.0",
        "pydantic==2.5.2",
        "loguru==0.7.2",
        "huggingface-hub==0.12.1",
        "transformers==4.26.1",
        "torch==2.2.1",
        "torchvision==0.17.1",
        "numpy>=1.20.0,<2.0.0",
        "scikit-learn==1.2.2",
        "tqdm>=4.65.0",
        "typing-extensions>=4.5.0",
        "filelock>=3.12.0"
    ]
)