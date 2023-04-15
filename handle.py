from src.prepare.process_job import load_input, load_output
from src.prepare.converting_json_data_to_files import converting_json_data_to_files
from src.prepare.model import Job

def handle(job_input: str) -> Job:
    # print(job_input)
    converted_job = Job()

    # ---- TODO: convert input_job_text to Job object ----
    # ---- Your code ------------------------------------








    converted_job.requirement = ""
    converted_job.responsibilities = ""
    converted_job.about = ""
    converted_job.benefit = ""
    converted_job.compensation = ""
    # ---------------------------------------------------

    return converted_job

if __name__ == "__main__":

    # load job data from /input folder
    job_text_by_file_names = load_input()

    # convert job data to Job object and save to /output folder
    for item in job_text_by_file_names:
        job = handle(item["text"])
        load_output(job, item["name"])