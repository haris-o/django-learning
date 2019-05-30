from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=50)
    artists = models.ManyToManyField('artists.Artist')
    pub_date = models.DateField()

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    duration = models.DecimalField(decimal_places=2, max_digits=5)
    format = models.CharField(max_length=10)
    artists = models.ManyToManyField('artists.Artist')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
