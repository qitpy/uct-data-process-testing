from src.prepare.model import Job
import os
import glob


# TODO: loop for every file in /input and read to a variable
def load_input():
    job_texts = []
    for file in glob.glob('./input/*.txt'):
        with open(file, 'r') as f:
            job_texts.append(f.read())

        # with open(file, 'r') as f:
        #     job_texts.append(f.read())
    return job_texts


def load_output(jobs: list[Job]):
    for job in jobs:
        job_id = job['_id']['$oid']
        with open(f'./output/{job_id}.json', 'w') as f:
            f.write(job.json())
