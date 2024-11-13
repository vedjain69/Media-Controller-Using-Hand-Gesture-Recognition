# Media Controller Using Hand Gesture Recognition

This project enables users to control media playback and system functions (like volume control, play/pause, and navigation) using hand gestures captured via a webcam. Leveraging computer vision techniques with **OpenCV**, **MediaPipe**, and **PyAutoGUI**, the system recognizes hand gestures and maps them to corresponding media control commands.

## Features
- **Hand Gesture Recognition**: Detects various hand gestures using MediaPipe’s hand tracking model.
- **Real-Time Control**: Allows users to control media (play/pause, volume, skip, etc.) using gestures in real time.
- **Customizable Commands**: The gesture-to-command mappings can be easily customized based on user preferences.
- **Multi-Hand Support**: Detect and track multiple hands for more complex control schemes (optional feature).

## Technologies Used
- **Python**: The programming language for implementing the application.
- **OpenCV**: Used for capturing and processing webcam video.
- **MediaPipe**: Utilized for hand gesture detection and tracking.
- **PyAutoGUI**: Used for controlling the media playback and other system functions based on gestures.
- **Tkinter**: GUI framework for displaying instructions and controls.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/vedjain69/media-controller-using-hand-gesture-recognition.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## How it Works
1. The application uses a webcam to track hand gestures in real time.
2. Gestures like "one finger" (right swipe), "two fingers" (left swipe), etc., are mapped to actions like play, pause, or navigation commands.
3. After starting the app, follow the on-screen instructions and perform the gestures in front of the camera.

## Customization
Feel free to modify the hand gesture-to-command mappings or add additional gestures to fit your specific needs. The code is designed to be easily extensible and customizable.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
