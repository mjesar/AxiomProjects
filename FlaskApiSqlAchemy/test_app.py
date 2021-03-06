import unittest
import sys, json

from app import app
class TestMain(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"]=True
        self.app=app.test_client()


    def tearDown(self):
        pass

    def test_index_get(self):
        response=self.app.get("/")
        self.assertEqual(response.status_code,200)

    def test_one_get(self):
        response = self.app.get("/todo/6")
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.app.post("/todo")
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        response = self.app.put("/todo/6" )
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        response = self.app.delete("/todo/6")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
