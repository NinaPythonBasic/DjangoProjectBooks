from django.test import TestCase
from books.tests.utils import login_user, username


class TestIndexView(TestCase):
    def test_guest_index_page(self):
        # status_code
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        # content
        hello = "Здравствуйте, Читатель!".encode(encoding="utf-8")
        self.assertIn(hello, response.content)

    def test_authorized_index_page(self):
        # create user
        login_user(self)
        # authorized user
        # status_code
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        # content
        hello = f"Здравствуйте, {username}!".encode(encoding="utf-8")
        self.assertIn(hello, response.content)
        self.client.logout()

    def test_left_links(self):
        # create user
        login_user(self)
        # authorized user
        response = self.client.get("/")
        # content

        href_list = '<a href="/categories/">'.encode(encoding="utf-8")
        self.assertIn(href_list, response.content)

        href_list = '<a href="/books/">'.encode(encoding="utf-8")
        self.assertIn(href_list, response.content)

        href_list = '<a href="/readers/">'.encode(encoding="utf-8")
        self.assertIn(href_list, response.content)

        href_list = '<a href="/booksonhand/">'.encode(encoding="utf-8")
        self.assertIn(href_list, response.content)
