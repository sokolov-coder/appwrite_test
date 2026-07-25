import requests
import json


PROJECT_ID = "6a65222f000016630610"

FUNCTION_ID = "6a652cf000337b977e14"

API_KEY = "standard_882acf6adde857b9fbcaec4640a9f624a1130f705f571ad107c285f2bcdba35e219d529dae80e131804889ea83e88587566463b311a823fe4184b77318ad78da258d559897d41fe301f09d0f851166ae314e4eca4e922b2ab7003aae58af0a530e2161b012e90ec41aa58affad4e2a425d9c3b897a0bbbe2077ca58c4b9f1cec"


URL = (
    f"https://cloud.appwrite.io/v1/functions/"
    f"{FUNCTION_ID}/executions"
)


payload = {
    "data": json.dumps({
        "text": "I love Python programming"
    })
}


headers = {
    "X-Appwrite-Key": API_KEY,
    "X-Appwrite-Project": PROJECT_ID,
    "Content-Type": "application/json"
}


response = requests.post(
    URL,
    headers=headers,
    json=payload
)


print("STATUS:", response.status_code)

print(response.json())