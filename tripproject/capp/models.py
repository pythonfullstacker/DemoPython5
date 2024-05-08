from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img = models.ImageField(upload_to='gallery')
    review_text = models.TextField(null=True)  # Allow null values
    score = models.PositiveSmallIntegerField(default=0)
    link = models.URLField(max_length=200, blank=True)


    def __str__(self):
        return self.name