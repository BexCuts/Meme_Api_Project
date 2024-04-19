from endpoints.endpoints_main_class import EndpointsMain
import requests
import allure


class CreateTokenEndpoint(EndpointsMain):

    @allure.step('Create new token')
    def create_token(self, body):
        self.response = requests.post(f'{self.url}/authorize', json=body)
        self.json = self.response.json()
        return self.response
