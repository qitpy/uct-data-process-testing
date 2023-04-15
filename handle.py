from src.prepare.process_job import load_input, load_output
from src.prepare.converting_json_data_to_files import converting_json_data_to_files
from src.prepare.model import Job

def handle(input_job_text: str) -> Job:
    # print(input_job_text)
    converted_job = Job()

    # ---- TODO: convert input_job_text to Job object ----
    # ---- Your code ------------------------------------








    # ---------------------------------------------------

    converted_job.requirement = ""
    converted_job.responsibilities = ""
    converted_job.about = ""
    converted_job.benefit = ""
    converted_job.compensation = ""

    return converted_job

if __name__ == "__main__":
    job_texts = load_input()
    load_output(map(handle, job_texts))