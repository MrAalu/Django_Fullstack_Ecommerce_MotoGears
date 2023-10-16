from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class HomeTests(TestCase):
    def test_url_exists_at_current_location(self):
        # '/' URL ma yo APP Exists garxa ki nai
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        # 'homepage' named URL availabe xaki nai
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        # 'homepage' url is responsible for 'template' or NOT
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "home/index.html")

    def test_template_content(self):
        # HTML Contents of URL Check
        response = self.client.get(reverse("homepage"))

        # Here can check if , '<h1>homepage</h1>' exists on URL 'homepage' or NOT
        self.assertContains(response, "")
