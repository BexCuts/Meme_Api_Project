from endpoints.endpoints_main_class import EndpointsMain
import requests
import allure


class GetObjects(EndpointsMain):

    @allure.step('Get all objects')
    def get_all_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme', headers=headers)
        self.json = self.response.json()
        return self.response
