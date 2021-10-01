from django.test import TestCase
from django.shortcuts import reverse
# Create your tests here.


class LandingPageTest(TestCase):

    def test_status_code(self):
        # TODO some test
        response = self.client.get(reverse("landing-page"))
        print(response.status_code)
        # response.status_code
        self.assertEqual(response.status_code, 200)
        pass

    def test_template_name(self):
        # TODO some test
        response = self.client.get(reverse("landing-page"))
        self.assertTemplateUsed(response, "landing.html")
        pass
