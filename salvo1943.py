import time
import requests

TOKEN_DELETER = input("Token: ")
VANITY_URL = input("Vanity-URL: ")

DELETER_HEADERS = {
    "Authorization": TOKEN_DELETER,
}

def deleter_action():
    time.sleep(1)
    response = requests.delete(f"https://discord.com/api/v10/invites/{VANITY_URL}",
                               headers=DELETER_HEADERS)
    print(f"Response Status Coe: {response.status_code}")
    print(f"Response Content: {response.text}")

deleter_action()