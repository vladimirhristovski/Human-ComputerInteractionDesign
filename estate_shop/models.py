from django.db import models
from django.contrib.auth.models import User


class Estate(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    area = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='estates/', null=True, blank=True)
    reserved = models.BooleanField(default=False, null=True, blank=True)
    sold = models.BooleanField(default=False, null=True, blank=True)
    characteristic = models.CharField(max_length=100, default="", null=True, blank=True)

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    sales = models.IntegerField(default=0, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'


class AgentsEstates(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.agent} - {self.estate}'


class Characteristic(models.Model):
    characteristic = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.characteristic


class EstatesCharacteristics(models.Model):
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.estate} - {self.characteristic}'
