import os
import subprocess

# Path to the directory containing the .tar files
tar_files_path = 'directory_for_tar_files'

# Docker repository
repository = 'docker_repo'

# Get the list of .tar files in the directory
tar_files = [f for f in os.listdir(tar_files_path) if f.endswith('.tar')]

for tar_file in tar_files:
    tar_file_path = os.path.join(tar_files_path, tar_file)
    image_name = os.path.splitext(tar_file)[0]
    
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

print("All images have been pushed to the repository and deleted locally.")
