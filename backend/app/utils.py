import mediapipe as mp
import cv2
import numpy as np

# Initialize MediaPipe Holistic
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(static_image_mode=False)

def extract_keypoints(image):
    """
    Extract 471 key points from the given image using MediaPipe Holistic.

    :param image: Input image (numpy array)
    :return: Flattened numpy array of key points
    """
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
