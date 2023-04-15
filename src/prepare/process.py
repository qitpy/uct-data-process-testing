from handle import handle
from src.prepare.model import Job
import os
import glob


# TODO: loop for every file in /input and read to a variable
def load_input():
    job_texts = []
    for file in glob.glob(os.path.join('./input')):
        with open(file, 'r') as f:
            job_texts.append(f.read())
    return job_texts


def load_output(jobs: list[Job]):
    for job in jobs:
        with open(f'./output/{job.id}.json', 'w') as f:
            f.write(job.json())

def process():
    job_texts = load_input()
    load_output(job_texts)
    return map(handle, job_texts)
