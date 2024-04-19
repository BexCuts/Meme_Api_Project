from endpoints.endpoints_main_class import EndpointsMain
import allure
import requests


class PostEndpoint(EndpointsMain):

    @allure.step('Create new meme')
    def create_meme(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/meme', json=body, headers=headers)
        self.json = self.response.json()
        return self.response
