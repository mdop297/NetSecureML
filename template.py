import os
from pathlib import Path
import logging

project_name="NetSecureML"

list_of_files=[
    ".github/workflows/.gitkeep",
    ".github/workflows/main.yaml",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/common.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configurations.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/logging/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception.py",
    f"{project_name}/cloud/__init__.py",
    "notebooks/notebook.ipynb",
    "config/config.yaml",
    "params.yaml",
    "schema.py",
    "main.py",
    "README.md",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "templates/index.html",
    ".gitignore",
    ".env",
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else: 
        logging.info(f"{filename} is already exists.")
