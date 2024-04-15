from endpoints.endpoints_main_class import EndpointsMain
import requests
import allure


class CreateObject(EndpointsMain):

    @allure.step('Create new object')
    def create_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/meme', json=body, headers=headers)
        self.json = self.response.json()
        return self.response
