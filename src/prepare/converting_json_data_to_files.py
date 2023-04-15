# TODO: get all **html2text** to every file in /input

# load Json data from data_source.json and convert it to a list of Job objects to /output
import json
from src.prepare.model import Job

def converting_json_data_to_files():
    with open('./data_source.json', 'r') as f:
        data = json.load(f)

    for job in data:
        job_id = job['_id']['$oid']
        with open(f'./input/{job_id}.txt', 'w') as f:
            f.write(job['html2text'])
