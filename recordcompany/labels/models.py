from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
