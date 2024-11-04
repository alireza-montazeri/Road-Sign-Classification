# Road Sign Classification using Deep Learning

This project aims to develop a deep learning model capable of accurately identifying and classifying critical road signs in Australia, focusing specifically on **Stop**, **Give Way**, **Speed Limit**, and **No Entry** signs. This classification is essential for the safe navigation of autonomous vehicles on Australian roads.

## Table of Contents

- [Background](#background)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Training and Evaluation](#training-and-evaluation)
- [Results](#results)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)

## Background

Classifying road signs accurately is crucial for autonomous driving applications. Key challenges addressed in this project include:

1. **Data Availability**: Ensuring a diverse dataset of labeled images under varying conditions.
2. **Class Imbalance**: Handling imbalances due to variations in road sign frequency.
3. **Visual Similarities**: Distinguishing between signs with similar colors and shapes.
4. **Real-time Performance**: Optimizing the model for fast inference.

## Dataset

The dataset was created by combining multiple sources:

- **GTSRB (German Traffic Sign Recognition Benchmark)**
- **Road Sign Detection Dataset**
- **Self-Driving Cars Computer Vision Project**

The dataset was split into training, validation, and test sets with a distribution of approximately 60%, 20%, and 20%.

> You can find the prepared dataset in [here](https://drive.google.com/file/d/1ENEHvPJKQZCGNnq3wsyNXPR3YybJy5a5/view?usp=sharing)

## Model Architecture

A custom Convolutional Neural Network (CNN) architecture was designed, consisting of:

- **Three convolutional layers** with increasing filter sizes (16, 32, 64).
- **MaxPooling layers** to reduce feature map size.
- **Dropout layers** to prevent overfitting.
- **Global Average Pooling** to reduce the number of parameters.

The output layer uses a softmax activation function for multi-class classification, targeting the four road sign classes.

## Training and Evaluation

The model was trained with TensorFlow on the following parameters:

- **Optimizer**: Adam with a learning rate of 0.001.
- **Loss Function**: Categorical Crossentropy.
- **Metrics**: Accuracy, Precision, Recall, F1-Score.

### Data Augmentation

To enhance model robustness, data augmentation techniques were applied, including:

- Position shifts
- Z-axis rotation
- Lighting variations
- Motion blur
- Additive noise

## Results

The model achieved **accuracy** and **f1-score** above 95% across most classes, showing strong performance in classifying road signs, even in visually similar cases.

| Class       | Precision | Recall | F1 Score |
| ----------- | --------- | ------ | -------- |
| Stop        | 0.96      | 0.95   | 0.95     |
| Give Way    | 0.98      | 0.98   | 0.98     |
| Speed Limit | 0.97      | 0.96   | 0.97     |
| No Entry    | 0.96      | 0.95   | 0.96     |

## Acknowledgements

Special thanks to datasets like **GTSRB** and **Self-Driving Cars Project** for enabling this project. This model is developed for educational and research purposes to advance autonomous vehicle safety.

---
