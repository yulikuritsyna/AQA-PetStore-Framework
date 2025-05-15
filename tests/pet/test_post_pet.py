class TestPostPet:
    path = 'pet'

    def test_success_create(self, http, create_body, assert_status_code):
        resp = http.post(url_path=self.path, body=create_body)
        assert_status_code(resp)
