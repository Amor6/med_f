from django.test import TestCase, Client
from django.urls import reverse
from main import models
from main.models import Category
from users.views import Register


class TestModels(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(
            name='Name1'
        )

    def test_home_page(self):
        category1 = Category.objects.create(
            name='dev'
        )


class TestRegisterViews(TestCase):

    def setUp(self):
        self.user = Register(
            username='test@test.com',
            password='123456'
        )



    def test_register(self):
        user = Register(
            username='test@test'
        )

