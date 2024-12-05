from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings

def validate_image(file):
    if not file.name.endswith(('.jpg', '.png', '.jpeg')):
        raise ValidationError('Only image files are allowed.')
    if file.size > 5 * 1024 * 1024:
        raise ValidationError('File size must be under 5MB.')
class MyModel(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def search_by_name(user_input):
        return MyModel.objects.filter(name=user_input)
    


class EvaluationRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()  # Item description
    contact_method = models.CharField(
        max_length=10,
        choices=[('phone', 'Phone'), ('email', 'Email')],
        default='email'
    )  # Preferred contact method
    photo = models.ImageField(upload_to='uploads/', validators=[validate_image])  # Photo upload
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"Request by {self.user.username} - {self.description[:20]}"

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

