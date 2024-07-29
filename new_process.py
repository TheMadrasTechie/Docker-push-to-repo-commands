import os
import subprocess

# Path to the directory containing the .tar files
tar_files_path = 'D:\\python\\upwork\\AWS reognize with docker\\Docker_images'

# Docker repository
repository = 'themadrastechie/face_recognition'

# Get the list of .tar files in the directory
tar_files = [f for f in os.listdir(tar_files_path) if f.endswith('.tar')]

for tar_file in tar_files:
    tar_file_path = os.path.join(tar_files_path, tar_file)
    image_name = os.path.splitext(tar_file)[0]

    # Load the Docker image from the tar file and capture the output
    print(f"Loading image from {tar_file_path}...")
    result = subprocess.run(['docker', 'load', '-i', tar_file_path], check=True, capture_output=True, text=True)
    output = result.stdout
    print(output)
    
    # Extract the image ID from the output
    loaded_image_name = ""
    for line in output.split('\n'):
        if "Loaded image ID" in line or "Loaded image:" in line:
            loaded_image_name = line.split()[-1]
            break

    if loaded_image_name:
        # Tag the Docker image
        print(f"Tagging image {loaded_image_name} as {repository}:{image_name}...")
        subprocess.run(['docker', 'tag', loaded_image_name, f'{repository}:{image_name}'], check=True)
        
        # Push the Docker image to the repository
        print(f"Pushing image {repository}:{image_name} to repository...")
        subprocess.run(['docker', 'push', f'{repository}:{image_name}'], check=True)
        
        # Delete the Docker image to save memory
        print(f"Deleting local image {loaded_image_name}...")
        subprocess.run(['docker', 'rmi', loaded_image_name], check=True)
        
        # Optionally, remove the repository-tagged image as well to free up more space
        print(f"Deleting local image {repository}:{image_name}...")
        subprocess.run(['docker', 'rmi', f'{repository}:{image_name}'], check=True)
    else:
        print(f"Failed to load image from {tar_file_path}")

print("All images have been pushed to the repository and deleted locally.")
