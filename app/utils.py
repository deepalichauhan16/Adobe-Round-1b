def load_persona_job(input_dir):
    with open(f"{input_dir}/persona_job.txt", "r") as f:
        lines = f.readlines()
        persona = lines[0].strip()
        job = lines[1].strip()
        return persona, job
