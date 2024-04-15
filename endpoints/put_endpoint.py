from endpoints.endpoints_main_class import EndpointsMain
import requests
import allure


class PutObject(EndpointsMain):

    @allure.step('Full update object')
    def update_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/meme/{object_id}', json=body, headers=headers)
        self.json = self.response.json()
        return self.response
