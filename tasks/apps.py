import os
import subprocess
import webbrowser

def open_notepad():
    os.system("start notepad")

def open_chrome():
    # You can replace this path with your actual Chrome path
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    subprocess.Popen([chrome_path])

def play_music():
    music_path = "D:\\Music\\sample.mp3"  # Replace with your music file
    os.startfile(music_path)