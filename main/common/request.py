import requests


class Request:
    def __init__(self, url):
        self.url = url

    def get(self, url_path, params, headers):
        print("Отправили запрос")
        resp = requests.get(
            url=f'{self.url}/{url_path}',
            params=params,
            headers=headers
        )
        print("Получили ответ")
        return resp

    def post(self, url_path, body):
        print("Отправили запрос")
        resp = requests.post(
            url=f'{self.url}/{url_path}',
            json=body
        )
        print("Получили ответ")
        return resp