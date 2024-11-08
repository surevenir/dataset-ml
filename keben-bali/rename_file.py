import os
import subprocess

# Define the current directory and target extensions
current_extension = '.jpg', '.jpeg', '.png'  # Ganti dengan ekstensi file saat ini
new_extension = '.png'      # Ekstensi yang diinginkan

# Initialize a counter for numbering
counter = 1

# Get the current directory (assuming you open CMD in this directory)
directory = os.getcwd()

# Iterate over files in the current directory
for filename in os.listdir(directory):
    # Check if the file has the specified current extension
    if filename.endswith(current_extension):
        # Define the old file path
        old_file = os.path.join(directory, filename)
        
        # Create the new filename with sequential numbering
        new_filename = f"keben_bali{counter}{new_extension}"
        new_file = os.path.join(directory, new_filename)
        
        # PowerShell command to rename the file
        command = f'Rename-Item -Path "{old_file}" -NewName "{new_filename}"'
        
        # Run PowerShell command
        subprocess.run(["powershell", "-Command", command], shell=True)
        
        # Increment the counter
        counter += 1

print("Semua file dengan ekstensi yang ditentukan telah diubah namanya secara berurutan.")
