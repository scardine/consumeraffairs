from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models


class Company(models.Model):
    """This is a toy Company model - in a real application we probably would
    store more information.
    """
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Review(models.Model):
    """This is the review model. In a real world application we would have a
    user profile model as well. I'm keeping this simple for the assignment.
    """
    RATING_VALIDATORS = [
        validators.MaxValueValidator(5, "Maximun rating is 5"),
        validators.MinValueValidator(1, "Minimun rating is 1"),
    ]
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    summary = models.TextField(max_length=10000)
    rating = models.IntegerField(validators=RATING_VALIDATORS, default=1)
    ip = models.GenericIPAddressField()
    date_submitted = models.DateTimeField(auto_now_add=True)


