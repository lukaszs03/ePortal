from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EtatInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    etat = models.CharField(max_length=100)
    etat_to = models.CharField(max_length=100)
    etat_form = models.CharField(max_length=100)

    def __str__(self):
        return self.etat

class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pesel = models.CharField(max_length=11)
    birth_date = models.CharField(max_length=100)

    def __str__(self):
        return self.pesel

class PhoneNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.address
    
class JobTitle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=1000)

    def __str__(self):
        return self.job_title
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.content}'
    
class PayList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    korekta = models.CharField(max_length=1000)
    kwota = models.CharField(max_length=10000)
    data_wyp = models.CharField(max_length=1000)

    def __str__(self):
        return self.korekta