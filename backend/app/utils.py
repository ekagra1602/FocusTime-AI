import mediapipe as mp
import cv2
import numpy as np
from typing import Union, Tuple

# Initialize MediaPipe Holistic
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(static_image_mode=False)

def extract_keypoints(image: np.ndarray) -> np.ndarray:
    """
    Extrac 543 key points from the given image using MediaPipe Holistic.
    
    The key points include:
    - 33 pose landmarks (x, y, z, visibility)
    - 468 face landmarks (x, y, z)
    - 21 left hand landmarks (x, y, z)
    - 21 right hand landmarks (x, y, z)
    
    Total: 543 key points (33*4 + 468*3 + 21*3 + 21*3)

    Args:
        image (np.ndarray): Input image in BGR format (OpenCV default)
                           Expected shape: (height, width, 3)

    Returns:
        np.ndarray: Flattened array of 543 key points

    Raises:
        ValueError: If input image is not a valid numpy array or has incorrect shape
    """
    if not isinstance(image, np.ndarray):
        raise ValueError("Input must be a numpy array")
    
    if len(image.shape) != 3 or image.shape[2] != 3:
        raise ValueError("Input image must be a 3-channel BGR image")

    try:
        # Convert the image to RGB (MediaPipe requires RGB)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image with MediaPipe
        results = holistic.process(image_rgb)

        # Extract key points
        pose = (
            np.array(
                [[landmark.x, landmark.y, landmark.z, landmark.visibility]
                 for landmark in results.pose_landmarks.landmark]
            ).flatten()
            if results.pose_landmarks
            else np.zeros(33 * 4)
        )
        face = (
            np.array(
                [[landmark.x, landmark.y, landmark.z]
                 for landmark in results.face_landmarks.landmark]
            ).flatten()
            if results.face_landmarks
            else np.zeros(468 * 3)
        )
        left_hand = (
            np.array(
                [[landmark.x, landmark.y, landmark.z]
                 for landmark in results.left_hand_landmarks.landmark]
            ).flatten()
            if results.left_hand_landmarks
            else np.zeros(21 * 3)
        )
        right_hand = (
            np.array(
                [[landmark.x, landmark.y, landmark.z]
                 for landmark in results.right_hand_landmarks.landmark]
            ).flatten()
            if results.right_hand_landmarks
            else np.zeros(21 * 3)
        )

        # Concatenate all key points
        return np.concatenate([pose, face, left_hand, right_hand])
    
    except Exception as e:
        raise RuntimeError(f"Failed to process image: {str(e)}")
