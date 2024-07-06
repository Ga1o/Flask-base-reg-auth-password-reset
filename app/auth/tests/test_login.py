import unittest
from app import create_app


class AuthBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def test_login(self):
        response = self.client.get()
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
