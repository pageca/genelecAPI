import requests
import base64
import json

# Define the base URL for your Genelec API
base_url = "http://192.168.0.79:9000/public/v1"

# Prepare the headers with authorization and keep-alive
headers = {
    "Accept": "application/json",
    "Authorization": base64.b64encode(b"admin:admin").decode(),
    "Connection": "keep-alive",
    "Content-Length": "0"
}

# Define a session to manage the connection
session = requests.Session()

# Example 1: Send a GET request
response = session.get(f"{base_url}/device/info", headers=headers)
print("Response from GET request:", response.text)

# Example 2: Send a PUT request to change the volume
message_body = {
    "level": -15.0,
    "mute": False
}

message_length = len(json.dumps(message_body).encode("utf-8"))

# set message length to messsage body size
headers["Content-Length"] = message_length
response = session.put(f"{base_url}/audio/volume", json=message_body, headers=headers)
print("Response from PUT request:", response.text)

# Example 3: Send another GET request
response = session.get(f"{base_url}/audio/inputs", headers=headers)
print("Response from another GET request:", response.text)

# Don't forget to close the session when you're done
session.close()
