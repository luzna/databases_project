from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=255)
    year_released = models.PositiveIntegerField()
    genre = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title


class Client(AbstractUser):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)


class Order(models.Model):
    STATUS_CHOICES = [
        (1, 'Opened'),
        (2, 'In progress'),
        (3, 'Closed')
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    client = models.ForeignKey(Client)

    def __str__(self):
        return self.client.username + dict(self.STATUS_CHOICES)[self.status]


class Item(models.Model):
    CARRIER_CHOICES = [
        (1, 'CD'),
        (2, 'Vinyl'),
        (3, 'Mp3'),
    ]
    price = models.PositiveIntegerField()
    condition = models.CharField(max_length=100)
    carrier = models.CharField(max_length=100)
    album = models.ForeignKey(Album)
    order = models.ForeignKey(Order, null=True, blank=True, default=None)

    def __str__(self):
        return self.album.title