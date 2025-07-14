import requests
import webbrowser

def search_google(query: str):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def get_public_ip():
    try:
        ip = requests.get("https://api64.ipify.org").text
        return ip
    except:
        return "Unable to fetch IP."