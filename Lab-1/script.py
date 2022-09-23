import requests

print(requests.__version__)
print(requests.get("http://www.google.com")
)
raw  = requests.get("https://raw.githubusercontent.com/NatDev7/CMPUT-404-LABS/main/script.py")
print(raw.text)
