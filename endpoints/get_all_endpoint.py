from endpoints.endpoints_main_class import EndpointsMain
import requests
import allure


class GetAllMemes(EndpointsMain):

    @allure.step('Get all memes')
    def get_all_memes(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme', headers=headers)
        self.json = self.response.json()
        return self.response
