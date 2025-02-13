from setuptools import setup, find_packages

setup(
    name="github-repo-recommender",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9,<3.10",
    dependency_links=[
        "https://download.pytorch.org/whl/torch_stable.html",
        "https://download.pytorch.org/whl/cpu"
    ],
    install_requires=[
        "streamlit==1.32.0",
        "sentence-transformers==2.2.2",
        "PyGithub==2.1.1",
        "python-dotenv==1.0.0",
        "pydantic==2.5.2",
        "loguru==0.7.2",
        "torch==2.0.1+cpu",
        "torchvision==0.15.2+cpu",
        "transformers==4.30.2",
        "tokenizers>=0.13.3",
        "numpy>=1.21.0,<2.0.0",
        "scikit-learn>=1.0.2,<1.3.0",
        "huggingface-hub>=0.13.2,<0.14.0",
        "tqdm>=4.65.0",
        "typing-extensions>=4.5.0",
        "filelock>=3.12.0"
    ]
)