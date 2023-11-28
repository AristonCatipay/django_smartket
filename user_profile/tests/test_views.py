from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from user_profile.models import Profile

class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name = 'firstname test',
            last_name = 'lastname test',
            username='testuser',
            email='emailtest',
            password='12345'
        )

        self.profile = Profile.objects.create(
            user = self.user,
            image = 'media/default_profile_image.jpg',
        )

    def test_index_view(self):
        self.client.force_login(self.user)
        url = reverse('profile:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response ,'user_profile/index.html')

    def test_edit_view(self):
        self.client.force_login(self.user)
        url = reverse('profile:edit')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile/edit.html')

        data = {
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'username': self.user.username,
            'email': self.user.email,
            'password': self.user.password,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        
    def tearDown(self):
        # Cleanup after each test
        self.profile.delete()
        self.user.delete()