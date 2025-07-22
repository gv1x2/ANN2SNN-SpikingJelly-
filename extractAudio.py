import os
import zipfile
import shutil

# folder containing zip archives
archive_folder = r'C:\woic'
# output folder
output_folder = r'C:\extractedAudio'

# extract .wav
def extract_wav_from_zip(zip_path, destination_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            # Check .wav extension
            if file.lower().endswith('.wav'):
                zip_ref.extract(file, destination_folder)

os.makedirs(output_folder, exist_ok=True)

# Loop archive folder
for file_name in os.listdir(archive_folder):
    file_path = os.path.join(archive_folder, file_name)
    
    if zipfile.is_zipfile(file_path):
        extract_wav_from_zip(file_path, output_folder)

print("WAV extraction from zip files complete.")
