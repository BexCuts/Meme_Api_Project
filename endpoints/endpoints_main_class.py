import allure
import conftest


class EndpointsMain:
    url = 'http://167.172.172.115:52355'
    headers = {'Content-Type': 'application', 'Authorization': None}
    response = None
    json = None

    def __init__(self, token):
        self.token = token
        self.headers['Authorization'] = self.token

    @allure.step('Check response code is 200')
    def check_response_code(self):
        assert self.response.status_code == 200

    @allure.step('Check response id is correct')
    def check_response_id(self, meme_id):
        assert self.response.json()['id'] == meme_id

    @allure.step('Check response code is 400')
    def check_response_400_code(self):
        assert self.response.status_code == 400
