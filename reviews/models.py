from django.contrib.auth import get_user_model
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    summary = models.TextField(max_length=10000)
    ip = models.GenericIPAddressField()
    date_submitted = models.DateTimeField(auto_now_add=True)


