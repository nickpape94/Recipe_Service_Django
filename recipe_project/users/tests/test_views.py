from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User
from users.models import Profile
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
import json


class UserRegistrationAPIViewTestCase(APITestCase):
    url = reverse("register")

    def test_invalid_password(self):
        """
        Test to verify that a post call with invalid passwords
        """
        user_data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password1": "password",
            "password2": "INVALID_PASSWORD"
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(400, response.status_code)

    def test_user_registration(self):
        """
        Test to verify that a post call with user valid data
        """
        user_data = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password": "123123",
            "password2": "123123"
        }
        response = self.client.post(self.url, user_data)
        self.assertEqual(201, response.status_code)
        self.assertTrue("token" in json.loads(response.content))

    def test_unique_username_validation(self):
        """
        Test to verify that a post call with already exists username
        """
        user_data_1 = {
            "username": "testuser",
            "email": "test@testuser.com",
            "password": "123123",
            "confirm_password": "123123"
        }
        response = self.client.post(self.url, user_data_1)
        self.assertEqual(201, response.status_code)

        user_data_2 = {
            "username": "testuser",
            "email": "test2@testuser.com",
            "password": "123123",
            "confirm_password": "123123"
        }
        response = self.client.post(self.url, user_data_2)
        self.assertEqual(400, response.status_code)
