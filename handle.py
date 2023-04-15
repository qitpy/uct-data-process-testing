from src.prepare.converting_json_data_to_files import converting_json_data_to_files
from src.prepare.model import Job

def handle(input_job_text: str) -> Job:
    print(input_job_text)

    converted_job = Job()

    converted_job.requirement = ""
    converted_job.responsibilities = ""

    return converted_job

if __name__ == "__main__":
    # process()
    converting_json_data_to_files()
