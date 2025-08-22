import configuration
import requests
import data


def create_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.header)

response = create_new_user(data.create_user_body)


def create_new_kit(name):
    auth_token = response.json()["authToken"]

    head = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"}

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         headers = head,
                         json = {"name": name})

response2 = create_new_kit(data.kit_name)
