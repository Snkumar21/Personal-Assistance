import pyautogui
import requests

def take_screenshot():
    img = pyautogui.screenshot()
    img.save("screenshot.png")

def get_joke():
    try:
        res = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        if res.status_code == 200:
            return res.json()['joke']
        return "I couldn't find a joke right now."
    except:
        return "Something went wrong while fetching a joke."