from django.test import SimpleTestCase

# Create your tests here.
class simpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)    

#  we perform a check if the status code
# for each page is 200, which is the standard response for a successful HTTP request.
# That’s a fancy way of saying it ensures that a given webpage actually exists, but says
# nothing about the content of said page.