from endpoints.endpoints_main_class import EndpointsMain
import allure
import requests


class GetOneMeme(EndpointsMain):

    @allure.step('Get meme by id')
    def get_one_endpoint(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme/{meme_id}', headers=headers)
        self.json = self.response.json()
        return self.response
