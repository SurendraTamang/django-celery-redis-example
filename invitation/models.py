from django.db import models

# Create your models here.
class SignUpModel(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    full_address = models.CharField(max_length=500)
    

    def __str__(self) -> str:
        return self.full_name
    
    