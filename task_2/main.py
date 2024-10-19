import requests

from config import TOKEN


class YADisk:
    YD_BASE_URL = 'https://cloud-api.yandex.net/v1/disk'

    def __init__(self, token):
        self.token = token

    def get_common_params(self):
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _build_url(self, method):
        return f'{self.YD_BASE_URL}/{method}'

    def create_new_folder(self, folder_name):
        params = {
            'path': folder_name
        }
        response = requests.put(self._build_url('resources'), params=params,
                                headers=self.get_common_params())
        return response.status_code
