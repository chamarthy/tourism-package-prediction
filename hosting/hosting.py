from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
repo_id = "schamart/tourism-project-space"

try:
    # Corrected local path: the runner is already in the repo root
    api.upload_folder(
        folder_path="deployment",
        repo_id=repo_id,
        repo_type="space",
        path_in_repo=""
    )
    print(f"Successfully uploaded to {repo_id}")
except Exception as e:
    print(f"Error during upload: {e}")
    raise e
