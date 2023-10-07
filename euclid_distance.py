import pandas as pd
import numpy as np

# Load the data into a pandas dataframe
df = pd.read_csv('model\keypoint_classifier\keypoint.csv', header=None)

# This function computes the pairwise Euclidean distances for a list of points
def pairwise_distances(points):
    distances = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = np.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            distances.append(dist)
    return distances

# Convert right-hand points to left-hand points by flipping x-coordinates
def convert_to_left_hand(coords):
    left_coords = [(1 - x, y) for (x, y) in coords]
    return left_coords

# For each row in the DataFrame, compute the pairwise distances for both right and left hand and append them to the row
new_data = []

for _, row in df.iterrows():
    label = int(row[0])
    
    # Right hand coordinates
    right_coords = list(zip(row[1::2], row[2::2]))  # Forming (x,y) pairs for the 21 points
    right_distances = pairwise_distances(right_coords)
    
    # Append right hand data
    right_hand_row = [label] + list(row)[1:] + right_distances
    new_data.append(right_hand_row)
    
    # Left hand coordinates
    left_coords = convert_to_left_hand(right_coords)
    left_distances = pairwise_distances(left_coords)
    
    # Append left hand data
    left_hand_row = [label] + [1 - coord for coord in row[1::2]] + list(row)[2::2] + left_distances
    new_data.append(left_hand_row)

# Convert the processed data back to a dataframe and save to a new CSV
new_df = pd.DataFrame(new_data)
new_df.to_csv('model\keypoint_classifier\keypoint_with_euclid_and_left.csv', index=False, header=False)