from django.test import TestCase
from .models import Picture,Category

# Create your tests here.

# Set up method
class PictureTestClass(TestCase):
  def setUp(self):
    self.testing = Picture(image)
