from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class amazonScraper(models.Model):
    user = models.ForeignKey(User, verbose_name=(
        "related user"), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(validators=[MaxValueValidator(9999999)])
    date = models.DateField()
    amazonLink = models.URLField(("Amazon Scraper Link"), max_length=200)

    def __STR__(self):
        return self.amazonLink


class UserData(models.Model):
    user = models.OneToOneField(User, verbose_name=(
        "related user"), on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    date_of_signup = models.DateField(auto_now_add=True)
