from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):

    def setUp(self):
        self.api_list_url = reverse('api')
        self.auth_list_url = reverse('auth')
        self.data_1 = {'content': "content of the test"}
        self.data_2 = {'content': "second test note"}

        # Create an test user, so we can get authorisation token
        self.test_username = 'test_user'
        self.test_pass = 'test#@!password'
        self.user = User.objects.create_user(username=self.test_username, password=self.test_pass)
        Token.objects.create(user=self.user)

        # Add token to user requests, allowing to use auth api
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)

        return super(TestSetUp, self).setUp()

    def tearDown(self):
        user_to_delete = User.objects.get(username=self.test_username)
        user_to_delete.delete()
        return super().tearDown()


class TestViews(TestSetUp):
    """
    Tests GET, POST, PUT, DELETE requests for all views.
    Requests, that need data to operate on, contain post requests as well.
    """
    def test_redirect(self):
        # test redirection
        get_all = self.client.get('')
        self.assertEqual(get_all.status_code, 302)

    def test_auth_api_get(self):
        post_1 = self.client.post(self.auth_list_url, self.data_1)
        post_2 = self.client.post(self.auth_list_url, self.data_2)
        get_all = self.client.get(self.auth_list_url)
        get_1 = self.client.get(reverse('auth_detail', kwargs={"pk": 1}))
        get_2 = self.client.get(reverse('auth_detail', kwargs={"pk": 2}))
        get_3 = self.client.get(reverse('auth_detail', kwargs={"pk": 3}))
        self.assertEqual(get_all.status_code, 200)
        self.assertEqual(get_1.status_code, 200)
        self.assertEqual(get_2.status_code, 200)
        self.assertEqual(get_3.status_code, 404)

    def test_auth_api_post(self):
        post_1 = self.client.post(self.auth_list_url, self.data_1)
        post_2 = self.client.post(self.auth_list_url, self.data_2)
        self.assertEqual(post_1.status_code, 200)
        self.assertEqual(post_2.status_code, 200)

    def test_auth_api_put(self):
        post_1 = self.client.post(self.auth_list_url, self.data_1)
        post_2 = self.client.post(self.auth_list_url, self.data_2)
        put_1 = self.client.put(reverse('auth_detail', kwargs={"pk": 1}), self.data_2)
        put_2 = self.client.put(reverse('auth_detail', kwargs={"pk": 2}), self.data_1)
        self.assertEqual(put_1.status_code, 201)
        self.assertEqual(put_2.status_code, 201)

    def test_auth_api_delete(self):
        post_1 = self.client.post(self.auth_list_url, self.data_1)
        post_2 = self.client.post(self.auth_list_url, self.data_2)
        get_1 = self.client.get(reverse('auth_detail', kwargs={"pk": 1}))
        delete_1 = self.client.delete(reverse('auth_detail', kwargs={"pk": 1}))
        self.assertEqual(get_1.status_code, 200)
        self.assertEqual(delete_1.status_code, 204)

    def test_api_get(self):
        get_all = self.client.get(self.auth_list_url)
        self.assertEqual(get_all.status_code, 200)

    def test_api_initial_get(self):
        post_1 = self.client.post(self.auth_list_url, self.data_1)
        post_2 = self.client.post(self.auth_list_url, self.data_2)
        get_all = self.client.get(self.api_list_url)
        get_1 = self.client.get(reverse('api_retrieve', kwargs={"pk": 1}))
        get_2 = self.client.get(reverse('api_retrieve', kwargs={"pk": 2}))
        get_3 = self.client.get(reverse('api_retrieve', kwargs={"pk": 3}))
        self.assertEqual(get_all.status_code, 200)
        self.assertEqual(get_1.status_code, 200)
        self.assertEqual(get_2.status_code, 200)
        self.assertEqual(get_3.status_code, 404)


class TestViewsAuthentication(TestSetUp):
    def test_auth_unauthorized(self):
        """
        Tests denial of access when user has no or wrong token
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + "wrongtoken")
        post_1 = self.client.post(self.auth_list_url, self.data_1)
        post_2 = self.client.post(self.auth_list_url, self.data_2)
        post_3 = self.client.post(self.auth_list_url, self.data_1)
        get_all = self.client.get(self.auth_list_url)
        put = self.client.put(reverse('auth_detail', kwargs={"pk": 1}), self.data_2)
        delete = self.client.delete(reverse('auth_detail', kwargs={"pk": 1}))

        self.assertEqual(post_1.status_code, 401)
        self.assertEqual(post_2.status_code, 401)
        self.assertEqual(post_3.status_code, 401)
        self.assertEqual(get_all.status_code, 401)
        self.assertEqual(put.status_code, 401)
        self.assertEqual(delete.status_code, 401)
