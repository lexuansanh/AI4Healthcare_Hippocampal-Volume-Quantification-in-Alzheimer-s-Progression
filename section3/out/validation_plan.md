# Validation Plan

## 1. General Information

### Intended Use
The AI model is designed to assist clinicians in quantifying the volume of the hippocampal area in MRI scans. This information provides a quick measurement of the hippocampal volume, aiding clinicians in their assessments. However, clinicians will need to gather additional information about their patients and conduct further analysis to draw definitive conclusions.

### Indications for Use
The tool is suitable for both male and female patients and is specifically intended for use with MRI images.

### Device Limitations
The algorithm requires a high-power processing GPU card to run effectively.

## 2. Dataset

### Collecting Training Data
The training dataset is sourced from the "Hippocampus" dataset from the [Medical Decathlon competition](http://medicaldecathlon.com/#tasks). The dataset consists of NIFTI files, each representing a volume and its corresponding segmentation mask. For training purposes, we use cropped volumes that focus on the hippocampus region, which significantly reduces the size of each sample, allowing for quicker training times.

### Labeling Training Data
The labels are created by expert radiologists. The labeling convention for the training data is as follows:
- The anterior part of the hippocampus is labeled as 1.
- The posterior part of the hippocampus is labeled as 2.
- All other parts (background) are labeled as 0.

These labels are in the form of masks overlaid on the images, showing the position and size of the hippocampus against a dark background.

## 3. Algorithm Performance

### Measuring Training Performance
The performance of the algorithm is measured using two key metrics:
- Dice Similarity Coefficient (DSC)
- Jaccard Similarity Coefficient (JSC)

The algorithm achieves a Dice Similarity Coefficient of approximately 0.90 and a Jaccard Similarity Coefficient of around 0.82.

### Real-World Performance
The real-world performance can be validated by applying the model to separate datasets. Since the dataset does not include information about age, gender, or the condition of patients, these factors cannot be directly accounted for in the validation process. However, in real-world applications, additional patient information such as gender, age, and medical condition can be used to improve validation and ensure the model performs well across diverse populations.

## 4. Real-World Inference

- The algorithm is designed to perform well on T2 MRI scans of the full brain.
- It is not suitable for use with CT scans or any other imaging formats.
- The algorithm is specifically intended for measuring the volume of the hippocampus and cannot be used for other body parts.

## 5. Additional Considerations

### Ground Truth and Validation
To establish the ground truth, silver standard readings from radiologists can be used. This helps ensure the robustness of the ground truth and represents the population for which the algorithm is intended.

### Clinical Validation
The clinical validation plan will involve proving that the AI model accurately measures hippocampal volume as claimed. This will include defining the accuracy of the algorithm, measuring its performance in the real world, and establishing the data on which the algorithm can operate. Validation will consider various patient demographics and conditions to ensure broad applicability.

By following this validation plan, we aim to ensure that the AI model performs reliably and provides valuable assistance to clinicians in measuring hippocampal volume from MRI scans.