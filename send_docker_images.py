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
    subprocess.run(['docker', 'load', '-i', tar_file_path], check=True)
    
    # Tag the Docker image
    subprocess.run(['docker', 'tag', image_name, f'{repository}:{image_name}'], check=True)
    
    # Push the Docker image to the repository
    subprocess.run(['docker', 'push', f'{repository}:{image_name}'], check=True)

print("All images have been pushed to the repository.")
