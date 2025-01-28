FocusTime AI

An AI-powered web application to enhance productivity and combat procrastination using real-time gesture analysis.

📌 Overview

FocusTime AI is a cutting-edge web application that integrates advanced machine learning and computer vision technologies to monitor and improve focus during study sessions. By leveraging MediaPipe Holistic and TensorFlow, the app performs real-time gesture analysis to detect signs of procrastination and provide timely interventions to help users stay on track.

🌟 Features

Real-Time Gesture Detection: Uses MediaPipe Holistic to extract 471 key points, analyzing body posture, hand movements, and facial expressions.

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

📂 Project Structure

FocusTimeAI/
|-- frontend/                # React-based frontend code
|-- backend/                 # Flask API and backend services
|-- models/                  # TensorFlow models for gesture analysis
|-- media_processing/        # MediaPipe Holistic integration
|-- static/                  # Static files like CSS, images, etc.
|-- templates/               # Flask templates for rendering
|-- requirements.txt         # Python dependencies
|-- README.md                # Project documentation

🚀 Getting Started

Prerequisites

Python 3.8+

Node.js 16+

PostgreSQL 13+

Installation

Clone the Repository:

git clone https://github.com/ekagra1602/FocusTime-AI
cd FocusTimeAI

Set Up Backend:

cd backend
python3 -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate    # For Windows
pip install -r requirements.txt

Set Up Frontend:

cd ../frontend
npm install

Set Up Database:

Create a PostgreSQL database.

Update database credentials in backend/config.py.

Run the Application:

Backend:

cd backend
flask run

Frontend:

cd ../frontend
npm start

Access the App:
Open your browser and navigate to http://localhost:3000.

🧠 How It Works

Data Capture:

MediaPipe Holistic extracts 471 key points from the user's body, hands, and face in real-time.

Model Prediction:

TensorFlow analyzes these points to classify user gestures into "focused" or "distracted" categories.

Feedback Loop:

If distraction is detected, the app provides prompts or suggestions to refocus.

🛡️ Security & Privacy

FocusTime AI is designed with user privacy in mind. No personal data or video streams are stored. Only processed gesture data is used to enhance the user experience.

🐛 Bug Reporting

If you encounter any bugs, please open an issue in the repository with detailed steps to reproduce the problem.

📜 License

This project is licensed under the MIT License.

📧 Contact

For questions or support, contact us at your-email@example.com.

✨ Acknowledgments

Google MediaPipe for the Holistic solution.

TensorFlow for enabling robust machine learning.

Open Source Community for inspiration and tools.

Stay focused and productive with FocusTime AI!

