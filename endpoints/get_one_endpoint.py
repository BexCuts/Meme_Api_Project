from endpoints.endpoints_main_class import EndpointsMain
import requests
import allure


class GetObjectById(EndpointsMain):

    @allure.step('Get object by id')
    def get_object_by_id(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(f'{self.url}/meme/{object_id}', headers=headers)
        self.json = self.response.json()
        return self.response
