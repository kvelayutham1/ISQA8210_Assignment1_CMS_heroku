from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default=' ')
    address = models.CharField(max_length=50, blank=True, null=True, default=' ')
    city = models.CharField(max_length=50, default=' ')
    state = models.CharField(max_length=50, default='NE')
    zipcode = models.CharField(max_length=10, default='00000')
    email = models.EmailField(max_length=100, default=' ')
    cell_phone = models.CharField(max_length=50, default='(402)000-0000')
    acct_number = models.CharField(max_length=50, blank=True, null=True, default='00000')
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])


class Comment(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('client_list')



class Vehicle(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='vehicle',
    )
    make = models.CharField(max_length=50, default=' ')
    model = models.CharField(max_length=50, default=' ')
    VIN_number = models.CharField(max_length=50, default=' ')
    Date_of_Purchase = models.DateField(null=True, blank=True)
    Date_of_LastService = models.DateField(null=True, blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('client_list')

