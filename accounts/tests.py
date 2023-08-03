from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status


class UserAPITests(TestCase):
    def setUp(self):
        # Set up the test client
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='testuser@example.com',
        )

        # Create additional data as needed for your tests

    def test_list_users(self):
        # Test fetching a list of users (GET /api/users/)
        url = reverse('user-list-create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions to verify the response data as needed

    def test_retrieve_user(self):
        # Test fetching a specific user by ID (GET /api/users/<id>/)
        url = reverse('user-retrieve-update', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions to verify the response data as needed

    def test_create_user(self):
        # Test creating a new user (POST /api/users/)
        url = reverse('user-list-create')
        data = {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'newuser@example.com',
            # Add more fields as needed
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Add more assertions to verify the response data and the database as needed

    def test_update_user(self):
        # Test updating a specific user (PUT /api/users/<id>/)
        url = reverse('user-retrieve-update', args=[self.user.id])
        data = {
            'username': 'updatedusername',
            'email': 'updatedemail@example.com',
            # Add more fields as needed for update
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions to verify the response data and the database as needed
