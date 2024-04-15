import allure
import conftest


class EndpointsMain:
    url = 'http://167.172.172.115:52355'
    headers = {'Content-type': 'application/json', 'Authorization': conftest.create_new_token()}
    response = None
    json = None

    @allure.step("Check response text")
    def check_response_name(self, text):
        assert self.response.json()['text'] == text

    @allure.step("Check status code is 200")
    def check_status_code(self):
        assert self.response.status_code == 200

    @allure.step("Check status code is 400")
    def check_status_code_bad(self):
        assert self.response.status_code == 400

    @allure.step("Check id is correct")
    def check_id(self, object_id):
        assert self.response.json()['id'] == object_id
