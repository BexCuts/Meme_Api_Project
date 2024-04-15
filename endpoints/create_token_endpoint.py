from endpoints.endpoints_main_class import EndpointsMain
import requests
import allure


class CreateToken(EndpointsMain):

    @allure.step('Create new token')
    def create_new_token(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(f'{self.url}/authorize', json=body)
        self.json = self.response.json()
        return self.response
