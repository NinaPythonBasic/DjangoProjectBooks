from django.test import TestCase
from books.tests.utils import (
    bookonhand_header,
    get_category,
    get_book,
    get_reader,
    get_bookonhand,
    login_user,
)
from django.contrib.auth.models import User


class TestBookOnHandListView(TestCase):
    def setUp(self) -> None:
        login_user(self)

    def test_response_status_code(self):
        response = self.client.get("/booksonhand/")
        self.assertEqual(response.status_code, 200)

    def test_response_context(self):
        response = self.client.get("/booksonhand/")
        self.assertIn("object_list", response.context)
        self.assertIn("bookonhand_list", response.context)

    def test_content(self):
        bookonhand = get_bookonhand(get_book(get_category()), get_reader())
        response = self.client.get("/booksonhand/")
        href = f'<a  href="/bookonhand/{bookonhand.pk}/">'.encode(encoding="utf-8")
        self.assertIn(href, response.content)


class TestBookOnHandDetailView(TestCase):
    def setUp(self) -> None:
        login_user(self)

    def test_response_unknown_page(self):
        # status_code
        response = self.client.get("/bookonhand/77/")
        self.assertEqual(response.status_code, 404)

    def test_response_known_page(self):
        bookonhand = get_bookonhand(get_book(get_category()), get_reader())
        # status_code
        response = self.client.get(f"/bookonhand/{bookonhand.pk}/")
        self.assertEqual(response.status_code, 200)
        # context
        self.assertIn("object", response.context)
        self.assertIn("bookonhand", response.context)
        # content
        header = bookonhand_header.encode(encoding="utf-8")
        self.assertIn(header, response.content)
