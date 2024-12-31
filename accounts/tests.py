from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse  # for URL reversing


class UsersManagersTests(TestCase):
    ...
class SignupPageTests(TestCase):  # Test for signup page

    def test_url_exists_at_correct_location_signupview(self):
        """
        Test if the signup URL exists at the correct location.
        """
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        """
        Test the signup view using the name defined in the URL configuration.
        """
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        """
        Test if the signup form creates a user correctly.
        """
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertEqual(get_user_model().objects.all().count(), 1)  # Check user count
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")  # Check username
        self.assertEqual(
            get_user_model().objects.all()[0].email, "testuser@email.com"
        )  # Check email
