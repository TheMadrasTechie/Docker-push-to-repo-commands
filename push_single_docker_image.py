import os
import subprocess

# Path to the directory containing the .tar files
tar_files_path = 'directory_for_tar_files'

# Docker repository
repository = 'docker_repo'

# Image tar file
tar_file = 'iscan_v2.1.0.0.tar'
tar_file_path = os.path.join(tar_files_path, tar_file)
image_name = os.path.splitext(tar_file)[0]

try:
    # Load the Docker image from the tar file
    print(f"Loading image from {tar_file_path}...")
    subprocess.run(['docker', 'load', '-i', tar_file_path], check=True)

    # Tag the Docker image
    print(f"Tagging image {image_name} as {repository}:{image_name}...")
    subprocess.run(['docker', 'tag', image_name, f'{repository}:{image_name}'], check=True)

    # Push the Docker image to the repository
    print(f"Pushing image {repository}:{image_name} to repository...")
    subprocess.run(['docker', 'push', f'{repository}:{image_name}'], check=True)

    # Delete the Docker image to save memory
    print(f"Deleting local image {image_name}...")
    subprocess.run(['docker', 'rmi', image_name], check=True)

    # Optionally, remove the repository-tagged image as well to free up more space
    print(f"Deleting local image {repository}:{image_name}...")
    subprocess.run(['docker', 'rmi', f'{repository}:{image_name}'], check=True)

    print("Image has been pushed to the repository and deleted locally.")

except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
