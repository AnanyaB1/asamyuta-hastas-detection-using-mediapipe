# Asamyuta Hastas Recognition using MediaPipe
------------------------------------------

This project aims to recognize the 28 unique hand signs, known as the Asamyuta Hastas, from the Indian classical dance form, Bharatanatyam. We recognise them using a machine learning model trained using a dense neural network, utilizing keypoints detected from hand gestures and their respective euclidian distances.

## CREDITS
Much of the foundational code for this project was adapted from the [hand-gesture-recognition-mediapipe repository](https://github.com/kinivi/hand-gesture-recognition-mediapipe). However, significant modifications were made to cater to the specific needs of recognizing Asamyuta Hastas, including changes in data collection methodology and model architecture.

## DATA COLLECTION
The original script was adapted to enable the collection of data corresponding to 28 gestures, labeled from 0 to 27. This comprehensive range ensures that all Asamyuta Hastas gestures are accounted for during data collection, providing a robust dataset for training.

## MODEL TRAINING
The neural network was fine-tuned to better recognize the nuances of Asamyuta Hastas. Specifically:
- More hidden layers were introduced to capture intricate patterns.
- Each layer was populated with a greater number of neurons to increase the model's capacity.

## RESULTS
The trained model demonstrated promising performance. 

Note: A confusion matrix offers a summary of prediction results on a classification problem. The number of correct and incorrect predictions are summarized with count values and broken down by each class.

## CONCLUSION
This project offers an innovative application of hand gesture recognition technology to the rich tapestry of Indian classical dance. By seamlessly merging the ancient art of Bharatanatyam with modern ML techniques, we hope to foster a deeper appreciation of both domains.
