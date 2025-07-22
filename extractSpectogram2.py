import os
import numpy as np
import librosa
import librosa.display
import matplotlib
matplotlib.use('Agg')  # Use Agg backend to avoid Tkinter conflicts
import matplotlib.pyplot as plt
import glob
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import threading

plt.ioff()  # Turn off interactive plotting

def process_audio_file(audio_file, output_folder, chunk_duration=5, overlap_duration=2):
    y, sr = librosa.load(audio_file, sr=16000)
    file_name = os.path.splitext(os.path.basename(audio_file))[0]
    total_duration = len(y) / sr

    # spectrograms with overlap
    current_start = 0
    chunk_idx = 0
    while current_start < total_duration:
        # Calculate current chunk
        start_sample = int(current_start * sr)
        end_sample = start_sample + int(chunk_duration * sr)
        
        # Check remaining part
        if end_sample > len(y):
            break

        # Extract the chunk
        y_chunk = y[start_sample:end_sample]

        # Create Mel spectrogram
        if np.all(y_chunk == 0):
            current_start += (chunk_duration - overlap_duration)
            chunk_idx += 1
            continue
        
        S = librosa.feature.melspectrogram(y=y_chunk, sr=sr, n_mels=128)
        S_dB = librosa.power_to_db(S, ref=np.max)

        # Normalize the spectrogram
        S_min, S_max = S_dB.min(), S_dB.max()
        S_scaled = (S_dB - S_min) / (S_max - S_min + 1e-10)  # Avoid division by zero

        # Save spectrogram as grayscale
        with threading.Lock():
            fig, ax = plt.subplots(figsize=(2.5, 2.5))
            ax.axis('off')
            librosa.display.specshow(S_scaled, sr=sr, cmap='gray_r', ax=ax)
            output_file_name = f"{file_name}_chunk_{chunk_idx:04d}.png"
            output_file_path = os.path.join(output_folder, output_file_name)
            fig.savefig(output_file_path, bbox_inches='tight', pad_inches=0)
            plt.close(fig)

        # Update start position
        current_start += (chunk_duration - overlap_duration)
        chunk_idx += 1

def create_spectrograms(input_folder, output_folder, chunk_duration=5, overlap_duration=2):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    audio_files = glob.glob(os.path.join(input_folder, "*.wav"))

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        futures = [executor.submit(process_audio_file, audio_file, output_folder, chunk_duration, overlap_duration) for audio_file in audio_files]
        for future in tqdm(futures):
            future.result()

if __name__ == "__main__":
    input_folder = r"C:\1extractedAudio"
    output_folder = r"C:\2Spectrogram"
    create_spectrograms(input_folder, output_folder)

