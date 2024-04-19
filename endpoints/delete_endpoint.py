from endpoints.endpoints_main_class import EndpointsMain
import requests
import allure


class DeleteMeme(EndpointsMain):

    @allure.step('Delete the meme')
    def delete_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f"{self.url}/meme/{meme_id}", headers=headers)
        self.json = self.response.json()
        return self.response
