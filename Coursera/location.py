import requests


def get_my_location():
    return requests.get("https://freegeoip.net/json/").json()


if __name__ == "__main__":
    print(get_my_location())
