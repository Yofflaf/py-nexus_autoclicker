import time
import pyautogui
import easyocr
import numpy as np

print("Initializing text recognition engine... Please wait.")
reader = easyocr.Reader(['en'])

TARGET_PHRASES = [
    "download manually",
    "slow download",
    "open vortex"
]

print("Script is active! Bring up your browser window.")
print("Press Ctrl+C in this terminal window to stop the script.")

try:
    while True:
        screenshot = pyautogui.screenshot()
        
        frame = np.array(screenshot)
        
        results = reader.readtext(frame)
        
        for (bbox, text, prob) in results:
            detected_text = text.strip().lower()
            
            for phrase in TARGET_PHRASES:
                if phrase in detected_text:
                    top_left = bbox[0]
                    bottom_right = bbox[2]
                    
                    center_x = int((top_left[0] + bottom_right[0]) / 2)
                    center_y = int((top_left[1] + bottom_right[1]) / 2)
                    
                    print(f"Found match: '{text}' -> Clicking at ({center_x}, {center_y})")
                    
                    pyautogui.click(center_x, center_y)
                    
                    time.sleep(2.0)
                    break # Break out of phrase loop to refresh screenshot
                    
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nScript stopped safely.")


input()
