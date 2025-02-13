#!/bin/bash

# Update pip first
python -m pip install --upgrade pip

# Install PyTorch CPU version first
python -m pip install torch==2.2.0+cpu torchvision==0.17.0+cpu --extra-index-url https://download.pytorch.org/whl/cpu

# Install other dependencies
python -m pip install -r requirements-deploy.txt