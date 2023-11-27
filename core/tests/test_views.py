from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class CoreViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_home_view(self):
        url = reverse('core:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'core/home.html')

    def test_index_view(self):
        self.client.force_login(self.user)
        url = reverse('core:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'core/index.html')

    def test_signin_view(self):
        url = reverse('core:signin')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'core/signin.html')

    def test_signup_view(self):
        url = reverse('core:signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'core/signup.html')

    def test_signout_view(self):
        # Assuming your URL name for signout is 'core:signout'
        url = reverse('core:signout')
        
        # You can directly use the self.client.post method for the sign-out action
        response = self.client.post(url)
        
        # Check if the sign-out action results in a redirect (status code 302)
        self.assertEqual(response.status_code, 302)

        # You can also check if the user is no longer authenticated after signout
        self.assertNotIn('_auth_user_id', self.client.session)
    
    def tearDown(self):
        # Cleanup after each test
        self.user.delete()