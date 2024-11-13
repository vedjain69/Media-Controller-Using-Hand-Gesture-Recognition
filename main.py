import cv2  # Computer Vision Library
import mediapipe as mp  # MediaPipe for hand tracking
import pyautogui as pt # Auto GUI for Command Binding
import time
import win32gui
import win32con
import tkinter as tk
from PIL import Image, ImageTk

# Opens a webcam for capture. The value 0 uses the default camera
def start_app():
    # Close the Tkinter window
    root.destroy()

    # Opens a webcam for capture. The value 0 uses the default camera
    cap = cv2.VideoCapture(0)

    def fing_counters(lst):
        cnt=0
        thresh=(lst.landmark[0].y*100-lst.landmark[9].y*100)/2

        if((lst.landmark[5].y*100-lst.landmark[8].y*100))>thresh:
            cnt+=1
        if((lst.landmark[9].y*100-lst.landmark[12].y*100))>thresh:
            cnt+=1
        if((lst.landmark[13].y*100-lst.landmark[16].y*100))>thresh:
            cnt+=1
        if((lst.landmark[17].y*100-lst.landmark[20].y*100))>thresh:
            cnt+=1
        if((lst.landmark[5].x*100-lst.landmark[4].x*100))>5:
            cnt+=1
        return cnt




    # Initialize MediaPipe's drawing and hand detection modules
    drawing = mp.solutions.drawing_utils
    hands = mp.solutions.hands
    hands_obj = hands.Hands(max_num_hands=1)


    start_init = False 
    prev = -1


    while True:  # Infinite loop for continuous capture
        end_time = time.time()
        _, frm = cap.read()  # Reading frame

        frm = cv2.flip(frm, 1)  # Flipping to make it a mirror image

        # Process the frame for hand landmarks, converting to RGB as required by MediaPipe
        res = hands_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))



        # If hand landmarks are detected, draw them
        if res.multi_hand_landmarks:
            hand_keypoints=res.multi_hand_landmarks[0]

            cnt=fing_counters(hand_keypoints)

            if not(prev==cnt):
                if not(start_init):
                    start_time = time.time()
                    start_init = True

                elif (end_time-start_time) > 0.2:
                    if (cnt == 1):
                        pt.press("right")
                    
                    elif (cnt == 2):
                        pt.press("left")

                    elif (cnt == 3):
                        pt.press("up")
                        pt.press("up")
                        pt.press("up")
                        pt.press("up")

                    elif (cnt == 4):
                        pt.press("down")
                        pt.press("down")
                        pt.press("down")
                        pt.press("down")

                    elif (cnt == 5):
                        pt.press("space")

                    prev = cnt
                    start_init = False

            drawing.draw_landmarks(frm, hand_keypoints, hands.HAND_CONNECTIONS)

        # Displaying the frame with landmarks in real-time
        cv2.imshow("window", frm)

        preview = cv2.resize(frm, (160, 120))  # Resize to a small thumbnail size
        cv2.imshow("Corner Preview", preview)

        #########
        gesture_instructions = {
        1: "5 Second Forward",
        2: "5 Seconds Backwardst",
        3: "Volume UP",
        4: "Volume Down",
        5: "Play/Pause"
    }
        instruction_text = gesture_instructions.get( "Perform a Gesture")
        
        # Put text below the preview window
        # Position the text 10 pixels below the preview window
        preview_with_instructions = preview.copy()
        cv2.putText(preview_with_instructions, instruction_text, (10, 135), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # Display the preview window with instructions
        cv2.imshow("Corner Preview", preview_with_instructions)

        # Set the corner preview as always on top and position it at the bottom-right corner
        preview_hwnd = win32gui.FindWindow(None, "Corner Preview")
        win32gui.SetWindowPos(preview_hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE) 


        # Press 'Esc' key to exit
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()  # Close all OpenCV windows
            cap.release()  # Release the webcam
            break



root = tk.Tk()
root.title("Media Controller")

#root.attributes("-fullscreen", True)
root.geometry("600x800")


image = Image.open("logo.png")  
image = image.resize((600, 300))
photo = ImageTk.PhotoImage(image)

# Create and place the image in the Tkinter window
image_label = tk.Label(root, image=photo)
image_label.pack()

# Create and place the instruction text
instruction_label = tk.Label(root, text="Welcome to Hand Gesture Recognition Media Contoller app - Wednesday!\n\nPlease follow the instructions below:\n\n1. Hold your hand in front of the camera.\n2. Perform one of the gestures:\n   - 1 Finger = Move 5 Second Forward\n   - 2 Fingers = Move 5 Second Backwards\n   - 3 Fingers = Volume Up\n   - 4 Fingers = Volume Down\n   - 5 Fingers = Play/Pause\n\n Use ESC key to exit the controller.", justify="left")
instruction_label.pack(pady=20)

# Create and place the "Next" button
next_button = tk.Button(root, text="Next", command=start_app)
next_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
