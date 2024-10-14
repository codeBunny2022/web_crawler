import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_crawl(self):
        response = self.client.post('/crawl', json={
            "root_url": "https://example.com",
            "depth": 2
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("crawled_links", response.get_json())

if __name__ == "__main__":
    unittest.main()
