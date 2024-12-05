from django.test import TestCase

from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Test password hash and validation'

    def handle(self, *args, **kwargs):
        try:
            user = User.objects.get(username='test')
            hashed_password = user.password 

            input_password = 'testpassword'
            is_correct = check_password(input_password, hashed_password)
            if is_correct:
                self.stdout.write("Password matches the hash!")
            else:
                self.stdout.write("Password does not match.")
        except User.DoesNotExist:
            self.stderr.write("User 'test' does not exist.")
