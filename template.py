import os
import logging
logging.basicConfig(level=logging.INFO)

folders=[
    os.path.join("Data","raw"),
    os.path.join("Data","procrss"),
    os.path.join('src',"components"),
    os.path.join('src',"pipelines"),
    "Notebook",
    "models",
    "reports"

    
]

for fol in folders:
    if(not os.path.exists(fol)):
        os.makedirs(fol)
        # Make a git keep file
        git_keep=os.path.join(fol,".gitkeep")
        with open(git_keep,"w") as f:
            pass

# Make a necessary files
files=[
    os.path.join("src","__init__.py"),
    os.path.join("src","utils.py"),

    os.path.join(f"src/components","__init__.py"),
    os.path.join(f"src/components","data_ingestion.py"),
    os.path.join(f"src/components","data_transformation.py"),
    os.path.join(f"src/components","model_training.py"),


    os.path.join(f"src/pipelines","prediction_pipeline.py"),

    "setup.py",
    "test_environment.py",
    "Dockerfile",
    ".dockerignore",
    ".env",
    "requirements.txt"
]

for file in files:
    if (not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open(file,'w') as f:
            pass
    else:
        logging.info(f"File {file} already exists")
