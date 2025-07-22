# ANN2SNN-SpikingJelly-

# SNN Conversion and Simulation

This project provides a pipeline for training a convolutional neural network (CNN) on spectrogram images, converting the trained model to a spiking neural network (SNN), and evaluating both conventional and spiking performance. The use case: binary classification of participants based on their PHQ-8 score, for depression detection.

## Features

- Loads spectrogram images and corresponding labels from Excel and PNG files.
- Balances the dataset using SMOTE.
- Trains a CNN for binary classification.
- Converts the trained ANN to SNN using SpikingJelly.
- Evaluates accuracy, F1, ROC-AUC, and confusion matrix for both ANN and SNN models.

## Requirements

- Python 3.x
- PyTorch
- pandas
- numpy
- scikit-learn
- imbalanced-learn
- matplotlib
- seaborn
- Pillow
- spikingjelly

## File Structure

- Input Excel: participant labels (PHQ-8 binary)  
- Input images: spectrogram PNGs (participant ID in filename)
- Model output: `ENERGY1.pth`
- Data needs to be prepared first

## Usage

1. Update the notebook file paths to your local environment:
   - Excel file (labels):  
     `C:/woic/1sorted.xlsx`
   - Spectrogram images:  
     `C:/2Spectrogram/*.png`

2. Run all cells in the notebook.  
   This will:
   - Load data and labels.
   - Balance classes using SMOTE.
   - Train the CNN model.
   - Convert to SNN and evaluate performance.

3. Model weights are saved to `ENERGY1.pth`.

## Notes

- SNN conversion relies on SpikingJelly's `Converter`.
- Evaluation prints metrics and confusion matrices for both ANN and SNN versions.
- This code expects that participant IDs can be parsed from the spectrogram filenames.
- Early stopping is implemented for CNN training.

## Citation

If you use this code, cite the original authors and SpikingJelly.

---

*No warranty. Assumes user is familiar with PyTorch and has a CUDA-capable GPU for best performance.*

SpikingJelly repository - https://github.com/fangwei123456/spikingjelly
