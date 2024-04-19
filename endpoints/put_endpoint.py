from endpoints.endpoints_main_class import EndpointsMain
import allure
import requests


class UpdateEndpoint(EndpointsMain):

    @allure.step('Update meme')
    def update_meme(self, meme_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/meme/{meme_id}', json=body, headers=headers)
        self.json = self.response.json()
        return self.response
