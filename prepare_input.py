import os
import shutil
import json
import sys

def prepare_input(collection_path):
    input_dir = os.path.abspath("input")
    if os.path.exists(input_dir):
        shutil.rmtree(input_dir)
    os.makedirs(input_dir)

    with open(os.path.join(collection_path, "challenge1b_input.json"), "r") as f:
        data = json.load(f)

    persona = data["persona"]["role"]
    task = data["job_to_be_done"]["task"]

    with open(os.path.join(input_dir, "persona_job.txt"), "w") as f:
        f.write(persona.strip() + "\n")
        f.write(task.strip())

    pdf_dir = os.path.join(collection_path, "PDFs")
    for file in os.listdir(pdf_dir):
        if file.endswith(".pdf"):
            shutil.copy(os.path.join(pdf_dir, file), input_dir)

    print(f"✅ Prepared input for {persona} → {task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python prepare_input.py <Collection Folder Path>")
        sys.exit(1)

    prepare_input(sys.argv[1])
