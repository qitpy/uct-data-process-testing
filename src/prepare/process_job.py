import json
from src.prepare.model import Job
import os
import glob


# TODO: loop for every file in /input and read to a variable
def load_input():
    job_texts = []
    for file in glob.glob('./input/*.txt'):
        with open(file, 'r') as f:
            job_texts.append({"name": os.path.basename(f.name), "text": f.read()})

    return job_texts


def load_output(job: Job, file_name: str):
    # for job in jobs:
    with open(f'./output/{file_name}', 'w') as f:
        json.dump(job.dict(), f, indent=4)
