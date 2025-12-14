from huggingface_hub.utils import RepositoryNotFoundError, HfHubHTTPError
from huggingface_hub import HfApi, create_repo
import os

from huggingface_hub import HfApi, create_repo
from huggingface_hub.utils import RepositoryNotFoundError, HfHubHTTPError

repo_id = "haseena84/Wellness-Tourism-Package-Customer-Prediction"
repo_type = "dataset"

# Initialize API client
api = HfApi(token=os.getenv("HF_TOKEN"))
# Step 1: Check if dataset repository exists
try:
    api.repo_info(repo_id=repo_id, repo_type=repo_type)
    print(f"Dataset repository '{repo_id}' already exists. Using it.")
except RepositoryNotFoundError:
    print(f"Dataset repo '{repo_id}' not found. Creating a new one...")
    create_repo(
        repo_id=repo_id,
        repo_type=repo_type,
        private=False
    )
    print(f"Dataset repo '{repo_id}' created successfully.")

 # Step 2: Upload folder to HF Dataset Space
api.upload_folder(
    folder_path="wellness_tourism_package_customer_prediction/data",
    repo_id=repo_id,
    repo_type=repo_type,
)
