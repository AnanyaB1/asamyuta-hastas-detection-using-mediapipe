# Asamyuta Hastas Recognition using MediaPipe
------------------------------------------

This project aims to recognize the 28 unique hand signs, known as the Asamyuta Hastas, from the Indian classical dance form, Bharatanatyam. We recognise them using a machine learning model trained using a dense neural network, utilizing keypoints detected from hand gestures and their respective euclidian distances.

## CREDITS
Much of the foundational code for this project was adapted from the [hand-gesture-recognition-mediapipe repository](https://github.com/kinivi/hand-gesture-recognition-mediapipe). However, significant modifications were made to cater to the specific needs of recognizing Asamyuta Hastas, including changes in data collection methodology and model architecture.

## DATA COLLECTION
The original script was adapted to enable the collection of data corresponding to 28 gestures, labeled from 0 to 27. This comprehensive range ensures that all Asamyuta Hastas gestures are accounted for during data collection, providing a robust dataset for training.

### Hand sign recognition training
#### 1. Learning data collection
Press "k" to enter the mode to save key points（displayed as 「MODE:Logging Key Point」）<br>
#### 2. Saving data points
You start off at gesture 0, or "Pathaka", and to save the frame press "s". You can press the right arrow key (->) to increase the gesture index, and then to log the next gesture and so on until 27 gestures. The data points will be saved to "model/keypoint_classifier/keypoint.csv".
#### 3. Data Processing & Cleaning
The key point coordinates in the hand are logged as data points after normalisation and standardisation & the euclidian distances between each of the points are also stored in order to better train the model.

The current dataset in this repo (in "model/keypoint_classifier/keypoint.csv") does not have the euclidean distances to minimise size of upload. To achieve the final dataset I used, run 
```bash
python euclid_dist.py
```
and the final data set, with the euclidian distances and flipped data points to model left hand data will be saved to "model\keypoint_classifier\keypoint_with_euclid_and_left.csv"

## MODEL TRAINING
The neural network was fine-tuned to better recognize the nuances of Asamyuta Hastas. Specifically:
- More hidden layers were introduced to capture intricate patterns.
- Each layer was populated with a greater number of neurons to increase the model's capacity.

## Directory
```
│   app.py
│   euclid_distance.py
│   keypoint_classification_EN.ipynb
│   README.md
│
├───model
│   │   __init__.py
│   │
│   ├───keypoint_classifier
│       │   keypoint.csv
│       │   keypoint_classifier.hdf5
│       │   keypoint_classifier.py
│       │   keypoint_classifier.tflite
│       └───keypoint_classifier_label.csv
│   
│
└───utils
    └─── cvfpscalc.py
```

## RESULTS
The trained model demonstrated promising performance. 
<img src= https://github.com/AnanyaB1/asamyuta-hastas-detection-using-mediapipe/assets/63778650/76ac906b-f47a-43e6-bb60-3712b688c968 width="60%"><br><br>

Overall accuracy: 98.0%

## CONCLUSION
This project offers an innovative application of hand gesture recognition technology to the rich tapestry of Indian classical dance. By seamlessly merging the ancient art of Bharatanatyam with modern ML techniques, I hope to foster a deeper appreciation of both domains.
