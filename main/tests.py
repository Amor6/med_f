from django.test import TestCase
from main.models import Category
from users.views import Register


class TestModels(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(
            name='Name1'
        )


class TestRegisterViews(TestCase):

    def setUp(self):
        self.user = Register(
            username='test@test.com',
            password='123456'
        )

    def test_register(self):
        self.user = Register(
            username='test@test')
