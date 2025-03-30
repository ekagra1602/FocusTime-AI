FocusTime AI

An AI-powered web application to enhance productivity and combat procrastination using real-time gesture analysis.

🌟 Features

Real-Time Gesture Detection: Uses MediaPipe Holistic to extract 543 key points, analyzing body posture, hand movements, and facial expressions.

Machine Learning Integration: TensorFlow-powered models detect gestures associated with procrastination or loss of focus.

Actionable Feedback: Provides tailored suggestions and nudges to refocus the user.

User-Friendly Interface: Built with React for an intuitive and seamless user experience.

Data Management: PostgreSQL for secure and scalable data storage.

Backend Support: Flask for API endpoints and backend functionality.

🛠️ Tech Stack

Frontend

React: For building a dynamic and responsive user interface.

Backend

Flask: Lightweight and efficient framework for API development.

Machine Learning & Computer Vision

MediaPipe Holistic: To extract 471 key points from body, hand, and face landmarks.

TensorFlow: For training and deploying gesture analysis models.

Database

PostgreSQL: To manage user data securely and efficiently.


🧠 How It Works

Data Capture:

MediaPipe Holistic extracts 471 key points from the user's body, hands, and face in real-time.

Model Prediction:

TensorFlow analyzes these points to classify user gestures into "focused" or "distracted" categories.

Feedback Loop:

If distraction is detected, the app provides prompts or suggestions to refocus.


📜 License

This project is licensed under the MIT License.

📧 Contact

For questions or support, contact us at egupta3@asu.edu

✨ Acknowledgments

Google MediaPipe for the Holistic solution.

TensorFlow for enabling robust deep learning.


