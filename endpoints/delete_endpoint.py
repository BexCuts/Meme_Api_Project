from endpoints.endpoints_main_class import EndpointsMain
import requests
import allure


class DeleteObject(EndpointsMain):

    @allure.step('Delete object')
    def delete_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/meme/{object_id}', headers=headers)
        self.json = self.response.json()
        return self.response
