import requests


def validate_user_id(user_id):
    resp = requests.get(f"https://abstract-user-dot-heroic-climber-277222.df.r.appspot.com//user/list/{user_id}/")
    print(resp.status_code)
    if resp.status_code == 200:
        print(resp.json())
        return True
