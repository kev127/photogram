from django.test import TestCase
from .models import Profile

# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.Kelvin = Profile(name = 'Kelvin', profile_pic = 'image.jpg', bio='Small and simple thins makes me happy')
        self.Kelvin.save()

    def tearDown(self):
        Profile.objects.all().delete()
    

    def test_instance(self):
        self.assertTrue(isinstance(self.Kelvin, Profile))

    def test_save_method(self):
        self.Kelvin.save_profile()
        name = Profile.objects.all()

    def test_delete_method(self):
        self.profile_pic.delete_profile_pic()
        Profile = Profile.objects.all()
        self.assertTrue(len(Locations)==2) 


