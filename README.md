# Hand Gesture Control using MediaPipe and PyAutoGUI

This Python script utilizes the MediaPipe library to detect hand gestures from a webcam feed and controls keyboard inputs accordingly using PyAutoGUI.

## Requirements
- Python 3
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- PyAutoGUI
- `directkeys` module (assumed to contain `right_pressed`, `left_pressed`, `PressKey`, and `ReleaseKey` functions)
- Webcam

## Setup

1. Install the required libraries:

    ```bash
   pip install -r requirements.txt
    ```

2. Ensure you have the `directkeys` module in your project directory.

3. Connect a webcam to your system.

## Usage

1. Run the script.

   ```bash
   python main.py
   ```

3. Bring your hand in front of the webcam.

4. Control the keyboard inputs using hand gestures:
    - Spread all fingers to accelerate (Gas).
    - Close all fingers to brake.

5. Press 'q' to quit and close the webcam feed.

## Code Explanation

- Imports required libraries and modules.

- Defines key mappings for keyboard inputs (`break_key_pressed` for braking and `accelerator_key_pressed` for acceleration).

- Sets up MediaPipe for hand detection.

- Enters an infinite loop to continuously process webcam frames.

- Detects hand landmarks using MediaPipe and extracts finger positions.

- Determines hand gestures based on finger positions:
    - All fingers closed: Braking action.
    - All fingers spread: Accelerating action.

- Emulates keyboard inputs using PyAutoGUI based on detected hand gestures.

- Handles key presses and releases.

- Displays the webcam feed with hand landmarks.

- Listens for 'q' key press to quit the application.

- Releases the webcam resources and closes all windows upon quitting.

## Notes

- Ensure proper lighting conditions for accurate hand detection.

- Adjust `min_detection_confidence` and `min_tracking_confidence` parameters in `mp_hand.Hands` initialization for better accuracy.

- Customize key mappings in `pyautogui.keyUp()` and `pyautogui.keyDown()` functions as per your requirement.

- This script assumes only one hand is present in the webcam frame and tracks gestures for that hand only.

- Make sure to have the necessary permissions to control keyboard inputs programmatically, especially if running on systems with security restrictions.

