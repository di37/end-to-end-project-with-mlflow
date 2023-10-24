import os
from pathlib import Path
import logging

# Set up logging to print to console and write to file
logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
file_handler = logging.FileHandler('project_setup.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s]: %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)


dirs = [
    os.path.join(".github", "workflows"),
    os.path.join("artifacts", "data_ingestion"),
    os.path.join("artifacts", "data_transformation"),
    os.path.join("artifacts", "data_validation"),
    os.path.join("artifacts", "model_evaluation"),
    os.path.join("artifacts", "model_trainer"),
    "docker",
    "config",
    "research",
    "wine_quality",
    "utils"
]

absolute_imports = "import os, sys\nfrom os.path import dirname as up\n\nsys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))\n"

files = [
    (".dockerignore", "databox\n**/*__pycache__\ndocker\n"),
    (".gitignore", "databox\n**/*__pycache__\n"),
    ("main_fastapi.py", absolute_imports),
    ("main.py", absolute_imports),
    ("README.md", ""),
    ("requirements.txt", ""),
    ("params.yaml", ""),
    ("schema.yaml", ""),
    (os.path.join("config", "config.yaml"), ""),
    (os.path.join(".github", "workflows", "main.yaml"), ""),
    (os.path.join("research", "01_data_ingestion.ipynb"), ""),
    (os.path.join("research", "02_data_validation.ipynb"), ""),
    (os.path.join("research", "03_data_transformation.ipynb"), ""),
    (os.path.join("research", "04_model_trainer.ipynb"), ""),
    (os.path.join("research", "05_model_evaluation.ipynb"), ""),
    (os.path.join("research", "trails.ipynb"), ""),
    (os.path.join("utils", "__init__.py"), "from utils.constants import *\nfrom utils.helper import *\n"),
    (os.path.join("utils", "constants.py"), absolute_imports),
    (os.path.join("utils", "helper.py"), absolute_imports),
    (os.path.join("wine_quality", "__init__.py"), "from wine_quality.helper import *\nfrom wine_quality.models import *\n"),
    (os.path.join("wine_quality", "helper.py"), absolute_imports),
    (os.path.join("wine_quality", "models.py"), absolute_imports),
    (os.path.join("docker", "docker_run.sh"), ""),
    (os.path.join("docker", "Dockerfile"), ""),
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass
    logger.info(f"Created directory: {dir_}")

for file_, content in files:
    dir_ = os.path.dirname(file_)
    if dir_ != "": os.makedirs(dir_, exist_ok=True)
    with open(file_, "w") as f:
        f.write(content)
    logger.info(f"Created file: {file_}")